# pages/urls.py
from django.urls import path
from testimonials.views import testimonios_view
from .views_static import (
    HomeStaticView,
    ProductsStaticView,
    AboutStaticView,
    TestimonialsStaticView,
    ContactStaticView,
)

urlpatterns = [
    path('', HomeStaticView.as_view(), name='home'),
    #path('products/', ProductsStaticView.as_view(), name='products'),
    path('about/', AboutStaticView.as_view(), name='about'),
    path('testimonials/', testimonios_view, name='testimonials'),
    path('contact/', ContactStaticView.as_view(), name='contact'),
]
