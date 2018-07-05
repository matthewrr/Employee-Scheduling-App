from django.conf import settings
from django.conf.urls import include,url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from events import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^$', redirect_root),
    url(r'events/', include('events.urls')),
    url(r'employees/', include('employees.urls')),
    url(r'locations/', include('locations.urls')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)