# ~/.zshrc
export ZSH="$HOME/.oh-my-zsh"

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Options
setopt prompt_subst
setopt auto_list
setopt hist_find_no_dups
setopt hist_ignore_dups
zstyle ':omz:update' mode auto 

# Prompt
eval "$(starship init zsh)"

plugins=(git zsh-autosuggestions zsh-syntax-highlighting zsh-history-substring-search autoswitch_virtualenv you-should-use auto-notify)

# redefine what is ignored by auto-notify
export AUTO_NOTIFY_IGNORE=("ani-cli" "ranger" "nvim" "bat" "htop" "spotify" "mysql" "zshrc" "tgpt" "mov-cli" "calcurse" "npm" "node" "python")

source $ZSH/oh-my-zsh.sh

# Vars
export TERMINAL="kitty"
export BROWSER="brave"
export EDITOR="nvim"
export VISUAL="${EDITOR}"

# Aliases
alias mirrors="sudo reflector --verbose --latest 5 --country 'India' --age 6 --sort rate --save /etc/pacman.d/mirrorlist"
alias clean="sudo pacman -Scc --noconfirm && yay -Sc --noconfirm && paru -Sc --noconfirm"
alias purga="sudo pacman -Rns $(pacman -Qtdq) ; sudo fstrim -av"
alias update="sysupdates --update-system"
alias list="sysupdates --print-updates"
alias autoremove="sudo pacman -R $(pacman -Qdtq)"
alias scan_wifi="nmcli dev wifi rescan && nmcli dev wifi"

# tools
alias h='htop'
alias v='nvim'
alias c='bat'
alias f='ranger'

# git
alias g='git'
alias ga='git add'
alias gc='git commit -m -S'
alias gp='git push'
alias gpl='git pull'

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
alias mysql='mariadb'
alias code='codium'
alias wt='curl wttr.in'
alias tar='tar -xf'
alias wget="wget -c"
alias fr="free -h --si"
alias fs="df --si"
alias zshrc="v ~/.zshrc"
alias q='exit'

# custom
alias ani="ani-cli"
alias cal="calcurse"
alias spotify="spotify_player"
alias t="tgpt"
alias drive="/run/media/$USER/"
alias news="newsboat"

# History
HISTFILE=$HOME/.cache/zsh/zhistory
HISTSIZE=1000
SAVEHIST=1000

# history substring search options
bindkey '^[[A' history-substring-search-up
bindkey '^[[B' history-substring-search-down

# cute sudo
export SUDO_PROMPT="Give me %u's pass pls: "

# not found
command_not_found_handler() {
	printf "%s%s? I don't know what is it\n" "$acc" "$0" >&2
    return 127
}

if [ -d "$HOME/.local/bin" ] ;
  then PATH="$HOME/.local/bin:$PATH"
fi
