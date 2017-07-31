from django.db import models

from core.utils import upload_location, cleanhtml
from ckeditor.fields import RichTextField
from core.models import ImageMixin


class Attainments(models.Model):
    intro = RichTextField()
    content = RichTextField()

    def __unicode__(self):
        return '{}...'.format(cleanhtml(self.intro[:100]))

    def __str__(self):
        return '{}...'.format(cleanhtml(self.intro[:100]))

    class Meta:
        verbose_name_plural = u"Достижения"


class Photo(ImageMixin):
    attainments = models.ForeignKey(Attainments)

    def __unicode__(self):
        return '{}'.format(self.id)

    def __str__(self):
        return '{}'.format(self.id)


class Diploma(ImageMixin):
    Photo.Meta.verbose_name_plural = u"Дипломы"

    attainments = models.ForeignKey(Attainments)

    def __unicode__(self):
        return '{}'.format(self.id)

    def __str__(self):
        return '{}'.format(self.id)
