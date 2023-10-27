from django.urls import path, include
from .views import Home, ProfileList

app_name = 'netviesapp'


urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('profiles/', ProfileList.as_view(), name='profile-list')
]