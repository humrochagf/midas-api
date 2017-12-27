from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from djmoney.models.fields import MoneyField
from moneyed import Money

from .validators import validate_not_zero


class BoardQuerySet(models.QuerySet):

    def visible_by(self, user):
        if user.is_authenticated:
            return self.filter(Q(owner=user) | Q(users=user))


class Board(models.Model):

    name = models.CharField(verbose_name=_('name'), max_length=80)
    slug = models.SlugField(verbose_name=_('slug'))
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='owned_boards',
        verbose_name=_('owner'), on_delete=models.CASCADE)
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='boards',
        verbose_name=_('users'), blank=True)

    objects = BoardQuerySet.as_manager()

    def __unicode__(self):
        return self.name


class EntryQuerySet(models.QuerySet):

    def visible_by(self, user):
        if user.is_authenticated:
            return self.filter(Q(board__owner=user) | Q(board__users=user))


class Entry(models.Model):

    board = models.ForeignKey(
        'Board', related_name='entries', verbose_name=_('board'),
        on_delete=models.CASCADE)
    date = models.DateField(verbose_name=_('date'), default=now)
    description = models.CharField(
        verbose_name=_('description'), max_length=255)
    value = MoneyField(
        max_digits=10, decimal_places=2, verbose_name=_('value'),
        default_currency=settings.MIDAS_DEFAULT_CURRENCY,
        validators=[validate_not_zero])
    tag = models.ForeignKey(
        'Tag', related_name='entries', verbose_name=_('tag'),
        null=True, on_delete=models.SET_NULL)

    objects = EntryQuerySet.as_manager()

    def __unicode__(self):
        return self.description

    @property
    def is_income(self):
        return self.value > Money(0, settings.MIDAS_DEFAULT_CURRENCY)

    @property
    def is_outcome(self):
        return self.value < Money(0, settings.MIDAS_DEFAULT_CURRENCY)


class TagQuerySet(models.QuerySet):

    def visible_by(self, user):
        if user.is_authenticated:
            return self.filter(Q(board__owner=user) | Q(board__users=user))


class Tag(models.Model):

    board = models.ForeignKey(
        'Board', related_name='tags', verbose_name=_('board'),
        on_delete=models.CASCADE)
    name = models.CharField(verbose_name=_('name'), max_length=80)
    slug = models.SlugField(verbose_name=_('slug'))

    objects = TagQuerySet.as_manager()

    def __unicode__(self):
        return self.name
