from django.urls import path
from .views import mark_attendance, attendance_list

urlpatterns = [
    path('mark/', mark_attendance, name='mark_attendance'),
    path('list/', attendance_list, name='attendance_list'),
]
