from .views import SamerView
from .views import SamerAboutView
from django.urls import path

urlpatterns = [
    path('',SamerView.as_view(),name='samerhome'),
    path('about',SamerAboutView.as_view(),name='samerabout'),
]