from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include



urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('dj_rest_auth.urls')),
   path('', include('allauth.urls')),
   path('registration/', include('dj_rest_auth.registration.urls')),
   path('accounts/', include('accounts.urls')),
   path('check/', include('check.urls'))
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)