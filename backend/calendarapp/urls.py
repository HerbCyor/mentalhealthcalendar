from django.urls import path
from .views import CreateDayAPIView, DayAPIView

urlpatterns = [
    path("days/<int:calendar_id>", DayAPIView.as_view(), name='days-api'),
    path("days/new", CreateDayAPIView.as_view(), name='new-day-api'),
]