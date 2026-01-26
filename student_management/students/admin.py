from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_number', 'first_name', 'email', 'course', 'is_active')
    search_fields = ('roll_number', 'first_name', 'email')
