from django.urls import path

from videos_api.views import VideosDetailAPIView, VideosListAPIView
from videos_api.yasg import schema_view

urlpatterns = [
    path('videos/', VideosListAPIView.as_view(), name='videos-list-api'),
    path('videos/<int:pk>/', VideosDetailAPIView.as_view(), name='videos-detail-api'),
    path('', schema_view.with_ui('swagger')),
]
