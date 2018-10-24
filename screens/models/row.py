import os

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

from rest_framework.reverse import reverse
from . import Screen


class Row(models.Model):
    class Meta:
        app_label = 'screens'
        db_table = 'screens_row'
        verbose_name = _('Row')
        verbose_name_plural = _('Rows')

    row_char = models.CharField(max_length=128,
                                help_text=_('Row character'),
                                unique=True
                                )

    screen = models.ForeignKey(Screen, related_name='rows')

    total_seats = models.IntegerField(db_index=True,
                                      help_text=_('The size of the resource')
                                      )

    def __str__(self):
        return '%s' % (self.row_char)
