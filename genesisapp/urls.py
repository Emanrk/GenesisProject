from django.urls import path
from genesisapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home_alt'),
    path('blog/', views.blog, name='blog'),
    path('details/', views.details, name='details'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('services/', views.services, name='services'),
    path('starter/', views.starter, name='starter'),
    path('contact/', views.contact, name='contact'),
    path('newsletter/', views.newsletter, name='newsletter'),
]
