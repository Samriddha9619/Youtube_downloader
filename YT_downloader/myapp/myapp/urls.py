from django.contrib import admin
from django.urls import include,path
from downloader import views
urlpatterns = [
    
    path('admin/', admin.site.urls),   
    path('', include('downloader.urls')),
]
