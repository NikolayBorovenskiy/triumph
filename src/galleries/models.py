from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from unidecode import unidecode

from core.models import DateTimeMixin, ImageMixin
from core.utils import (upload_location,
                        pre_save_post_receiver,
                        create_slug,
                        pre_save_photo_receiver)


class Gallery(DateTimeMixin):
    title = models.CharField(verbose_name=u'Заголовок', max_length=50)
    slug = models.SlugField(editable=False, unique=True, null=True, blank=True,
                            max_length=255)
    
    def __unicode__(self):
        return self.title
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("galleries:detail", kwargs={"slug": self.slug})
    
    def get_cover_photo(self):
        if self.photo_set.filter(is_cover_photo=True).count() > 0:
            return self.photo_set.filter(is_cover_photo=True)[0]
        elif self.photo_set.all().count() > 0:
            return self.photo_set.all()[0]
        else:
            return None
    
    class Meta:
        ordering = ["-date_created", "-date_updated"]
        verbose_name_plural = u"Фотогалерея"


class Photo(ImageMixin):
    gallery = models.ForeignKey(Gallery, null=True, blank=True)
    is_cover_photo = models.BooleanField(default=False)
    is_slider_photo = models.BooleanField(default=False)
    
    def get_gallery(self):
        return u'{}'.format(
            self.gallery.title if hasattr(self.gallery, 'title') else None)


pre_save.connect(pre_save_photo_receiver, sender=Photo)

pre_save.connect(pre_save_post_receiver, sender=Gallery)
