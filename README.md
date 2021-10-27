
# yWatch
## Watch youtube videos with mpv while saving the video to disk.

### Instalation

* **install using makepkg**
  * **`git clone https://github.com/prayzjomba/ywatch.git`**
  * **`cd ywatch`**
  * **`makepkg -si`**
  * if you get this *error* install **`archlinux-keyring`** then run again **`makepkg -si`**
![error](https://github.com/prayzjomba/kajhdfhakldfl/blob/main/sc/error.png)

* **install using pip**
  + check if **$HOME/.local/bin** is in *PATH* by running **`echo $PATH`**
  + if not add this line to your **bashrc** **`export PATH=$HOME/.local/bin:$PATH`**

  * ##### ubuntu/debian users:

    * **`sudo apt install xclip mpv youtube-dl`**
    * **`pip install ywatch`**

  * ##### Arch users:

    * **`sudo pacman -S xclip mpv youtube-dl`**
    * **`pip install ywatch`**
 
  * ##### Other users:
    * install **xclip**, **mpv** and **youtube-dl** with your package manager 
    * **`pip install ywatch`**


## Usage

![](https://github.com/prayzjomba/kajhdfhakldfl/blob/main/sc/usage.gif)
## `>> yw -h`
**The output/video files will be on ~/Videos/WATCHED**

	usage: yw [-h] [-b] [-c] [-d] [-f] [-p] [-m] [-r] [-s] [-sk] [-sp] [-v] [-w] [Quality]

 	Quality
                        1/8 = 1080p | 2 = 240p  | 3 = 360p  | 4 = 480p
                        7 = 720p    | 9 = 1440p | 0 = 2160p
                        w = worst   | b = best  | a = audio(m4a)
                        o = audio(opus)  | O = audio(Best Opus)
                        default is 480p

	optional arguments:
	  -h, --help            show this help message and exit
	  -b, --bar             enable bar
	  -c, --disable-clear   don't clear the screen
	  -d, --dir             save to current directory
	  -f, --fullscreen      enable fullscreen
	  -p, --playonly        play only, don't save
	  -m, --mkv             play mkv, default is mp4
	  -r, --disable-resume  don't resume, start at the beginning
	                        (wont work on live videos)
	  -s, --size            show size and exit
	  -sk, --size-mkv       show mkv size, don't forget the '-m' option
	  -sp, --size-mp4       show mp4 size
	  -v, --version         show version
	  -w, --watch           play after streaming

### Screenshots
![](https://github.com/prayzjomba/kajhdfhakldfl/blob/main/sc/1.png)
![](https://github.com/prayzjomba/kajhdfhakldfl/blob/main/sc/2.png)
![](https://github.com/prayzjomba/kajhdfhakldfl/blob/main/sc/3.png)
![](https://github.com/prayzjomba/kajhdfhakldfl/blob/main/sc/4.png)
![](https://github.com/prayzjomba/kajhdfhakldfl/blob/main/sc/5.png)
![](https://github.com/prayzjomba/kajhdfhakldfl/blob/main/sc/6.png)
![](https://github.com/prayzjomba/kajhdfhakldfl/blob/main/sc/7.png)






