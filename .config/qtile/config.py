import os
import subprocess

from libqtile import hook
from settings.keys import keys, mod
from settings.groups import groups, dgroups_key_binder
from settings.layouts import layouts
from settings.widgets import screens


@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "sart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D" 
