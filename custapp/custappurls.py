from django.urls import path 
from . import views

urlpatterns=[
    path('custhome/',views.custhome,name='custhome'),
    path('custlogout/',views.custlogout,name='custlogout'),
    path('viewcars/',views.viewcars,name='viewcars'),
    path('book/<cid>',views.book,name='book'),
    path('viewbookings/',views.viewbookings,name='viewbookings'),
    path('response/',views.response,name='response'),
    path('returncar/<id>',views.returncar,name='returncar'),
]