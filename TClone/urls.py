from TClone import views
#from django.conf.urls import path
from django.urls import path
#from . views import LoginView
#from TClone.forms import UserLoginForm
#from TClone.views import HomeView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView


app_name='TClone'

urlpatterns= [
path('', views.index, name='index'),
path('login/', views.authentication, name='login'),
path('signup/', views.signup, name='signup'),
path('logout/', views.logouter, name='logout'),
path('home/', views.tweeter, name='home'),]