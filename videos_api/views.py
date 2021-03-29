from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

from videos.models import Video
from videos_api.serializers import VideoListSerializer, VideoDetailSerializer


class VideosListAPIView(ListAPIView):
    """
    Get list of videos
    """
    serializer_class = VideoListSerializer
    queryset = Video.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['title']
    ordering_fields = ['title']


class VideosDetailAPIView(RetrieveAPIView):
    """
    Get detail info about specified video
    """
    serializer_class = VideoDetailSerializer
    queryset = Video.objects.all()
