# MENU by (Prayz Jomba)
# last updated(24 Oct 2021) 03:52:19 PM


from rich.panel import Panel
from rich.padding import Padding
from rich.console import Console
from rich import print as rprint
rinput = Console().input
from func_timeout import FunctionTimedOut, func_timeout


# COLORS
r   = 'b color(9)'      #red
lg  = 'b color(112)'    #light green
tc  = 'b color(155)'    #lightest green 
w   = 'b color(254)'    #white
g   = 'b color(46)'     #green
b   = 'b color(80)'     #blue
aq  = 'b color(78)'     #aqua
y   = 'b color(190)'    #yellow
pu  = 'b color(169)'    #purple
br  = 'b color(172)'    #brown
yo  = 'b color(220)'    #yellow/orange
ly  = 'b color(215)'    #light yellow


def con_err():
    ce = Panel.fit(f"[{yo}]Connection Error!![/{yo}]", border_style = yo)
    rprint(Padding(ce, (0, 28)))

def age_err():
    ce = Panel.fit(f"[{yo}]You have to sign in to watch this video!![/{yo}]", border_style = yo)
    rprint(Padding(ce, (0, 16)))

def tim_err(link):
    ce = Panel.fit(f"[{yo}]Check Your LINK[/{yo}]", border_style = yo)
    lk = f'[{w}]{link} [/{w}]'
    rprint(Padding(ce, (0, 30)))
    rprint(Padding(lk, (0, 18)))

def usr_err():
    ce = Panel.fit(f"[{yo}]You Killed Me [/{yo}]", border_style = yo)
    rprint(Padding(ce, (0, 30)))

def version(apn, ver):
    ap_name = f'[{br}]{apn}[/{br}]'
    ap_ver  = f'[{g}]{ver}[/{g}]'
    dev     = f'[{y}]Prayz Jomba[/{y}]'
    version = Panel.fit(f'[{w}]{ap_name} | ver({ap_ver}) | ({dev})', border_style = w)
    rprint(Padding(version, (0,20)))

def title(link, title):
    link    = f'[{w}]LINK: {link} [/{w}]'
    title   = f"[{w}]TITLE:[/{w}] [{tc}]{title}[/{tc}]"
    rprint(f'{title} \n{link}')

def bestQ(quality):
    global bestq

def duration_asize(duration, aac, opus):

    def s(size):
        if size is None:
            return f'[{r}]?(MB)[/{r}]'
        else:
            audioSize = size.split()
            sizeN = f'[{lg}]{audioSize[0]}[/{lg}]'
            sizeT = audioSize[1]
            if 'G' in sizeT:
                sizeT = f'[{pu}]{sizeT}[/{pu}]'
            else:
                sizeT = f'[{ly}]{sizeT}[/{ly}]'
            return sizeN+sizeT
    s_aac = s(aac)
    s_opus = s(opus)
    duration = f'[{w}]DURATION:[/{w}][{ly}] ([i {lg}]{duration}[/i {lg}])[/{ly}]'
    A = f'[{b}]M4A:[/{b}] [{lg}]{s_aac}[/{lg}]'
    O = f'[{aq}]OPUS:[/{aq}] [{lg}]{s_opus}[/{lg}]'

    #print(len(duration))
    #print(len(A))

    #dur_len
    if   len(duration) == 107: duration += '        '
    elif len(duration) == 108: duration += '       '
    elif len(duration) == 110: duration += '     '
    elif len(duration) == 111: duration += '    '
    elif len(duration) == 112: duration += '   '

    #aac_len
    if   len(A) == 95: A += '         '
    elif len(A) == 124: A += '         '
    elif len(A) == 125: A += '        '
    elif len(A) == 126: A += '       '
    elif len(A) == 127: A += '      '
    elif len(A) == 128: A += '     '
    elif len(A) == 130: A += '       '
    elif len(A) == 131: A += '      '
    elif len(A) == 132: A += '     '
    elif len(A) == 133: A += '    '
    #print(len(A), len(O), len(duration))
    rprint(f'{duration}[{ly}]| {A}| {O}[/{ly}]\n')


def clr_size(name, size):
    if type(size) is tuple:
        size = size[0]
    if type(size) is list:
        bestq = size[1]
        size  = size[0]

    if size is None:
        return ''

    elif len(size.split()) != 2:
        size = f'[{r}]{size}(MB)[/{r}]'
    else:
        size = size.split()
        ss = size[0]
        st = size[1]
        ss = f'[{lg}]{ss}[/{lg}]'
        if 'G' in st:
            st = f'[{pu}]{st}[/{pu}]'
        else:
            st = f'[{ly}]{st}[/{ly}]'
        size = ss+st
    if name == 'best':
        q = f' [{br}]({bestq})[/{br}]'
        size = size+q
    name = f'[{br}]{name}[/{br}]'

    sizeQu = f'{name} = {size}'
    #print(len(sizeQu))
    sizeQu = lens(sizeQu)
    sizeQu = [sizeQu]
    return sizeQu


def lens(size):
    if   len(size) == 66: size += '       '
    elif len(size) == 67: size += '      '
    elif len(size) == 97: size += '     '
    elif len(size) == 98: size += '    '
    elif len(size) == 99: size += '   '
    elif len(size) == 100: size += '  '
    elif len(size) == 101: size += '     '
    elif len(size) == 102: size += '    '
    elif len(size) == 103: size += '   '
    elif len(size) == 104: size += '  '
    elif len(size) == 106: size += '       '
    elif len(size) == 109: size += '         '
    elif len(size) == 107: size += '    '
    elif len(size) == 108: size += '   '
    elif len(size) == 122: size += '       '
    elif len(size) == 124: size += '     '
    elif len(size) == 125: size += '    '
    elif len(size) == 128: size += '   '
    return size


def data(fmat, qsize):
    qlen = len(qsize)
    if qlen == 1:
        rprint(f'[{w}]{fmat}:[/{w}][{ly}] {qsize[0]}[/{ly}]\n')
    elif qlen == 2:
        rprint(f'[{w}]{fmat}:[/{w}][{ly}] {qsize[0]}| {qsize[1]}[/{ly}]\n')
    elif qlen == 3:
        rprint(f'[{w}]{fmat}:[/{w}][{ly}] {qsize[0]}| {qsize[1]}| {qsize[2]}[/{ly}]\n')
    elif qlen == 4:
        rprint(f'''[{w}]{fmat}:[/{w}][{ly}] {qsize[0]}| {qsize[1]}| {qsize[2]}
     {qsize[3]}[/{ly}]\n''')
    elif qlen == 5:
        rprint(f'''[{w}]{fmat}:[/{w}][{ly}] {qsize[0]}| {qsize[1]}| {qsize[2]}
     {qsize[3]}| {qsize[4]}[/{ly}]\n''')
    elif qlen == 6:
        rprint(f'''[{w}]{fmat}:[/{w}][{ly}] {qsize[0]}| {qsize[1]}| {qsize[2]}
     {qsize[3]}| {qsize[4]}| {qsize[5]}[/{ly}]\n''')
    elif qlen == 7:
        rprint(f'''[{w}]{fmat}:[/{w}][{ly}] {qsize[0]}| {qsize[1]}| {qsize[2]}
     {qsize[3]}| {qsize[4]}| {qsize[5]}
     {qsize[6]}[/{ly}]\n''')
    elif qlen == 8:
        rprint(f'''[{w}]{fmat}:[/{w}][{ly}] {qsize[0]}| {qsize[1]}| {qsize[2]}
     {qsize[3]}| {qsize[4]}| {qsize[5]}
     {qsize[6]}| {qsize[7]}[/{ly}]\n''')
    elif qlen == 9:
        rprint(f'''[{w}]{fmat}:[/{w}][{ly}] {qsize[0]}| {qsize[1]}| {qsize[2]}
     {qsize[3]}| {qsize[4]}| {qsize[5]}
     {qsize[6]}| {qsize[7]}| {qsize[8]}[/{ly}]\n''')
    elif qlen == 10:
        rprint(f'''[{w}]{fmat}:[/{w}][{ly}] {qsize[0]}| {qsize[1]}| {qsize[2]}
     {qsize[3]}| {qsize[4]}| {qsize[5]}
     {qsize[6]}| {qsize[7]}| {qsize[8]}
     {qsize[9]}[/{ly}]\n''')


def live():
    live = Panel.fit(f'[{w}]This Video is [{br}]LIVE[/{br}][/{w}]',border_style = br)
    rprint(Padding(live, (0,27)))

def premier(duration):
    premier = Panel.fit(f'[{br}]PREMIERING NOW[/{br}]', border_style = br)
    duration = f'[{w}]DURATION:[/{w}][{ly}] ([i {lg}]{duration}[/i {lg}])[/{ly}]'
    rprint(f'{duration}')
    rprint(Padding(premier, (0, 30)))

def liveFormats(formats):
    global fList
    fList = [i for i in formats if i is not None]
    LL = len(fList)

    if 92 in fList:
        fList[fList.index(92)] = f'[{br}]240p[/{br}]'
    if 93 in fList:
        fList[fList.index(93)] = f'[{br}]360p[/{br}]'
    if 94 in fList:
        fList[fList.index(94)] = f'[{br}]480p[/{br}]'
    if 95 in fList:
        fList[fList.index(95)] = f'[{br}]720p[/{br}]'
    if 96 in fList:
        fList[fList.index(96)] = f'[{br}]1080p[/{br}]'

    lv = f'[{w}]LIVE:[/{w}][{y}]'
    if LL == 1:
        rprint(f'{lv} {fList[0]}[/{y}]')
    elif LL == 2:
        rprint(f'{lv} {fList[0]} | {fList[1]}[/{y}]')
    elif LL == 3:
        rprint(f'{lv} {fList[0]} | {fList[1]} | {fList[2]}[/{y}]')
    elif LL == 4:
        rprint(f'{lv} {fList[0]} | {fList[1]} | {fList[2]} | {fList[3]}[/{y}]')
    elif LL == 5:
        rprint(f'{lv} {fList[0]} | {fList[1]} | {fList[2]} | {fList[3]} | {fList[4]}[/{y}]')


def checker(listt, size, item, name):
    def qnf(n):
        qnotf = f'[s {r}]{name}[/s {r}]'
        if item == '':
            return f'[{lg}]{n}[/{lg}]'
        else:
            return f'{qnotf} [{lg}]{n}[/{lg}]'

    if size:
        result = bool([i for i in listt if i.endswith(item)])
        if result and item != '':
            return f'[{lg}]{name}[/{lg}]'
        else:
            if bool([i for i in listt if i.endswith('480')]):
                return qnf('480p (DEFAULT)')
            elif bool([i for i in listt if i.endswith('360')]):
                return qnf('360p')
            else:
                return qnf('best')
    else:
        result = bool([i for i in listt if item in i])
        if result and item != '':
            return f'[{lg}]{name}[/{lg}]'
        else:
            if bool([i for i in listt if '480p' in i]):
                return qnf('480p (DEFAULT)')
            elif bool([i for i in listt if '360p' in i]):
                return qnf('360p')
            else:
                return qnf('best')


def play(choice, size, mkv, video_quality, playonly):
    aac = video_quality.get('aac')
    opus = video_quality.get('opus')

    def bq():
        if mkv:
            if bool([i for i in video_quality if i.endswith('mkv_480')]):
                return '244+249/244+250/244+251/333+249/333+250/333+251'
            elif bool([i for i in video_quality if i.endswith('mkv_360')]):
                return '243+249/243+250/243+251'
            else:
                return '94/93/bestvideo[ext=webm]+bestaudio[ext=webm]/best'
        else:
            if bool([i for i in video_quality if i.endswith('mp4_480')]):
                return '135+140/397+140'
            elif bool([i for i in video_quality if i.endswith('mp4_360')]):
                return '134+140/396+140'
            else:
                return '94/93/best'
            

    def qqquality(mkvC, mp4C, name, LQ):
        if size:
            if mkv:
                qInfo = checker(video_quality, size, mkvC, name)
                vid = video_quality.get(mkvC)
                if name == 'm4a' or name == 'Opus' or name == 'Best Opus':
                    qPlay = f'{vid}/{bq()}'
                else:
                    qPlay = f'{vid}+{opus}/{bq()}'
            else:
                qInfo = checker(video_quality, size, mp4C, name)
                vid = video_quality.get(mp4C)
                if name == 'm4a' or name == 'Opus' or name == 'Best Opus':
                    qPlay = f'{vid}/{bq()}'
                else:
                    qPlay = f'{vid}+{aac}/{bq()}'
        else:
            qInfo = checker(fList, size, name, name)
            qPlay = f'{LQ}/{bq()}'
        return qInfo, qPlay


    if not choice:
        def na(n): return f'[{lg}]{n}[/{lg}]'

        n1 = na(1); n2 = na(2); n3 = na(3); n4 = na(4); n7 = na(7); n9 = na('[9]'); n0 = na('[0]')
        s = f'[{ly}]-[/{ly}]' ; nb = na('b'); nw = na('w')
        rprint(f'{nb}[{br}]est {s} {nw}orst {s} {n1}080p {s} {n2}40p {s} {n3}60p {s} {n4}80p {s} {n7}20p {s} {n9}1440p {s} {n0}2160p [/{br}]')

        try:
            try:
                def userChoice():
                    if mkv:
                        userC = rinput(f'[{w}]QUALITY:[{b}](mkv)[/{b}][{ly}] > ')
                    else:
                        userC = rinput(f'[{w}]QUALITY:[{b}](twice for mkv)[/{b}][{ly}] > ')
                    return userC
                choice = func_timeout(20, lambda: userChoice())
            except FunctionTimedOut:
                print('')
            if choice:
                if choice.count(choice[0]) == 2 and len(choice) == 2:
                    choice = choice[0]
                    cl = ['a', 'o', 'O', 'b', 'w', '1', '2', '3', '4', '7', '8', '9', '0']
                    if choice in cl:
                        mkv = True

        except KeyboardInterrupt:
            print(''); usr_err()
            exit()

    if choice == 'a':
        chkd = qqquality('aac', 'aac', 'm4a', '00')
        qInfo = chkd[0] ; qPlay = chkd[1]

    elif choice == 'o':
        chkd = qqquality('opus', 'opus', 'Opus', '00')
        qInfo = chkd[0] ; qPlay = chkd[1]

    elif choice == 'O':
        chkd = qqquality('best_opus', 'best_opus', 'Best Opus', '00')
        qInfo = chkd[0] ; qPlay = chkd[1]

    elif choice == 'b':
        qInfo = f'[{lg}]Best[/{lg}]'
        if mkv:
            qPlay = 'bestvideo[ext=webm]+bestaudio[ext=webm]/best'
        else:
            qPlay = 'best'

    elif choice == 'c':
        print('') ; exit()

    elif choice == 'w': 
        qInfo = f'[{r}]Worst[/{r}]'
        if mkv:
            qPlay = 'worstvideo[ext=webm]+worstaudio[ext=webm]/worst'
        else:
            qPlay = 'worstvideo[ext=mp4]+worstaudio[ext=m4a]/worst'

    elif choice == '1' or choice == '8':
        chkd = qqquality('mkv_1080', 'mp4_1080', '1080p', '96')
        qInfo = chkd[0] ; qPlay = chkd[1]

    elif choice == '2': 
        chkd = qqquality('mkv_240', 'mp4_240', '240p', '92')
        qInfo = chkd[0] ; qPlay = chkd[1]

    elif choice == '3': 
        chkd = qqquality('mkv_360', 'mp4_360', '360p', '93')
        qInfo = chkd[0] ; qPlay = chkd[1]

    elif choice == '4': 
        chkd = qqquality('mkv_480', 'mp4_480', '480p', '94')
        qInfo = chkd[0] ; qPlay = chkd[1]

    elif choice == '7':
        chkd = qqquality('mkv_720', 'mp4_720', '720p', '95')
        qInfo = chkd[0] ; qPlay = chkd[1]

    elif choice == '9':
        chkd = qqquality('mkv_1440', 'mp4_1440', '1440p', '00')
        qInfo = chkd[0] ; qPlay = chkd[1]

    elif choice == '0':
        chkd = qqquality('mkv_2160', 'mp4_2160', '2160p', '00')
        qInfo = chkd[0] ; qPlay = chkd[1]

    else: 
        qPlay = f'{bq()}'
        choice = None

    
    if choice:
        rprint(f'[{w}]PLAYING:[/{w}] {qInfo}')
    else:
        chkd = qqquality('', '', '', '')
        qInfo = chkd[0]
        rprint(f'[{w}]PLAYING:[/{w}] {qInfo}')

    if playonly:
        rprint(f'[{br}]PLAYONLY:[/{br}] [{lg}]Enabled[/{lg}]')
    else:
        if size:
            if choice == 'o' or choice == 'O':
                rprint(f'[{w}]OUTPUT:[/{w}] [{b}]opus[/{b}]')
            elif choice == 'a':
                rprint(f'[{w}]OUTPUT:[/{w}] [{b}]m4a[/{b}]')
            elif mkv:
                rprint(f'[{w}]OUTPUT:[/{w}] [{b}]mkv[/{b}]')
            else:
                rprint(f'[{w}]OUTPUT:[/{w}] [{yo}]mp4[/{yo}]')
        else:
            if mkv:
                rprint(f'[{w}]OUTPUT:[/{w}][s {r}]mkv[/s {r}] [{yo}]mp4[/{yo}]')
            else:
                rprint(f'[{w}]OUTPUT:[/{w}] [{yo}]mp4[/{yo}]')

    return qPlay, choice, mkv








