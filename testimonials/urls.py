from django.urls import path
from .views_static import TestimonialsStaticView

urlpatterns = [
    path('', TestimonialsStaticView.as_view(), name='testimonials'),
]
