from django.urls import path
from django.conf.urls import include
from .views import *

app_name = 'musicians'

urlpatterns = [
    path('', MusicianListView.as_view(), name='musicians_list'),
    path('<slug:musician_slug>/', MusicianView.as_view(), name='show_musician'),
]