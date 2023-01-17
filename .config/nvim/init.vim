set number
set mouse=a
set numberwidth=1
set clipboard=unnamed
syntax enable
set showcmd
set ruler
set encoding=utf-8
set showmatch
" set sw=2
set relativenumber
set laststatus
set noshowmode

"_________________PLUGINS BEGIN_________________

call plug#begin('~/.config/nvim/plugged')

" THEMES

" sonokai theme
Plug 'sainnhe/sonokai'

" gruvbox theme
Plug 'morhetz/gruvbox'

"Ayu theme
Plug 'ayu-theme/ayu-vim'

" tokyonight theme
Plug 'folke/tokyonight.nvim', { 'branch': 'main' }

" makes background transparent
Plug 'xiyaowong/nvim-transparent'

" allows commenting
Plug 'b3nj5m1n/kommentary'

" autocomplete pluggin
Plug 'ms-jpq/coq_nvim', {'branch': 'coq'}
Plug 'ms-jpq/coq.artifacts', {'branch': 'artifacts'}
Plug 'ms-jpq/coq.thirdparty', {'branch': '3p'}

"IDE
"indentetion lines
Plug 'Yggdroot/indentLine'
"allows to find by two chars
Plug 'easymotion/vim-easymotion'
"allows to display a tree to open other files without close neovim
Plug 'scrooloose/nerdtree'
"allows to navigate between windows open by nerdtree
Plug 'christoomey/vim-tmux-navigator'
"auto close some pairs
Plug 'jiangmiao/auto-pairs'

call plug#end()

"_________________THEMES CONFIG____________________
let g:transparent_enabled = v:true
set termguicolors     " enable true colors support

"----------CONFIG FOR AYU THEME--------------
"let ayucolor="light"  " for light version of theme
"let ayucolor="mirage" " for mirage version of theme
"let ayucolor="dark"   " for dark version of theme
" colorscheme ayu

"---------CONFIG FOR SONOKAI THEME-----------
" let g:sonokai_style = 'espresso'
" let g:sonokai_style = 'andromeda'
" let g:sonokai_style = 'maia'
colorscheme sonokai

" --------TOKYONIGHT THEME CONFIG-----------
"colorscheme tokyonight

" --------CONFIG FOR GRUVBOX THEME--------
" colorscheme gruvbox
" let g:gruvbox_contrast_dark = "hard"

let NERDTreeQuitOnOpen=1

let mapleader=" "

nmap <Leader>s <Plug>(easymotion-s2)
nmap <Leader>nt :NERDTreeFind<CR>
nmap <CR> o<Esc>
nmap <Leader>w :w<CR>
nmap <Leader>q :q<CR>
nmap <Leader>cc I/*<Esc>A*/<Esc>
nmap <Tab> I<Tab><Esc>
nmap <BS> a<BS><Esc>
imap jj <Esc>
imap <A-j> <Down>
imap <A-k> <Up>
imap <A-l> <Right>
imap <A-h> <Left>
