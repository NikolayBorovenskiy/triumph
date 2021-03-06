# coding: utf-8

import os
import re
import requests

from hashlib import md5
from unidecode import unidecode
from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.mail import send_mail as django_send_mail
from django.db.models import Model
from django.db.models.fields.files import FieldFile
from django.shortcuts import resolve_url
from django.template.loader import render_to_string
from django.utils.text import slugify


def upload_to(directory=None):
    """Загрузить файл в директорию `directory` с хешированным именем."""
    
    def uploader(instance, filename):
        ext = os.path.splitext(filename)[1]
        h = md5(filename.encode('utf-8')).hexdigest()
        parts = [h[:2], h[2:4], h + ext]
        if directory is not None:
            parts.insert(0, directory)
        return '/'.join(parts)
    
    return uploader


def send_mail(email, subject, template_html, template_txt, context, **kwargs):
    """
    Отправить email пользователю.

    Аргументы:
        email - адрес электронной почты
        subject - заголовок письма
        template_html - путь до шаблона с html разметкой
        template_txt - путь до текстового шаблона
        context - словарь с данными, с которыми будут отрендерены шаблоны
    """
    email_html = render_to_string(template_html, context)
    email_text = render_to_string(template_txt, context)
    django_send_mail(
        auth_user=settings.EMAIL_HOST_USER,
        auth_password=settings.EMAIL_HOST_PASSWORD,
        from_email=settings.DEFAULT_FROM_EMAIL,
        subject=subject,
        recipient_list=[email],
        fail_silently=kwargs.pop('fail_silently', True),
        html_message=email_html,
        message=email_text,
        **kwargs
    )


def save_url_to_file_field(model, url, save_to=None, filename=None):
    """
    Сохранить файл, доступный по адресу ``url`` в поле ``save_to`` модели ``model``.

    Аргументы:
        model — объект класса Model, либо FieldFile / ImageFieldFile
        url — ссылка на файл
        save_to — название файлового поля
        filename — новое имя для сохраняемого файла

    Примеры использования:
        save_file_from_url(gallery, '<url>', save_to='image')
        save_file_from_url(gallery.image, '<url>')
    """
    assert isinstance(model, (FieldFile,
                              Model)), '"model" argument should be a Model or FieldFile instance'
    
    if isinstance(model, FieldFile):
        field = model
    else:
        assert isinstance(save_to,
                          str), '"save_to" argument must be provided along with Model instance'
        field = getattr(model, save_to)
    
    r = requests.get(url)
    
    if not filename:
        filename = url.split('/')[-1]
    
    temp_file = NamedTemporaryFile(delete=True)
    temp_file.write(r.content)
    temp_file.flush()
    
    field.save(filename, File(temp_file), save=True)


def create_slug(sender, instance, new_slug=None):
    slug = slugify(unidecode(instance.title))
    if new_slug is not None:
        slug = new_slug
    qs = sender.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(sender, instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(sender, instance)


def pre_save_photo_receiver(sender, instance, *args, **kwargs):
    if not instance.name:
        instance.name = create_name(sender, instance)


def create_name(sender, instance, new_name=None):
    filebase, extension = instance.image.name.split(".")
    name = unidecode(filebase)
    if new_name is not None:
        name = new_name
    qs = sender.objects.filter(name=name).order_by("-id")
    exists = qs.exists()
    if exists:
        new_name = "%s-%s" % (name, qs.first().id)
        return create_name(sender, instance, new_name=new_name)
    return name


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    _cleanr = re.compile('&\w+;')
    _cleantext = re.sub(_cleanr, '', cleantext)
    return _cleantext
