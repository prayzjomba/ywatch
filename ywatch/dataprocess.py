# DATAPROCESS by (Prayz Jomba)
# last updated(10 sep 2021) 11:03:19 AM


import subprocess, re, os, tempfile
from time import sleep
from ywatch.checklink import link
import ywatch.menu as menu


# CHANGE DIR
tmp_dir = tempfile.gettempdir()

dataFile = f'{tmp_dir}/wFile.txt'
qualito = dict()


class Save:

    def linkAndTitle(self):
        with open(dataFile, 'w') as save:
            save.write(link) 

            try:
                dt = subprocess.run(['youtube-dl', '-e', '--get-duration', link, '--no-playlist'], timeout=15, capture_output=True)
                dtOut = dt.stdout.decode('utf-8')
                dtErr = dt.stderr.decode('utf-8')
                if dtOut:
                    save.write(f'\n{dtOut}')
                else:
                    if 'confirm your age' in dtErr:
                        menu.age_err()
                    elif 'Unable to download' in dtErr:
                        menu.con_err()
                    else:
                        menu.tim_err(link)
                    exit()
            except subprocess.TimeoutExpired:
                print(''); menu.tim_err(link)
                exit()
            except KeyboardInterrupt:
                print(''); menu.usr_err()
                exit()

    def data(self):
        with open(dataFile, 'a') as save_data:
            try:
                dd =  subprocess.run(['youtube-dl', '-F', link, '--no-playlist'], timeout=15, capture_output=True)
                ddOut = dd.stdout.decode('utf-8')
                if ddOut:
                    save_data.write(ddOut)
                else:
                    menu.con_err()
                    exit()
            except subprocess.TimeoutExpired:
                print(''); menu.tim_err(link)
                exit()
            except KeyboardInterrupt:
                print(''); menu.usr_err()
                exit()


class Read:
    def __init__(self):
        with open(dataFile, 'r') as data:
            self.data = data.read()
            self.dataL = self.data.splitlines()

    def link(self):
        return self.dataL[0]
    
    def title(self):
        return re.sub('[%\/|`$^]', '_', self.dataL[1])

    def duration(self):
        duration = self.dataL[2]
        if len(duration) == 2:
            duration = f'0:{duration}'
        return duration
    

    def listcheck(self, *quality):
        quality = list(quality)

        while len(quality) > 1 and not Read.qcheck(self, quality[0]):
            quality.pop(0)

        if bool(Read.qcheck(self, quality[0])):
            qlt = quality[0].split('\\')[0]
            return Read.qcheck(self, quality[0]), qlt

    def qcheck(self, quality):
        q = re.search(quality, self.data)
        if q:
            if q[0].startswith('9'):
                q = int(q[0].split() [0])
            else:
                q = Read.size_check(self, q[0])
        return q

    def size_check(self, *file):
        file_list = file
        file_one = len(file_list) == 1
        file = file_list[0]

        mkv = re.search('.*webm', file)
        if mkv:
            mkvq = mkv[0].split()[0]

        fileS = re.search('.*iB', file)
        if fileS is None:
            fileS = '?'
            return fileS
        else:
            fileS = fileS[0].split() [-1]
            if fileS[-3:] == 'KiB':
                fileS = float(fileS[:-3])
                fileS = round(fileS * 0.001024, 1)
                if mkv:
                    if mkvq not in ['249', '250', '251']:
                        opus = float(Read._opus(self)[:-5])
                        opusBest = float(Read._opusBest(self)[:-5])
                        if file_one:
                            fileS = round(fileS + opus, 1)
                        else:
                            fileS = round(fileS + opusBest, 1)

                elif not file.startswith('140') and not file.endswith('best'):
                    aac = float(Read._audio(self)[:-5])
                    fileS = round(fileS + aac, 1)
                fileS = f'{fileS} (MB)'
                return fileS

            elif fileS[-3:] == 'MiB':
                fileS = float(fileS[:-3])
                fileS = round(fileS * 1.048576, 1)
                if mkv:
                    if mkvq not in ['249', '250', '251']:
                        if file_one:
                            if not 'G' in Read._opus(self):
                                opus = float(Read._opus(self)[:-5])
                            else:
                                opus = float(Read._opus(self)[:-5]) * 1073.742
                            fileS = round(fileS + opus, 1)

                        else:
                            if not 'G' in Read._opusBest(self):
                                opusBest = float(Read._opusBest(self)[:-5])
                            else:
                                opusBest = float(Read._opusBest(self)[:-5]) * 1073.742
                            fileS = round(fileS + opusBest, 1)

                elif not file.startswith('140') and not file.endswith('best'):
                    if not 'G' in Read._audio(self):
                        aac = float(Read._audio(self)[:-5])
                    else:
                        aac = float(Read._audio(self)[:-5]) * 1073.742
                    fileS = round(fileS + aac, 1)

                if fileS > 1000:
                    fileS = round(fileS * 0.001, 2)
                    fileS = f'{fileS} (GB)'
                else:
                    fileS = f'{fileS} (MB)'
                return fileS

            else:
                fileS = float(fileS[:-3])
                fileS = round(fileS * 1.073742, 2)
                if mkv:
                    if mkvq not in ['249', '250', '251']:
                        if file_one:
                            if not 'G' in Read._opus(self):
                                opus = float(Read._opus(self)[:-5]) * 0.001
                            else:
                                opus = float(Read._opus(self)[:-5]) * 1.073742
                            fileS = round(fileS + opus, 2)

                        else:
                            if not 'G' in Read._opusBest(self):
                                opusBest = float(Read._opusBest(self)[:-5]) * 0.001
                            else:
                                opusBest = float(Read._opusBest(self)[:-5]) * 1.073742
                            fileS = round(fileS + opusBest, 2)

                elif not file.startswith('140') and not file.endswith('best'):
                    if not 'G' in Read._audio(self):
                        aac = float(Read._audio(self)[:-5]) * 0.001
                        fileS = round(fileS + aac, 2)
                    else:
                        aac = float(Read._audio(self)[:-5]) * 1.073742
                        fileS = round(fileS + aac, 2)
                fileS = f'{fileS} (GB)'
            return fileS

    def true(self):
        if (bool(re.search('KiB', self.data))):
            check = re.search('KiB', self.data)
        elif (bool(re.search('MiB', self.data))):
            check = re.search('MiB', self.data)
        else:
            check = re.search('GiB', self.data)
        return check


    def _audio(self):
        aac_size = Read.listcheck(self, '140\s.*m4a\s.*audio only.*')
        qualito['aac'] = aac_size[1]
        return aac_size[0]
    
    def _opus(self):
        sOpus = Read.listcheck(self, '249\s.*webm\s.*audio only.*', '250\s.*webm\s.*audio only.*', '251\s.*webm\s.*audio only.*')
        qualito['opus'] = sOpus[1]
        return sOpus[0]
    
    def _opusBest(self):
        bOpus = re.findall('.*webm\s.*audio only.*', self.data) [-1]
        size = Read.size_check(self, bOpus, 'A')
        qualito['best_opus'] = bOpus.split() [0]
        return size
    
    def _best(self):
        bestS = re.search('.*best', self.data) [0]
        bestq = bestS.split() [3]
        bestS = Read.size_check(self, bestS)
        return [bestS, bestq]

    def duration_menu(self):
        aac = Read._audio(self)
        opus = Read._opus(self)
        menu.duration_asize(Read.duration(self), aac, opus)

    def size_mp4(self):
        best    = Read._best(self)
        sAAC    = Read._audio(self)
        p240    = Read.listcheck(self, '133\s.*mp4\s.*video only.*', '395\s.*mp4\s.*video only.*')
        p360    = Read.listcheck(self, '134\s.*mp4\s.*video only.*', '396\s.*mp4\s.*video only.*')
        p480    = Read.listcheck(self, '135\s.*mp4\s.*video only.*', '397\s.*mp4\s.*video only.*')
        p720    = Read.listcheck(self, '136\s.*mp4\s.*video only.*', '298\s.*mp4\s.*video only.*', '398\s.*mp4\s.*video only.*', '698\s.*mp4\s.*video only.*')
        p1080   = Read.listcheck(self, '137\s.*mp4\s.*video only.*', '399\s.*mp4\s.*video only.*', '299\s.*mp4\s.*video only.*', '699\s.*mp4\s.*video only.*')
        p1440   = Read.listcheck(self, '400\s.*mp4\s.*video only.*', '700\s.*mp4\s.*video only.*')
        p2160   = Read.listcheck(self, '401\s.*mp4\s.*video only.*', '701\s.*mp4\s.*video only.*')


        qqq = []
        #qqq += menu.clr_size('Audio', sAAC)
        qqq += menu.clr_size('240p', p240)
        qqq += menu.clr_size('360p', p360)
        qqq += menu.clr_size('480p', p480)
        qqq += menu.clr_size('720p', p720)
        qqq += menu.clr_size('1080p', p1080)
        qqq += menu.clr_size('1440p', p1440)
        qqq += menu.clr_size('2160p', p2160)
        qqq += menu.clr_size('best', best)

        menu.data('MP4', qqq)

        qualito['mp4_240'] = p240
        qualito['mp4_360'] = p360
        qualito['mp4_480'] = p480
        qualito['mp4_720'] = p720
        qualito['mp4_1080'] = p1080
        qualito['mp4_1440'] = p1440
        qualito['mp4_2160'] = p2160


    def mkvBest(self):
        bestV = re.findall('.*webm.*', self.data) [-1]
        size = Read.size_check(self, bestV, 'B')
        bestq = bestV.split() [3]
        if bestq == 'DASH':
            bestq = bestV.split() [2].split('x') [1]
            bestq = f'{bestq}p'
        return [size, bestq]


    def size_mkv(self):
        best    = Read.mkvBest(self)
        k240    = Read.listcheck(self, '242\s.*webm\s.*video only.*')
        k360    = Read.listcheck(self, '243\s.*webm\s.*video only.*')
        k480    = Read.listcheck(self, '244\s.*webm\s.*video only.*', '333\s.*webm\s.*video only.*')
        k720    = Read.listcheck(self, '247\s.*webm\s.*video only.*', '302\s.*webm\s.*video only.*', '334\s.*webm\s.*video only.*')
        k1080   = Read.listcheck(self, '248\s.*webm\s.*video only.*', '303\s.*webm\s.*video only.*', '335\s.*webm\s.*video only.*')
        k1440   = Read.listcheck(self, '271\s.*webm\s.*video only.*', '308\s.*webm\s.*video only.*', '336\s.*webm\s.*video only.*')
        k2160   = Read.listcheck(self, '313\s.*webm\s.*video only.*', '315\s.*webm\s.*video only.*', '337\s.*webm\s.*video only.*')

        qqq = []
        qqq += menu.clr_size('240p', k240)
        qqq += menu.clr_size('360p', k360)
        qqq += menu.clr_size('480p', k480)
        qqq += menu.clr_size('720p', k720)
        qqq += menu.clr_size('1080p', k1080)
        qqq += menu.clr_size('1440p', k1440)
        qqq += menu.clr_size('2160p', k2160)
        qqq += menu.clr_size('best', best)

        menu.data('MKV', qqq)

        qualito['mkv_240'] = k240
        qualito['mkv_360'] = k360
        qualito['mkv_480'] = k480
        qualito['mkv_720'] = k720
        qualito['mkv_1080'] = k1080
        qualito['mkv_1440'] = k1440
        qualito['mkv_2160'] = k2160


    def live(self):
        l240  = Read.qcheck(self, '92\s.*mp4')
        l360  = Read.qcheck(self, '93\s.*mp4')
        l480  = Read.qcheck(self, '94\s.*mp4')
        l720  = Read.qcheck(self, '95\s.*mp4')
        l1080 = Read.qcheck(self, '96\s.*mp4')
        formats = [l240, l360, l480, l720, l1080]
        menu.liveFormats(formats)


def stream(link, quality, file, resume, playonly, fs):
    try:
        if playonly:
            rec     = ''
            stream  = subprocess.run(['mpv', f'--ytdl-format={quality}/best', link, fs, resume, '--loop-playlist=no', rec, '--player-operation-mode=pseudo-gui', '--autofit-larger=30%'])
            if stream.returncode != 0:
                print(''); menu.con_err()
            else:
                print('')
            exit()
        else:
            rec     = f'--stream-record={file}'
            stream  = subprocess.Popen(['mpv', f'--ytdl-format={quality}/best', link, fs, resume, '--loop-playlist=no', rec, '--player-operation-mode=pseudo-gui', '--autofit-larger=30%'])

            #WAITING..
            x = 0
            while not os.path.isfile(file):
                sleep(1)
                x += 1
                if x == 30:
                    print(''); menu.con_err()
                    stream.kill()
                    exit()

            #STREAMED FILE SIZE
            x = True
            while x:
                fsize = os.path.getsize(file)
                fsize = round(fsize * 0.000001, 1)
                if fsize > 1000:
                    fsize = round(fsize * 0.01, 2)
                    print(f'\rSize: {fsize}(GB)', end='')
                else:
                    print(f'\rSize: {fsize}(MB)', end='')
                if stream.poll() is not None:
                    print('\n')
                    x = False

    except KeyboardInterrupt:
        print(''); menu.usr_err()
        if not playonly: stream.terminate()
        exit()



