from ckeditor_uploader.fields import RichTextUploadingField
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save

from core.models import DateTimeMixin, SEOMixin
from core.utils import pre_save_post_receiver, upload_location


class SEOArticlesTotal(SEOMixin):
    """
    SEO as total item for all articles
    """


class Articles(DateTimeMixin, SEOMixin):
    title = models.CharField(verbose_name=u'Заголовок', max_length=500)
    cover_image = models.ImageField(upload_to=upload_location,
                                    null=True, blank=True,
                                    width_field="width_field",
                                    height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = RichTextUploadingField()
    slug = models.SlugField(editable=False, unique=True, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-date_created", "-date_updated"]
        verbose_name_plural = u"Статьи"


pre_save.connect(pre_save_post_receiver, sender=Articles)
