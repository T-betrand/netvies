from django.urls import path
from .views import Home

app_name = 'netviesapp'


urlpatterns = [
    path('', Home, name='home')
]