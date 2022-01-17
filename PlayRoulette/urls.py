from django.contrib import admin
from django.urls import path, include, re_path

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('api/raw/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('admin/', admin.site.urls),
    path('api/user/', include('user.api.urls', 'account_api')),
    path('api/roulette/', include('roulette.api.urls', 'roulette_api')),
    path('api-auth/', include('rest_framework.urls'))
]