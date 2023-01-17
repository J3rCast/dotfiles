#!/bin/sh
setxkbmap latam
feh --bg-fill /home/jerson/Escritorio/fondos/1.jpg --bg-fill /home/jerson/Escritorio/fondos/2.jpg
systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target
picom &
