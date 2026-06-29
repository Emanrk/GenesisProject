from django.contrib import admin
from django.urls import path, include
from genesisapp import views

handler404 = 'genesisapp.views.custom_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('genesisapp.urls')),
]
