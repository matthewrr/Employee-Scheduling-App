from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.event_list, name='events'),
    path('create/', views.event_create, name='event_create'),
    # path('create/schedule/', views.schedule_create, name='schedule_create'),
    path('update_schedule/', views.update_schedule, name='update_schedule'),
    # path('templates/create/', views.create_template, name='create_template'), --> moved to schedules... but not yet
    # path('templates/create/generate/', views.generate_template, name='generate_template'), --> moved to schedules
    # path('templates/create/save/', views.save_template, name='save_template'),
    path('<int:pk>/update/', views.event_update, name='event_update'),
    path('<int:pk>/delete/', views.event_delete, name='event_delete'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.event_detail_view),
    path('export_events/',views.export_events, name='export_events'),
]