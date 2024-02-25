export VISUAL="${EDITOR}"
export EDITOR='nvim'
export TERMINAL='kitty'
export BROWSER='librewolf'
export HISTORY_IGNORE="(bspwall|ls|cd|pwd|exit|startx|reboot|shutdown|sudo su|sudo reboot|history|cd -|cd ..|c|v|pi|ms|mysql|g|update|list|upgrade|clean|mirrors|zshrc|code|subl)"

if [ -d "$HOME/.local/bin" ] ;
  then PATH="$HOME/.local/bin:$PATH"
fi

HISTFILE=$HOME/.cache/zsh/zhistory
HISTSIZE=5000
SAVEHIST=5000


export ZSH="$HOME/.oh-my-zsh"
eval "$(starship init zsh)"
zstyle ':omz:update' mode auto     

setopt AUTOCD              
setopt PROMPT_SUBST        
setopt MENU_COMPLETE       
setopt LIST_PACKED		     
setopt AUTO_LIST           
setopt HIST_IGNORE_DUPS	   
setopt HIST_FIND_NO_DUPS   
setopt COMPLETE_IN_WORD

plugins=(git zsh-autosuggestions zsh-syntax-highlighting zsh-history-substring-search autoswitch_virtualenv you-should-use auto-notify)

source $ZSH/oh-my-zsh.sh

alias mirrors="sudo reflector --verbose --latest 5 --country 'India' --age 6 --sort rate --save /etc/pacman.d/mirrorlist"
alias clean="sudo pacman -Scc --noconfirm && yay -Sc --noconfirm && paru -Sc --noconfirm"
alias purga="sudo pacman -Rns $(pacman -Qtdq) ; sudo fstrim -av"
alias update="sysupdates --update-system"
alias list="sysupdates --print-updates"
alias autoremove="sudo pacman -R $(pacman -Qdtq)"
alias scan_wifi="nmcli dev wifi rescan && nmcli dev wifi"
alias clock="peaclock --config-dir ~/.config/peaclock"


# tools
alias h='htop'
alias v='nvim'
alias c='bat'
alias f='ranger'

# ls
alias ls='lsd'
alias l='ls -l'
alias la='ls -a'
alias lla='ls -la'
alias lt='ls --tree'

# cpp
alias cpl='g++ -std=c++11 -Wall -o'

# python
alias penv='python -m venv .venv'
alias pi='python -m pip install'
alias pf='python -m pip freeze > requirements.txt'
alias pu='python -m pip install --upgrade pip'

# helpers
alias mysql="mariadb"
alias code="codium"
alias wt='curl wttr.in'
alias tar='tar -xf'
alias wget="wget -c"
alias fr="free -h --si"
alias fs="df --si"
alias zshrc="v ~/.zshrc"
alias q='exit'
