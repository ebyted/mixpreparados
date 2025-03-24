from django.urls import path
from .views_static import ProductsStaticView

urlpatterns = [
    path('', ProductsStaticView.as_view(), name='products'),
]