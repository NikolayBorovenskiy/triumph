from django.db import models

from core.utils import upload_location
from ckeditor.fields import RichTextField


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
    
    def __unicode__(self):
        return '{} {}'.format(self.last_name, self.first_name)
    
    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)
    
    class Meta:
        verbose_name_plural = u"Тренеры"
        ordering = ["id"]
