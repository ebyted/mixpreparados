from django.urls import path
from .views_static import ContactStaticView

urlpatterns = [
    path('', ContactStaticView.as_view(), name='contact'),
]