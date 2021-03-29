import os
import subprocess

from django.conf import settings
from django.core.files.uploadedfile import UploadedFile

from videos.models import Video


def handle_uploaded_file(author: str, title: str, file: UploadedFile):
    """
    The function receives the video file, convert it to .mp4 format nd adds the watermark. Then save to db
    :param author: author of the video
    :param title: title of the video
    :param file: file that have been uploaded
    :return:
    """
    # Define the directory to video storage
    dir_with_videos = os.path.join(settings.MEDIA_ROOT, 'videos')
    if not os.path.exists(dir_with_videos):
        os.makedirs(dir_with_videos)

    # Receiving the video
    path_to_destination_file = os.path.join(dir_with_videos, title)
    with open(path_to_destination_file, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    # Converting the video and adding the watermark
    result_filename = f"wm-{title}.mp4"
    path_to_watermark = os.path.join("videos", "static", "images", "watermark.png")

    if os.path.isfile(path_to_destination_file):
        try:
            subprocess.run(['ffmpeg', '-i', os.path.join("media", "videos", title),
                            '-i', path_to_watermark,
                            '-filter_complex', "[0:v][1:v]overlay=10:10",
                            os.path.join("media", "videos", result_filename)])
        except Exception as e:
            print(e)

    # Delete the source file
    os.remove(path_to_destination_file)

    # Saving the info of the video to db
    if os.path.isfile(os.path.join(dir_with_videos, result_filename)):
        Video.objects.create(author=author,
                             title=title,
                             video=os.path.join('videos', result_filename))
        return True
    else:
        return False


def delete_video(pk: int):
    """
    The function deletes chosen by id video from the storage and from database
    :param pk: id of the video
    :return:
    """
    video = Video.objects.get(pk=pk)
    path_to_file = os.path.join(settings.MEDIA_ROOT, str(video.video))
    if os.path.isfile(path_to_file):
        os.remove(path_to_file)
    video.delete()
