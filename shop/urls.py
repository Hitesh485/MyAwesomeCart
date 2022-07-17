from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shopHome'),
    path('about/', views.about, name='AboutUs'),
    path('contact/', views.contact, name='ContactUs'),
    path('tracker/', views.tracker, name='TrackingStatus'),
    path('search/', views.search, name='search'),
    path('productView/', views.productView, name='productView'),
    path('checkout/', views.checkout, name='shopHome'),
    path('get_data/', views.get_data, name='get_data')
]