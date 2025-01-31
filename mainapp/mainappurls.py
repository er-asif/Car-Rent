from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('services/',views.services,name='services'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('registration/',views.registration,name='registration'),
    path('login/',views.login,name='login'),
]