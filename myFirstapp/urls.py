from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.loginUser, name='login'),
    path('signin/', views.signin, name = 'sigin'),
    path('services/',views.services_p,name='services'),
    path('online/',views.online,name='online'),
    path('offline/',views.offline,name='offline'),
]