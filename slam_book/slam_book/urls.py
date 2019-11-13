"""webpage1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showindex,name='home'),
    path('',views.showindex,name='admin'),
    path('',views.showindex,name='user1'),
    path('myadmin/',views.ShowAdmin.as_view(template_name="Admin_registration.html"),name='myadmin'),
    path('user_registration/', views.User_Registration.as_view(template_name="User_registration.html"), name='user'),
    path('admin_login/',views.Admin_Login.as_view(template_name="Admin_Login.html"), name='admin_login'),
    path('user_login_page/',views.Admin_Login.as_view(template_name="user_Login.html"), name='user_login_page'),
    path('admin_validation/',views.admin_validation, name='admin_validation'),
    path('store_user/', views.store_user, name = 'store_user'),
    path('user_login/',views.user_login,name = 'user_login')



]

