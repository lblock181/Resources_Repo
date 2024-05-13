set relativenumber 
set tabstop=4
set shiftwidth=4
syntax on
set cursorline
set wildignore=*.docx,*.jpg,*.png,*.gif,*.pdf,*.pyc,*.exe,*.flv,*.img,*.xlsx
set wildmenu
set wildmode=list:longest

" Keybindings
nnoremap <Leader>wq :wq<CR>
nnoremap <Leader>t :tabnew<CR>
inoremap <silent> <C-s> <Esc>:w<CR>
nnoremap <C-w> :tabclose<CR>
inoremap <C-w> :tabclose<CR>
inoremap <silent> jk <Esc>
