from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.core.views import home

urlpatterns = [
    path('', home, name='home'),

    path('admin/', admin.site.urls),

    # AUTH (Django built-in)
    path('auth/', include('django.contrib.auth.urls')),

    # USERS APP
    path('users/', include('apps.users.urls')),

    path('services/', include('apps.services.urls')),

    path('orders/', include('apps.orders.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)