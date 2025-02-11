from django.contrib import admin
from django.urls import include,path
from downloader import views
urlpatterns = [
    path('youtube', views.youtube, name='youtube'),
    path('admin/', admin.site.urls),   
]
