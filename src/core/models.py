# coding: utf-8

from django.db import models

from .utils import upload_location


class DateTimeMixin(models.Model):
    date_created = models.DateTimeField(
        'Дата создания', auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(
        'Дата обновления', auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class MetaFieldsMixin(models.Model):
    meta_title = models.CharField(
        'Тег <title>', max_length=255, blank=True, default='')
    meta_keywords = models.TextField(
        'Тег <keywords>', blank=True, default='')
    meta_description = models.TextField(
        'Тег <description>', blank=True, default='')

    class Meta:
        abstract = True


class ImageMixin(models.Model):
    name = models.CharField(verbose_name=u'Название',
                            max_length=50,
                            null=True,
                            blank=True)
    image = models.ImageField(upload_to=upload_location,
                              null=True, blank=True,
                              width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        verbose_name_plural = u"Фотографии"


class SEOMixin(models.Model):
    browser_title = models.CharField(
        verbose_name=u'Заголовок в браузере',
        max_length=200,
        default=u'Школа спортивного танца «Триумф»',
        null=True
    )
    h1 = models.CharField(
        verbose_name=u'Заголовок первого уровня',
        max_length=200,
        default=u'Школа спортивного танца «Триумф»',
        null=True
    )
    key_words = models.TextField(
        verbose_name=u'Ключевые слова',
        default=u"школа танцев, клуб танцев, харьков, в харькове, харьковская, триумф, ирина балагула, контемн, детский танец, танцы для детей, бальные танцы, хип-хоп, политех, хпи, НТУ 'ХПИ'",
        null=True
    )
    head_description = models.TextField(
        verbose_name=u'Описание для метатега',
        default=u"Школа спортивного танца «Триумф» — известная школа танцев в Харькове. Танцы для каждого. Широкое расписание. Профессиональные преподаватели. Удобное расположение в центре города. Звоните и присоеденяйтесь! (067)256-54-26. С танцем по жизни!",
        null=True
    )

    def __unicode__(self):
        return self.browser_title

    def __str__(self):
        return self.browser_title

    class Meta:
        abstract = True
        verbose_name_plural = "SEO"
