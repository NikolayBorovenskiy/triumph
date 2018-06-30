from ckeditor.fields import RichTextField
from django.db import models

from core.models import ImageMixin, SEOMixin
from core.utils import cleanhtml


class Attainments(SEOMixin):
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
        return '{}'.format(self.name)

    def __str__(self):
        return '{}'.format(self.name)


class Diploma(ImageMixin):
    Photo.Meta.verbose_name_plural = u"Дипломы"

    attainments = models.ForeignKey(Attainments)

    def __unicode__(self):
        return '{}'.format(self.name)

    def __str__(self):
        return '{}'.format(self.name)
