from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from debug.views import debug_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),  # esta línea lo conecta todo
    path('cart/', include('cart.urls', namespace='cart')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('products/', include('products.urls', namespace='products')),
#path('testimonials/', include('testimonials.urls')),
    path('debug/', debug_info),
]

# Esto sirve las imágenes subidas en modo desarrollo
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)