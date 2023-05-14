
from django.urls import path
from .views import IndexView, GetTimeView, StreamView
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('stream/', StreamView.as_view(), name='stream'),
    path('get_time/', GetTimeView.as_view(), name='get_time'),
]
