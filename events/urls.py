from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # url(r'^$', views.event_list_view, name='events'),
    url(r'^$', views.event_list, name='event_list'),
    # path('edit/', views.event_edit, name='edit'),
    # path('edit/<int:pk>/', views.event_edit, name='edit'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.event_detail_view),
    path('(?P<pk>\d+)/update/', views.event_update, name='event_update'),
    # path('myevents/', views.event_list, name='event_list'),
    path('create/', views.event_create, name='event_create'),
    path('(?P<pk>\d+)/update/', views.event_update, name='event_update'),
]

