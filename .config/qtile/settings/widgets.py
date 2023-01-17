"""Config file for widgets."""


from libqtile import bar, widget
from libqtile.config import Screen


colors = {
        "background": "#565a60",
        "white": "#ffffff",
        "purple": "#ab70d9",
        "blue": "#01b3ff"
        }
screens = [
    Screen(
        top=bar.Bar(
                [
                    widget.Sep(
                        foreground=colors["background"],
                        background=colors["background"]
                    ),
                    widget.GroupBox(
                        inactive=colors["white"],
                        font="Caskaydia Cove Nerd Font",
                        highlight_method='block',
                        background=colors["background"],
                        this_current_screen_border="#ab70d9",
                        other_screen_border="#7f53a1",
                        fontsize=13
                    ),
                    widget.WindowName(
                        font="Caskaydia Cove Nerd Font Bold",
                        background=colors["background"],
                        foreground=colors["blue"],
                    ),
                    widget.TextBox(
                        text="\u2bc7",
                        fontsize=100,
                        background=colors["background"],
                        foreground=colors["purple"],
                        width=40,
                        padding=0
                    ),
                    widget.Net(
                        format="直 {down}  ↓↑ {up}",
                        prefix="M",
                        background=colors["purple"],
                        font="Caskaydia Cove Nerd Font Bold",
                    ),
                    widget.TextBox(
                        text="\u2bc7",
                        fontsize=100,
                        background=colors["purple"],
                        foreground=colors["blue"],
                        width=40,
                        padding=0
                    ),
                    widget.CPU(
                        font="Caskaydia Cove Nerd Font Bold",
                        background=colors["blue"],
                    ),
                    widget.TextBox(
                        text="\u2bc7",
                        fontsize=100,
                        background=colors["blue"],
                        foreground=colors["purple"],
                        width=40,
                        padding=0
                    ),
                    widget.Clock(
                        font="Caskaydia Cove Nerd Font Bold",
                        background=colors["purple"],
                        format="  %Y-%m-%d  %I:%M %p "
                    ),
                    widget.QuickExit(
                            default_text="  ",
                            font="Caskaydia Cove Nerd Font Bold",
                            fontsize=15,
                            countdown_format=" {} ",
                            background=colors["blue"]
                    )
                ],
                24,
            ),
        ),
    ]
