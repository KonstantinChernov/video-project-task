from django.urls import path

from videos.views import UploadVideo, DeleteVideo, VideoView

urlpatterns = [
    path('', VideoView.as_view(), name='videos-list'),
    path('upload/', UploadVideo.as_view(), name='upload-video'),
    path('delete/<int:pk>', DeleteVideo.as_view(), name='delete-video'),
]
