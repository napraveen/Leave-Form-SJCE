from django.urls import path 
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('login', views.login, name='login'),
    path('register',views.register,name='register'),
    path('letter',views.letter,name='letter'),
    path('fill',views.fill, name='fill'),
    path('admins',views.admins,name='admins'),
    path('accept/<str:id>',views.accept,name='accept'),
    path('clear',views.clear,name='clear'),
]