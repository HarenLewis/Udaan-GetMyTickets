from django.conf.urls import url

from .views import (
    MovieScreenCreateListAPIView,
    SeatReservationCreateAPIView,
    ScreenSeatsListAPIView
)

urlpatterns = [
    url(r'^screens?/?$',
         MovieScreenCreateListAPIView.as_view(), name='add-screen'),

    url(r'^screens/(?P<screen_name>[\w\-]+)/reserve$',
         SeatReservationCreateAPIView.as_view(), name='reserve-seats'),
    
    url(r'^screens/(?P<screen_name>[\w\-]+)/seats$',
         ScreenSeatsListAPIView.as_view(), name='screeen-seats-data'),
]
