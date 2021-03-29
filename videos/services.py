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
    # Receiving the video
    path_to_destination_file = f'{settings.MEDIA_ROOT}/videos/{title}'

    with open(path_to_destination_file, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    # Converting the video and adding the watermark
    if os.path.isfile(path_to_destination_file):
        subprocess.run(['ffmpeg', '-i', f'media/videos/{title}', '-i', 'videos/static/images/watermark.png',
                        '-filter_complex', "[0:v][1:v]overlay=10:10", f'media/videos/wm-{title}.mp4'])

    # Saving the info of the video to db
    Video.objects.create(author=author,
                         title=title,
                         video=f'videos/wm-{title}.mp4')

    # Delete the source file
    if os.path.isfile(path_to_destination_file):
        os.remove(path_to_destination_file)


def delete_video(pk: int):
    """
    The function deletes chosen by id video from the storage and from database
    :param pk: id of the video
    :return:
    """
    video = Video.objects.get(pk=pk)
    path_to_file = f'{settings.MEDIA_ROOT}/{str(video.video)}'
    if os.path.isfile(path_to_file):
        os.remove(path_to_file)
    video.delete()
