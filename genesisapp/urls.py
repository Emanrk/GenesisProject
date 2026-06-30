
from django.contrib import admin
from django.urls import path
from genesisapp import views

urlpatterns = [

    path('admin/', admin.site.urls),
      path('', views.home, name='home'),  # Root URL → index.html
      path('details/', views.details, name='details'),
          path('blog/', views.blog, name='blog'),
            path('home/', views.home, name='home'),
              path('portfolio/', views.portfolio, name='portfolio'),
               path('services/', views.services, name='services'),
                path('starter/', views.starter, name='starter'),
]

 
    
