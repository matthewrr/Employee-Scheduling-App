from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='events'),
    path('<int:year>/<int:month>/<int:day>/', views.event_detail_view),
]