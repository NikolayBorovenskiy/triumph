from django.db import models


# Create your models here.
class SEO(models.Model):
    title = models.CharField(
        verbose_name=u'Титул',
        max_length=200,
        default=u'Школа спортивного танца «Триумф»'
    )
    h1 = models.CharField(
        verbose_name=u'Заголовок первого уровня',
        max_length=200,
        default=u'Школа спортивного танца «Триумф»'
    )
    key_words = models.TextField(
        verbose_name=u'Ключевые слова',
        default=u"школа танцев, клуб танцев, харьков, в харькове, харьковская, триумф, ирина балагула, контемн, детский танец, танцы для детей, бальные танцы, хип-хоп, политех, хпи, НТУ 'ХПИ'"
    )
    description = models.TextField(
        verbose_name=u'Описание',
        default=u"Школа спортивного танца «Триумф» — известная школа танцев в Харькове. Танцы для каждого. Широкое расписание. Профессиональные преподаватели. Удобное расположение в центре города. Звоните и присоеденяйтесь! (067)256-54-26. С танцем по жизни!"
    )

    class Meta:
        verbose_name_plural = "SEO"
