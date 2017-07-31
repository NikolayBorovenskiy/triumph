from django.db import models

DAYS_OF_WEEK = (
    (0, u'понедельник'),
    (1, u'вторник'),
    (2, u'среда'),
    (3, u'четверг'),
    (4, u'пятница'),
    (5, u'суббота'),
    (6, u'воскресенье'),
)


class Days(models.Model):
    title = models.CharField(max_length=12, choices=DAYS_OF_WEEK)
    
    def __unicode__(self):
        return '{}'.format(self.title)
    
    def __str__(self):
        return '{}'.format(self.title)


class Schedule(models.Model):
    title = models.CharField(verbose_name=u'Заголовок', max_length=255)
    work_days = models.ManyToManyField(
        Days, related_name='work_schedule', verbose_name=u'Рабочие дни')
    rest_days = models.ManyToManyField(
        Days, related_name='rest_schedule', verbose_name=u'Выходные дни')
    start = models.TimeField(verbose_name=u"Начало занятий", blank=True)
    end = models.TimeField(verbose_name=u"Конец занятий", blank=True)
    
    class Meta:
        verbose_name_plural = u"Расписание"


class Event(models.Model):
    name = models.CharField(verbose_name=u'Название', max_length=50)
    start = models.TimeField(verbose_name=u"Начало")
    finish = models.TimeField(verbose_name=u"Конец")
    day = models.ForeignKey(Days, verbose_name=u'День')
    
    def get_day(self):
        return u'{}'.format(self.day.title)
    
    class Meta:
        verbose_name_plural = u"Занятие"
