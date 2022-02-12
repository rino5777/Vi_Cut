from django.shortcuts import render, get_object_or_404
from .form import Videof
from cv2 import cv2
import os
from .models import VideoForm

import glob
import os

# Create your views here.
def main(request):
    str =''
    
    count =float(0)
    directory = 'C:/Users/bgrin/Desktop/vf_2/vf/home/static/file/img/'
    #files = os.listdir(directory)
    os.chdir(directory)
    files=glob.glob('*.jpg')
    for filename in files:
        os.unlink(filename) #удаление всех файлов в папке img
    video_input = Videof(request.POST, request.FILES)
    if request.method == 'POST':
        
        if video_input.is_valid(): 
            video_input.save()
            vs = get_object_or_404(VideoForm)
            vidcap = cv2.VideoCapture(f"C:/Users/bgrin/Desktop/vf_2/vf/media/{vs.video} ")
            success,image = vidcap.read()
            while success:
                
                if count%20 == 0:
                    cv2.imwrite("C:/Users/bgrin/Desktop/vf_2/vf/home/static/file/img/%d.jpg" % count, image)     # save frame as JPEG file
                    success,image = vidcap.read()
                    print ('Read a new frame: ', success, count )
                    count += 1       
                else:
                    success,image = vidcap.read()
                    count += 1
            vs.delete()    
            return render (request, 'player/player.html',  )
    return render(request, 'home/t1.html', {'video_input':video_input} )