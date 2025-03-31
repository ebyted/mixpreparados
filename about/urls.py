from django.urls import path
from .views_static import AboutStaticView

urlpatterns = [
    path('', AboutStaticView.as_view(), name='about'),
]