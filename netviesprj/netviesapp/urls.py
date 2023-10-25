from django.urls import path, include
from .views import Home

app_name = 'netviesapp'


urlpatterns = [
    path('', Home.as_view(), name='Home')
]