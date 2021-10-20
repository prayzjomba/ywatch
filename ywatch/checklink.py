#   CHECK LINK by (Prayz Jomba)
#   last updated(01 Sep 2021) 12:49:20 PM


import pyperclip
from rich.panel import Panel
from rich.padding import Padding
from rich import print as rprint



# COLORS
clink       = '[b color(112)]LINK[/b color(112)]'
notfound    = '[b color(254)]not found[/b color(254)]'
invalid     = '[b color(220)]Invalid[/b color(220)]'
bdr         = 'b color(9)'


# LINK CHECK
link = pyperclip.paste()
link = ''.join(link.split() [:1])


if not link:
    empty = Panel.fit(f"{clink} {notfound}", border_style = bdr)
    rprint(Padding(empty, (0, 30)))
    exit()

elif not link.startswith('https://') or 'you' not in link:
    invalid = Panel.fit(f"{invalid} {clink}", border_style = bdr)
    rprint(Padding(invalid, (0, 31)))
    exit()
