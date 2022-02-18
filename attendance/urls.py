from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include



urlpatterns = [
   path('api/admin/', admin.site.urls),
   path('api/', include('dj_rest_auth.urls')),
   path('api/', include('allauth.urls')),
   path('api/registration/', include('dj_rest_auth.registration.urls')),
   path('api/accounts/', include('accounts.urls')),
   path('api/check/', include('check.urls'))
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)