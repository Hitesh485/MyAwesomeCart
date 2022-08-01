from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shopHome'),
    path('about/', views.about, name='AboutUs'),
    path('contact/', views.contact, name='ContactUs'),
    path('tracker/', views.tracker, name='TrackingStatus'),
    path('search/', views.search, name='search'),
    path('products/<int:myid>', views.productView, name='productView'),
    path('checkout/', views.checkout, name='shopHome'),
    path('handlerequest/', views.handlerequest, name='HandlRequest')
]