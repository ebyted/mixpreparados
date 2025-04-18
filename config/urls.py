from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),  # esta línea lo conecta todo
    path('cart/', include('cart.urls', namespace='cart')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('products/', include('products.urls')),
]

# Esto sirve las imágenes subidas en modo desarrollo
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)