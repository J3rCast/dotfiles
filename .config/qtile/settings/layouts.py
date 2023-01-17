"""Config file for layouts."""


from libqtile import layout
from libqtile.config import Match


layouts = [
    layout.Columns(
        margin = 8,
        border_width = 3,
        border_focus = ["#7a6ec0"],
        border_normal = ["#1b182c"]
        )
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
