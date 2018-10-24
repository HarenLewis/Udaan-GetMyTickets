import os

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

from rest_framework.reverse import reverse
from . import Row


class Seat(models.Model):
    class Meta:
        app_label = 'screens'
        db_table = 'screens_seat'
        verbose_name = _('Seat')
        verbose_name_plural = _('Seats')

    row = models.ForeignKey(Row, related_name='seats')

    seat_no = models.IntegerField(db_index=True,
                                  help_text=_('The seat no.')
                                  )

    is_aisle_seat = models.BooleanField(verbose_name='Is is it an aisle seat?', 
                                        default=False,
                                        help_text=_('Is is it an aisle seat?'),
                                        db_index=True
                                        )

    is_reserved = models.BooleanField(verbose_name='Has the seat been reserved?', 
                                      default=False,
                                      help_text=_('Reserve a seat'),
                                      db_index=True
                                      )

    reserved_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    null=True, blank=True,
                                    related_name='reservations')

    reserved_at = models.DateTimeField(auto_now_add=True, db_index=True,
                                       null=True, blank=True)
    
    def __str__(self):
        return '%s' % (self.seat_no)
