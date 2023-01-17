"""Config file for key bindings."""


from libqtile.config import Key
from libqtile.lazy import lazy


def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    """Change the current window to the previous monitor."""
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i - 1)

def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    """Change the current window to the next monitor."""
    i = qtile.screens.index(qtile.current_screen)
    if i == 1:
        window_to_previous_screen(switch_screen=True)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i + 1)


mod = "mod4"
terminal = "alacritty"

keys = [
    # Change windows between screens
    Key([mod,"shift"], "n", lazy.function(window_to_next_screen, switch_screen=True)),
    Key([mod,"shift"], "v",  lazy.function(window_to_previous_screen, switch_screen=True)),

    # Spawn programs
    Key([mod], "f", lazy.spawn("firefox"), desc="Spawn firefox"),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),

    # Change focus to next monitor
    Key([mod], 'space', lazy.next_screen(), desc='Change focus to next monitor'),

    # Change between groups
    Key([mod], 'n', lazy.screen.next_group(), desc='Change focus to next monitor'),
    Key([mod], 'v', lazy.screen.prev_group(), desc='Change focus to next monitor'),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "p", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "q", lazy.reload_config(), desc="Reload the config"),

    # Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "u", lazy.spawn("rofi -show run"), desc="Spawn a command using a prompt widget"),
]


