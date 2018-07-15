from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.location_list, name='locations'),
    path('create/', views.location_create, name='location_create'),
    path('<int:pk>/update/', views.location_update, name='location_update'),
    path('<int:pk>/delete/', views.location_delete, name='location_delete'),
    # path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.event_detail_view),
]