import os

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _


class Theatre(models.Model):
    class Meta:
        app_label = 'screens'
        db_table = 'screens_theatre'
        verbose_name = _('Theatre')
        verbose_name_plural = _('Theatres')

    name = models.CharField(max_length=256,
                            help_text=_('theatre name'),
                            )

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name='created_theatres')

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    related_name='modified_theatres',
                                    null=True,
                                    blank=True)

    modified_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return '%s' % (self.name)