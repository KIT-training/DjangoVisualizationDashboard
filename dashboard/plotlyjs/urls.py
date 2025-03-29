from django.urls import path
from .views import *

urlpatterns = [
    path('BasicLinePlot/', BasicLinePlot, name='BasicLinePlot'),
]