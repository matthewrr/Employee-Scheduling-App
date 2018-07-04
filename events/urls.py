from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^event_detail/', views.index, name='event_detail'),
]