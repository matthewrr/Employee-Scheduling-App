from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.event_list_view, name='events'),
    path('edit/', views.event_edit, name='edit'),
    path('edit/<int:pk>/', views.event_edit, name='edit'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.event_detail_view),
    url('(?P<pk>\d+)/update/$', views.event_update, name='event_update'),
]