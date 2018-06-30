# coding: utf-8
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save

from core.models import DateTimeMixin, SEOMixin
from core.utils import pre_save_post_receiver, upload_location


class SEONewsTotal(SEOMixin):
    """
    SEO as total item for all galleries
    """


class News(DateTimeMixin, SEOMixin):
    title = models.CharField(verbose_name=u'Заголовок', max_length=500)
    image = models.ImageField(upload_to=upload_location,
                              null=True, blank=True,
                              width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = RichTextField(verbose_name=u'Контент', null=True, blank=True)
    slug = models.SlugField(editable=False, unique=True, null=True, blank=True,
                            max_length=255)

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
