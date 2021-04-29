from os import path
# import subprocess
import os
import sys
from pydub import AudioSegment


        


def convertToWav(filename):
    name = filename.split('.')[0]
    outpath = 'app/wav'
    dst = outpath+"/"+name+'.wav';
    print('converting')
    sound = AudioSegment.from_mp3('app/media/'+filename);
    # print(os.listdir())
    sound.export(dst, format="wav");
    
