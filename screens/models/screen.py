import os

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

from rest_framework.reverse import reverse


class Screen(models.Model):
    class Meta:
        app_label = 'screens'
        db_table = 'screens_screen'
        verbose_name = _('Screen')
        verbose_name_plural = _('Screens')

    # In case we need to add multiple screens for a theatre
    # theatre = models.ForeignKey(Theatre,
    #                             related_name='created_screens')

    screen_name = models.CharField(max_length=256,
                                   help_text=_('Screen name'),
                                   )

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name='created_screens')

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    related_name='modified_screens',
                                    null=True,
                                    blank=True)

    modified_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return '%s' % (self.screen_name)