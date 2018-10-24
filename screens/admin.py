from django.contrib import admin

from .models import *


class ScreenAdmin(admin.ModelAdmin):
    list_display = ('screen_name', 'created_by', 'created_at', 
                    'modified_by', 'modified_at')

class RowAdmin(admin.ModelAdmin):
    list_display = ('row_char', 'screen', 'total_seats')

class SeatAdmin(admin.ModelAdmin):
    list_display = ('row', 'seat_no', 'is_aisle_seat', 'is_reserved', 
                    'reserved_by', 'reserved_at')


admin.site.register(Screen, ScreenAdmin)
admin.site.register(Row, RowAdmin)
admin.site.register(Seat, SeatAdmin)
