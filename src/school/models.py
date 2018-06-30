from ckeditor.fields import RichTextField
from django.db import models

from core.models import ImageMixin, SEOMixin
from core.utils import upload_location


class School(SEOMixin):
    title = models.CharField(verbose_name=u'Название', max_length=60,
                             default=u'Труимф')
    about = RichTextField()
    promo = RichTextField()

    def has_related_object(self):
        return hasattr(self, 'contact') and self.car is not None

    def __unicode__(self):
        return '{}'.format(self.title)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name_plural = u"Школа"


class Coach(models.Model):
    last_name = models.CharField(verbose_name=u'Фамилия', max_length=20)
    first_name = models.CharField(verbose_name=u'Имя', max_length=20)
    avatar = models.ImageField(upload_to=upload_location,
                               null=True, blank=True,
                               width_field="width_field",
                               height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    title = RichTextField()
    quote = RichTextField()
    school = models.ForeignKey(School, blank=True, null=True)

    def __unicode__(self):
        return '{} {}'.format(self.last_name, self.first_name)

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)

    class Meta:
        verbose_name_plural = u"Тренеры"
        ordering = ["id"]


class Photo(ImageMixin):
    school = models.ForeignKey(School)

    def __unicode__(self):
        return '{}'.format(self.id)

    def __str__(self):
        return '{}'.format(self.id)


class DanceHall(models.Model):
    description = RichTextField()
    school = models.OneToOneField(School, related_name='hall')

    def get_school(self):
        return u'{}'.format(self.school.title)

    def __unicode__(self):
        return '{}'.format(self.id)

    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        verbose_name_plural = u"Танцевальный зал"


class Image(ImageMixin):
    dance_hall = models.ForeignKey(DanceHall)

    def __unicode__(self):
        return '{}'.format(self.id)

    def __str__(self):
        return '{}'.format(self.id)


class Contact(models.Model):
    school = models.OneToOneField(School, related_name='contact')
    address = models.CharField(verbose_name=u'Адресс', max_length=255)
    phones = models.CharField(verbose_name=u'Телефоны', max_length=255)
    work_time = models.CharField(verbose_name=u'Режим работы', max_length=255)

    def __unicode__(self):
        return self.address

    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural = u"Контакты"
