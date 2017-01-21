from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from unidecode import unidecode

from core.models import DateTimeMixin
from core.utils import upload_location, pre_save_post_receiver, create_slug


class Gallery(DateTimeMixin):
    title = models.CharField(verbose_name=u'Заголовок', max_length=50)
    slug = models.SlugField(editable=False, unique=True, null=True, blank=True)
    
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


class Photo(models.Model):
    name = models.CharField(verbose_name=u'Название',
                            max_length=50,
                            editable=False,
                            null=True,
                            blank=True)
    image = models.ImageField(upload_to=upload_location,
                              null=True, blank=True,
                              width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    gallery = models.ForeignKey(Gallery)
    is_cover_photo = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    def get_gallery(self):
        return u'{}'.format(self.gallery.title)
    
    class Meta:
        verbose_name_plural = u"Фотографии"


def pre_save_photo_receiver(sender, instance, *args, **kwargs):
    if not instance.name:
        instance.name = create_name(sender, instance)


def create_name(sender, instance, new_name=None):
    filebase, extension = instance.image.name.split(".")
    name = unidecode(filebase)
    if new_name is not None:
        name = new_name
    qs = sender.objects.filter(name=name).order_by("-id")
    exists = qs.exists()
    if exists:
        new_name = "%s-%s" % (name, qs.first().id)
        return create_name(sender, instance, new_name=new_name)
    return name


pre_save.connect(pre_save_photo_receiver, sender=Photo)

pre_save.connect(pre_save_post_receiver, sender=Gallery)
