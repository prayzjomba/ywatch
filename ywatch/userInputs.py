# INPUTS by (Prayz Jomba)
# last updated(21 Oct 2021) 01:10:10 PM

import argparse


#CHECKING INPUTS
par = argparse.ArgumentParser(prog='yw', formatter_class=argparse.RawTextHelpFormatter, description='Watch Youtube videos with mpv while saving to disk.')
par.add_argument('Quality', nargs='?', help=
'''
1/8 = 1080p | 2 = 240p  | 3 = 360p  | 4 = 480p
7 = 720p    | 9 = 1440p | 0 = 2160p    
w = worst   | b = best  | a = audio(m4a)
o = audio(opus)  | O = audio(Best Opus)
default is 480p''')

par.add_argument('-b', '--bar', action='store_true', help='enable bar')
par.add_argument('-c', '--disable-clear', action='store_true', help="don't clear the screen")
par.add_argument('-d', '--dir', action='store_true', help="save to current directory")
par.add_argument('-f', '--fullscreen', action='store_true', help="enable fullscreen")
par.add_argument('-p', '--playonly', action='store_true', help="play only, don't save")
par.add_argument('-m', '--mkv', action='store_true', help="play mkv, default is mp4")
par.add_argument('-r', '--disable-resume', action='store_true', help="don't resume, start at the beginning\n(wont work on live videos)")
par.add_argument('-s', '--size', action='store_true', help="show size and exit")
par.add_argument('-sk', '--size-mkv', action='store_true', help="show mkv size, don't forget the '-m' option")
par.add_argument('-sp', '--size-mp4', action='store_true', help="show mp4 size")
par.add_argument('-v', '--version', action='store_true', help="show version")
par.add_argument('-w', '--watch', action='store_true', help="play after streaming")

args = par.parse_args()
