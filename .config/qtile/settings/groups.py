"""
Config file for groups.
Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
"""


from settings.keys import mod
from libqtile.config import Group
from libqtile.dgroups import simple_key_binder


groups = [
        Group("  ", layout='columns'),
        Group("  ", layout='columns'),
        Group("  ", layout='columns'),
        Group("  ", layout='columns'),
        Group("  ", layout='columns'),
        Group("  ", layout='columns'),
        Group(" ﮭ ", layout='columns'),
        Group(" 阮 ", layout='columns'),
        Group(" ﭮ ", layout='columns')
        ]

dgroups_key_binder = simple_key_binder("mod4")
