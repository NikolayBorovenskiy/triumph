# coding: utf-8
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save

from core.models import ImageMixin, SEOMixin
from core.utils import (pre_save_photo_receiver, pre_save_post_receiver)


class SEOStyleTotal(SEOMixin):
    """
    SEO as total item for all galleries
    """


class Style(SEOMixin):
    title = models.CharField(verbose_name=u'Заголовок', max_length=500)
    subtitle = models.CharField(
        null=True,
        blank=True,
        verbose_name=u'Подзаголовок',
        max_length=500
    )
    group = models.CharField(
        null=True,
        blank=True,
        verbose_name=u'Группа',
        max_length=100
    )
    content = RichTextField()
    slug = models.SlugField(editable=False, unique=True, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("styles:detail", kwargs={"slug": self.slug})

    def get_cover_photo(self):
        if self.photo_set.filter(is_cover_photo=True).count() > 0:
            return self.photo_set.filter(is_cover_photo=True)[0]
        elif self.photo_set.all().count() > 0:
            return self.photo_set.all()[0]
        else:
            return None

    class Meta:
        verbose_name_plural = u"Танцевальные направления"


class Photo(ImageMixin):
    style = models.ForeignKey(Style)
    is_cover_photo = models.BooleanField(default=False)

    def get_style(self):
        return u'{}'.format(self.style.title)


pre_save.connect(pre_save_photo_receiver, sender=Photo)
pre_save.connect(pre_save_post_receiver, sender=Style)
