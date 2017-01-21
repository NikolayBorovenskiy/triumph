# coding: utf-8
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save

from core.models import DateTimeMixin
from core.utils import upload_location, pre_save_post_receiver, create_slug


class ExampleModel(models.Model):
    content = RichTextUploadingField()


class ExampleNonUploadModel(models.Model):
    content = RichTextField()


class News(DateTimeMixin):
    title = models.CharField(verbose_name=u'Заголовок', max_length=500)
    image = models.ImageField(upload_to=upload_location,
                              null=True, blank=True,
                              width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField(verbose_name=u'Контент', null=True, blank=True)
    content1 = RichTextUploadingField()
    content2 = RichTextField()
    slug = models.SlugField(editable=False, unique=True, null=True, blank=True)
    
    def __unicode__(self):
        return self.title
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("news:detail", kwargs={"slug": self.slug})
    
    class Meta:
        ordering = ["-date_created", "-date_updated"]
        verbose_name_plural = u"Новости"


pre_save.connect(pre_save_post_receiver, sender=News)
