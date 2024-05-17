" Vim Settings
let mapleader = " "
syntax on
set relativenumber 
set tabstop=4
set shiftwidth=4
set cursorline
set wildignore=*.docx,*.jpg,*.png,*.gif,*.pdf,*.pyc,*.exe,*.flv,*.img,*.xlsx
set wildmenu
set wildmode=list:longest

" Keybindings
" ---------------------
" Normal Mode
nnoremap <Leader>wq :wq<CR>
nnoremap <Leader>w :w<CR>
nnoremap <silent> <Leader>t :tabnew<CR>
nnoremap <silent> <C-w> :tabclose<CR>
nnoremap <silent> <C-u> <C-u>zz
nnoremap <silent> n nzzzv
nnoremap <silent> N Nzzzv
nnoremap <silent> <C-d> <C-d>zz
nnoremap <leader>s :%s/<C-r><C-w>//gI<Left><Left><Left>

" Visual & Select Mode
vnoremap <silent> J :m +1<CR>gv=gv
vnoremap <silent> K :m -2<CR>gv=gv
xnoremap <silent> <leader>p \_dP

" Insert Mode
inoremap <silent> <silent> <C-s> <Esc>:w<CR>
inoremap <silent> <C-w> :tabclose<CR>
inoremap <silent> jk <Esc>

