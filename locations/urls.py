from django.conf.urls import url
from django.urls import path
from . import views

from locations.views import LocationList, LocationCreate, LocationSave

urlpatterns = [
    url(r'^$', LocationList.as_view(), name='locations'),
    path('create/', LocationCreate.as_view(), name='location_create'),
    path('<int:pk>/update/', views.location_update, name='location_update'),
    path('<int:pk>/delete/', views.location_delete, name='location_delete'),
    path('<int:pk>/save/', LocationSave.as_view(), name='location_save'),
    path('export_locations/',views.export_locations, name='export_locations'),
]