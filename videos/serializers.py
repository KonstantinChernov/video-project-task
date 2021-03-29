from rest_framework import serializers

from videos.models import Video


class VideoFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('video', )
