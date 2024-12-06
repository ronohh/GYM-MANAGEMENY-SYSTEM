"""
URL configuration for gymproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index, name='index'),
    path('register/', views.register, name='register'),
    # path('register', views.morning_subscribers, name='one_subscribers'),
    path('login/', views.login, name='login'),
    path('register_monthly_package/', views.monthly_package, name='monthly_package'),
    path('register_half_package/', views.half_package, name='half_package'),
    path('register_yearly_package/', views.yearly_package, name='yearly_package'),
    path('admin_classes/', views.admin_classes, name='classes'),

    # admin
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    # fetch database members table
    path('members/',views.members, name='members'),
    path('new_admin/', views.new_admin, name='new_admin'),

    # editing database members

    # instead of popping edit as a whole instead  the one picked will have specific id
    path('edit/<int:id>/' ,views.edit, name='edit'),
    path('edit_monthly_subscribers/<int:id>', views.edit_monthly_subscribers, name='monthly_subscribers'),
    path('edit_half_subscribers/<int:id>', views.edit_half_subscribers, name='half_subscribers'),
    path('edit_yearly_subscribers/<int:id>', views.edit_yearly_subscribers, name='yearly_subscribers'),
    # end of edits

    path('delete/<int:id>/' ,views.delete, name='delete'),
    path('delete_monthly_subscribers/<int:id>', views.delete_monthly_subscribers, name='delete_monthly_subscribers'),
    path('delete_half_subscribers/<int:id>', views.delete_half_subscribers, name='delete_half_subscribers'),
    path('delete_yearly_subscribers/<int:id>', views.delete_yearly_subscribers, name='delete_yearly_subscribers'),

    path('studentsapi/' ,views.studentsapi, name='studentsapi'),
    path('mpesaapi/',views.mpesaapi, name='mpesaapi'),
]
