from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('services/',views.services,name='services'),
    path('photos/', views.photos,name='photos'),
    path('contact/',views.contact,name='contact'),
    path('quote',views.quote,name='quote')
]