from django.urls import path
from . views import CancelBookingView, RoomListView,BookingListView,RoomDetailView
app_name = 'hotel'

urlpatterns=[
    path('room_list/', RoomListView, name='RoomListView'),
    path('booking_list/', BookingListView.as_view(), name='BookingListView'),
    # path('book/', BookingView.as_view(), name='BookingView'),
    path('room/<category>', RoomDetailView.as_view(), name='RoomDetailView'),
    path('booking/cancel/<pk>',CancelBookingView.as_view(), name='CancelBookingView'),
]
