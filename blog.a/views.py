import os
from os.path import abspath, isfile
from django.http import HttpResponse
from django.shortcuts import render
from .models import Video


def homepage(request):
    video1 = Video();
    video1.filename = "earth.mp4"
    # return HttpResponse('homepage')

    return render(request, 'homepage.html', { 'video1': video1})


def read_more(request):
    return render(request, 'read_more.html')


def about(request):
#    my_dir = os.path.dirname(__file__) + '/../static/'
#    mp3_file = os.path.join(my_dir, '489513__jdrose__11-fc-w2018-v2.mp3')
#    path = abspath(mp3_file)
#    if isfile(path):
#        play_mp3_file = mp3_file
#        mp3_file += " GOT!"
#    return HttpResponse(mp3_file)
    return render(request, 'about.html')
