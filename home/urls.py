from django.urls import path
from .views_static import HomeStaticView

urlpatterns = [
    path('', HomeStaticView.as_view(), name='home'),
]