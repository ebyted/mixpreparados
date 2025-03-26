from django.urls import path
from .views import ProductsStaticView

urlpatterns = [
    path('', ProductsStaticView.as_view(), name='products'),
]