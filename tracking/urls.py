from django.urls import path
from .views import index, video_feed
from .views import process_frame

urlpatterns = [
    path('', index, name='index'),
    path('video_feed/', video_feed, name='video_feed'),
     path("process_frame/", process_frame, name="process_frame"),
]