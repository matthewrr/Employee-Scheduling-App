from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.location_list_view, name='locations'),
    # path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.event_detail_view),
]