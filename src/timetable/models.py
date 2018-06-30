from django.db import models

from core.models import SEOMixin
from school.models import Coach

DAYS_OF_WEEK = (
    (0, u'понедельник'),
    (1, u'вторник'),
    (2, u'среда'),
    (3, u'четверг'),
    (4, u'пятница'),
    (5, u'суббота'),
    (6, u'воскресенье'),
)


class SEOScheduleTotal(SEOMixin):
    """
    SEO as total item for all galleries
    """


class Days(models.Model):
    title = models.CharField(max_length=12, choices=DAYS_OF_WEEK)

    def __unicode__(self):
        return '{}'.format(self.title)

    def __str__(self):
        return '{}'.format(self.title)


class Room(models.Model):
    name = models.CharField(verbose_name=u'Название', max_length=255)
    level = models.CharField(verbose_name=u'Этаж', max_length=255, blank=True,
                             null=True)
    number = models.CharField(verbose_name=u'Номер комнаты', max_length=255)

    def __unicode__(self):
        return '{0} {1}'.format(self.name, self.number)

    def __str__(self):
        return '{0} {1}'.format(self.name, self.number)

    class Meta:
        verbose_name_plural = u"Комнаты"


class Schedule(models.Model):
    room = models.OneToOneField(Room, on_delete=models.CASCADE,
                                primary_key=True, verbose_name=u'Комната')
    title = models.CharField(verbose_name=u'Заголовок', max_length=255)
    work_days = models.ManyToManyField(
        Days, related_name='work_schedule', verbose_name=u'Рабочие дни')
    rest_days = models.ManyToManyField(
        Days, related_name='rest_schedule', verbose_name=u'Выходные дни')
    start = models.TimeField(verbose_name=u"Начало занятий")
    end = models.TimeField(verbose_name=u"Конец занятий")

    def __unicode__(self):
        return '{0}, {1}'.format(self.title, self.room)

    def __str__(self):
        return '{0}, {1}'.format(self.title, self.room)

    class Meta:
        verbose_name_plural = u"Расписания"


class Event(models.Model):
    schedule = models.ForeignKey(Schedule, verbose_name=u'Расписание')
    name = models.CharField(verbose_name=u'Название', max_length=50)
    start = models.TimeField(verbose_name=u"Начало")
    finish = models.TimeField(verbose_name=u"Конец")
    day = models.ManyToManyField(Days, verbose_name=u'День')
    coach = models.ForeignKey(Coach, verbose_name=u'Преподаватель', blank=True,
                              null=True)
    additional_info = models.CharField(
        verbose_name=u'Дополнительная информация',
        max_length=255,
        default=u'',
        blank=True,
        null=True)
    color = models.CharField(verbose_name=u'Цвет', max_length=15, choices=(
        ('#EF5350', u'красный'), ('#AB47BC', u'фиолетовый'),
        ('#7E57C2', u'глубоко фиолетовый'), ('#5C6BC0', u'индиго'),
        ('#42A5F5', u'голубой'), ('#29B6F6', u'легко-голубой'),
        ('#26C6DA', u'циан'),
        ('#66BB6A', u'бирюзовый'), ('#9CCC65', u'зеленый'),
        ('#D4E157', u'лайм'),
        ('#FFEE58', u'желтый'), ('#FFCA28', u'янтарный'),
        ('#FFA726', u'оранжевый'),
        ('#FF7043', u'глубоко оранжевый'), ('#8D6E63', u'желтый'),
        ('#8D6E63', u'коричневый'), ('#78909C', u'серый')), )

    def get_day(self):
        available_days = [day.title for day in self.day.all()]

        return u'{}'.format(', '.join(available_days))

    class Meta:
        verbose_name_plural = u"Занятия"
