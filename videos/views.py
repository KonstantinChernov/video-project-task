import json

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages

from videos.forms import VideoForm
from videos.models import Video
from videos.serializers import VideoFileSerializer
from videos.services import delete_video, handle_uploaded_file


class VideoView(View):
    """ Main page view with list of videos and video player """
    def get(self, request):
        videos = Video.objects.all()
        # Serialize the video files to work with them in JS
        serializer = VideoFileSerializer(videos, many=True)
        videos_files = json.dumps(serializer.data)
        return render(request, 'listvideos.html', {'videos_info': videos,
                                                   'videos_files': videos_files})


class UploadVideo(View):
    """ View to page with upload videos functionality """
    def post(self, request):
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(author=form.cleaned_data['author'],
                                 title=form.cleaned_data['title'],
                                 file=request.FILES['video'])
            messages.success(request, "The video posted successfully")
            return redirect(reverse_lazy('videos-list'))
        else:
            messages.error(request, "The video loading failed")
            return render(request, 'uploadvideo.html', {'form': form})

    def get(self, request):
        form = VideoForm()
        return render(request, 'uploadvideo.html', {'form': form})


class DeleteVideo(View):
    """ View to delete the video """
    def get(self, request, pk):
        delete_video(pk)
        return redirect(reverse_lazy('videos-list'))
