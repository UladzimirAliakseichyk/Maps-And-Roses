
from django.contrib import admin
from django.urls import path, include
from main.views import main, rose_map
from rest_framework import routers
from feedback.views import RevewsApi

router = routers.DefaultRouter()
router.register('api/feedback',RevewsApi)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('aqua_pink', rose_map,name='aqua_pink'),
    path('avalanche_white', rose_map,name='avalanche_white'),
    path('freedom_red', rose_map,name='freedom_red'),
    path('naomi_red', rose_map,name='naomi_red'),
    path('naomi_white', rose_map,name='naomi_white'),
    path('penny_yellow', rose_map,name='penny_yellow'),
    path('pich_yellow', rose_map,name='pich_yellow'),
    path('pich_yellow', rose_map,name='pich_yellow'),
    path('', include(router.urls),name='api/feedback'),
    
]
