#!/usr/bin/python

# (yw) YOUTUBE-WATCH (Prayz Jomba)
#           >>>VERSION (0.6.3)<<<
#

# APP
ver = '0.6.3'
apn = 'yWatch'


# IMPORTS
import os, subprocess
from ywatch import userInputs, menu
from datetime import date


# USER INPUTS
userIn  = userInputs.args
user_q  = userIn.Quality

# VERSION
if userIn.version:
    menu.version(apn, ver)
    exit()

from ywatch import dataprocess

# DATA FILE
dataFile = dataprocess.dataFile
link = dataprocess.link

# FULL SCREEN
if userIn.fullscreen: #-f
    fs = '-fs'
else:
    fs = '--no-fs'


# FUNCTIONS
def menu_version():
    if userIn.bar:   #-b
        menu.version(apn, ver)
    else:
        print('')

def menu_title():
    menu.title(link, title)

def dataFileSize():
    return os.path.getsize(dataFile)

def savedLink():
    return dataprocess.Read().link()

def save_title():
    dataprocess.Save().linkAndTitle()

def save_data():
    dataprocess.Save().data()

def read_title():
    global duration, title
    title    = dataprocess.Read().title()
    duration = dataprocess.Read().duration()

def size_true():
    return dataprocess.Read().true()

def menu_data():
    dataprocess.Read().duration_menu()
    if userIn.size_mkv:
        dataprocess.Read().size_mkv()
    elif userIn.size_mp4:
        dataprocess.Read().size_mp4()
    else:
        dataprocess.Read().size_mkv()
        dataprocess.Read().size_mp4()

def video_quality():
    vq = (dataprocess.qualito)
    vq = {k:v for k,v in list(vq.items()) if v is not None}
    for k,v in vq.items():
        if type(v) == tuple:
            vq[k] = v[1]
    return vq

def live_formats():
    dataprocess.Read().live()

def stream():
    dataprocess.stream(link, quality, file, resume, userIn.playonly, fs)


# CLEAR SCREEN
if not userIn.disable_clear: #-c
    os.system('clear')

# CONDITIONS
if not os.path.isfile(dataFile):
    save_title()

if link == savedLink() and dataFileSize() > 60:
    read_title()
    menu_version()
    menu_title()

else:
    save_title()
    read_title()
    menu_version()
    menu_title()

if duration == '0':
    menu.live()
    if userIn.size:
        exit()

if dataFileSize() < 400:
    save_data()

if duration != '0' and not size_true():
    menu.premier(duration)

if size_true():
    menu_data()
else:
    live_formats()


if userIn.size:
    exit()


size_true = size_true()
quality = menu.play(userIn.Quality, size_true, userIn.mkv, video_quality(), userIn.playonly)

if not user_q:
    user_q = quality[1]
    userIn.mkv = quality[2]
quality = quality[0]


# DATE
date  = date.today()
today = date.strftime(f"Videos of ({date}) %a")

# CHANGE DIR
home = os.path.expanduser('~')  
if userIn.dir:
    folder = f'WATCHED/{today}'
else:
    folder = f'{home}/Videos/WATCHED/{today}'

if not os.path.isdir(folder):
    os.makedirs(folder)  
os.chdir(folder)   

x = 1

#AUDIO DIR
if user_q == 'a' or user_q == 'o' or user_q == 'O':
    if size_true:
        if not os.path.isdir('Audio'):
            os.makedirs('Audio') 
        os.chdir('Audio')

        if user_q == 'a':
            file = f'{title}.m4a'
            if os.path.isfile(file):
                while os.path.isfile(f'{title}{x}.m4a'):
                    x += 1
                file = f'{title}{x}.m4a'
        elif user_q == 'o':
            file = f'{title}.opus'
            if os.path.isfile(file):
                while os.path.isfile(f'{title}{x}.opus'):
                    x += 1
                file = f'{title}{x}.opus'
        else:
            file = f'{title} (Best Opus).opus'
            if os.path.isfile(file):
                while os.path.isfile(f'{title}{x} (Best Opus).opus'):
                    x += 1
                file = f'{title}{x} (Best Opus).opus'

elif userIn.mkv:
    file = f'{title}.mkv'
    if os.path.isfile(file):
        while os.path.isfile(f'{title}{x}.mkv'):
            x += 1
        file = f'{title}{x}.mkv'

else:
    file = f'{title}.mp4'
    if os.path.isfile(file):
        while os.path.isfile(f'{title}{x}.mp4'):
            x += 1
        file = f'{title}{x}.mp4'


#LIVE DIR
if duration == '0' or not size_true:
    if not os.path.isdir('Live'):
        os.makedirs('Live')
    os.chdir('Live')

    file = f'{title}.ts'
    if os.path.isfile(file):
        while os.path.isfile(f'{title}_{x}.ts'):
            x += 1
        file = f'{title}_{x}.ts'
    

#RESUME
if userIn.disable_resume:
    resume = '--no-resume-playback'
else:
    resume = '--resume-playback'


stream()


#TS TO MP4
if file.endswith('ts'):
    file_mp4 = f'{file[:-2]}mp4'
    if os.path.isfile(file_mp4):
        file_mp4 = file_mp4[:-4]
        while os.path.isfile(f'{file_mp4}_{x}.mp4'):
            x += 1
        file_mp4 = f'{file_mp4}_{x}.mp4'
    os.rename(file, file_mp4)
    file = file_mp4


#OPEN
if userIn.watch:
    subprocess.Popen(['mpv', fs, file, '--loop-playlist', '--player-operation-mode=pseudo-gui', '--autofit-larger=30%'])


exit()
#END
