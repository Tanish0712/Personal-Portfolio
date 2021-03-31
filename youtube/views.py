from django.shortcuts import render, get_object_or_404
from .models import video


def home(request):
    videos = video.objects.all()
    return render(request, 'video/all_videos.html', {'videos': videos})
