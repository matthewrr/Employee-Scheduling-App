from django.conf import settings
from django.conf.urls import include,url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from events import views
from .views import redirect_root

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', redirect_root),
    url(r'employees/', include('employees.urls')),
    url(r'events/', include('events.urls')),
    url(r'features/', include('sms.urls')),
    url(r'locations/', include('locations.urls')),
    url(r'^nested_admin/', include('nested_admin.urls')),
    url(r'company/', include('company_profile.urls')),
]

# profile: company v individual. admin = true in URL?pythonpython

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
