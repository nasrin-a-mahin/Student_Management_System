"""
URL configuration for student_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views 
from students import views as student_views 

urlpatterns = [
    path('admin/', admin.site.urls),

    path('dashboard/', accounts_views.dashboard_redirect, name='dashboard_redirect'),

    path('admin-dashboard/', accounts_views.admin_dashboard, name='admin_dashboard'),
    path('teacher-dashboard/', accounts_views.teacher_dashboard, name='teacher_dashboard'),
    path('student-dashboard/', accounts_views.student_dashboard, name='student_dashboard'),

    path('login/', accounts_views.login_view, name='login'),
    path('logout/', accounts_views.login_view, name='logout'),
    path('accounts/', include('accounts.urls')),

    path('students/', include('students.urls')),

    path('attendance/', include('attendance.urls')),

]


