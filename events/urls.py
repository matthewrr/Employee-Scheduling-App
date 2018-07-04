from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.event_list_view, name='events'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.event_detail_view),
]