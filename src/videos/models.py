from embed_video.fields import EmbedVideoField

from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save

from core.models import DateTimeMixin
from core.utils import upload_location, pre_save_post_receiver, create_slug


class Video(DateTimeMixin):
    video = EmbedVideoField(
        verbose_name=u'Ссылка на видеоролик',
        help_text=u'Можно добавить видео с YouTube, Soundcloud или Vimeo'
    )
    title = models.CharField(verbose_name=u'Заголовок', max_length=50)
    slug = models.SlugField(editable=False, unique=True, null=True, blank=True)
    
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
