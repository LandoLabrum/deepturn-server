from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.account, name="account"),
    path('cookies/', views.cookies, name="cookies"),
   #  path('logout/', views.logoutUser, name="logout"),
    ]