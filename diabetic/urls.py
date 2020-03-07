"""diabetic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
import app.views as views
from django.conf.urls import url
from accounts import views as account_views
import django.contrib.auth.views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.home,name='home'),
    url(r'^signup',account_views.signup,name='signup'),
    url(r'^logout',auth_views.LogoutView.as_view(),name='logout'),
    url(r'^login',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    url(r'^account',account_views.myaccount,name='myaccount'),
    url(r'^diagnose',views.diagnose,name='diagnose'),
    url(r'^checkout',views.checkout,name='checkout'),
    url(r'^charge',views.charge,name='charge')
   


]
