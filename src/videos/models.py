from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from embed_video.fields import EmbedVideoField

from core.models import DateTimeMixin, SEOMixin
from core.utils import pre_save_post_receiver


class SEOVideoTotal(SEOMixin):
    """
    SEO as total item for all galleries
    """


class Video(DateTimeMixin):
    video = EmbedVideoField(
        verbose_name=u'Ссылка на видеоролик',
        help_text=u'Можно добавить видео с YouTube, Soundcloud или Vimeo'
    )
    title = models.CharField(verbose_name=u'Заголовок', max_length=50)
    slug = models.SlugField(editable=False, unique=True, null=True, blank=True)
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
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("videos:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-date_created", "-date_updated"]
        verbose_name_plural = u"Видеогалерия"


pre_save.connect(pre_save_post_receiver, sender=Video)
