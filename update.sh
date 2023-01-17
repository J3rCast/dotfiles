#!/bin/bash
# Update the repo folder with the real dotfiles, avoiding push all
# config files that we dont need

# Copy all qtile config
cp -r ~/.config/qtile/* .config/qtile/
rm -f ./.config/qtile/__pycache__/*
rmdir ./.config/qtile/__pycache__
rm -f ./.config/qtile/settings/__pycache__/*
rmdir ./.config/qtile/settings/__pycache__

# Copy neovim config
cp -r ~/.config/nvim/* .config/nvim/ 2>/dev/null

# Copy picom config
cp -r ~/.config/picom/* .config/picom/

# Copy alacritty config
cp -r ~/.config/alacritty/* .config/alacritty/

# Copy rofi config
cp -r ~/.config/rofi/* .config/rofi/
