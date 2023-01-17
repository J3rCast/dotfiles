**DESCRIPTION**
# This is my neovim configuration

## This set some utilities in neovim
* set number ***set numbers at the left of the doc***
* set mouse=a ***allows to use mouse in neovim***
* set numberwidth=1 ***set the width of the numbers at the left***
* set clipboard=unnamed ***allows to copy text and paste it outside of the document***
* syntax enable
* set showcmd
* set ruler
* set encoding=utf-8
* set showmatch
* set sw=2 ***set tab to 2 spaces***
* set relativenumber ***show relative number at the left of the doc***
* set laststatus 
* set noshowmode ***hide the current mode***


## This is the begining of the plugin, this time im using vim plug, visit https://github.com/junegunn/vim-plug for instructions about installation
## Once you've install vim plug proceed type in normal mode:
```
:PlugInstall
```
call plug#begin('~/.config/nvim/plugged') ***this start the pluggins part***

## Themes
* Plug 'morhetz/gruvbox' *this is the theme*

## IDE
* Plug 'easymotion/vim-easymotion' ***allows you to move to every part in the screen by using keys: space>s***
* Plug 'scrooloose/nerdtree' ***allows you to move between directories without leaving the document by using keys: space>n>t***
* Plug 'christoomey/vim-tmux-navigator' ***allows to movw between windows usin Ctrl>movement keys (h,j,k,l)***
* Plug 'jiangmiao/auto-pairs' ***close automatically pairs like: () {} [] "" ''*** 

call plug#end() ***this end the pluggins part***

* colorscheme gruvbox
* let g:gruvbox_contrast_dark = "hard"
* let NERDTreeQuitOnOpen=1

# Keybindings
* let mapleader=" " ***set space as a leader key***

* nmap <Leader>s <Plug>(easymotion-s2) ***allows to use easymotion***
* nmap <Leader>nt :NERDTreeFind<CR> ***allows to use nerdtree***
* nmap <CR> o<Esc> ***when press enter in normal mode it will create a line break and get back to normal mode***
* nmap <Leader>w :w<CR> ***save changes***
* nmap <Leader>q :q<CR> ***quit***
* imap jj <Esc> ***get back to normal mode***
* imap <A-j> <Down> ***allows you to move the cursor in insert mode with Alt and movement keys(h,j,k,l)***
* imap <A-k> <Up> ***allows you to move the cursor in insert mode with Alt and movement keys(h,j,k,l)***
* imap <A-l> <Right> ***allows you to move the cursor in insert mode with Alt and movement keys(h,j,k,l)***
* imap <A-h> <Left> ***allows you to move the cursor in insert mode with Alt and movement keys(h,j,k,l)***
