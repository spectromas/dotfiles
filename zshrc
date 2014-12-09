#### Source Prezto ####
if [[ -s "${ZDOTDIR:-$HOME}/.zprezto/init.zsh" ]]; then
  source "${ZDOTDIR:-$HOME}/.zprezto/init.zsh"
fi

#### startx automatically ####
[[ $(tty) = "/dev/tty1" ]] && exec startx

#### PROMPT ####

autoload colors; colors;

if [[ "$terminfo[colors]" -ge 8 ]]; then
  colors
fi

setopt prompt_subst
setopt promptsubst
setopt promptpercent

local return_code="%(?..%{$fg[red]%}%? ↵%{$reset_color%})"
local user_host='%{$fg[green]%}%n@%m%{$reset_color%}'
local current_dir='%{$fg[blue]%}%~%{$reset_color%}'
local git_branch='$(git_prompt_info)%{$reset_color%}'

PROMPT="%{${fg[cyan]}%}[%{${fg[magenta]}%}%n%{${fg[cyan]}%}] %{${fg[yellow]}%}%~ %{${fg[cyan]}%}%#%{${fg[default]}%} "
RPROMPT="%{${fg[cyan]}%}[%{${fg[default]}%}%*%{${fg[cyan]}%}] %{${fg[default]}%} "

#ZSH_THEME_GIT_PROMPT_SUFFIX=""

## Git Prompt
function git_prompt_info() {
 ref=$(git symbolic-ref HEAD 2> /dev/null) || return
  echo "[%{$fg[yellow]%}${ref#refs/heads/}%{$reset_color%}]"
}

if [[ `uname` == 'Linux' ]]
then
    local user_host='%{$fg[yellow]%}%n@%m%{$reset_color%}'
    local current_dir='%{$fg[green]%}%~%{$reset_color%}'
fi
PROMPT="%{${fg[cyan]}%}[%{${fg[magenta]}%}%n%{${fg[cyan]}%}] %{${fg[yellow]}%}%~ %{${fg[cyan]}%}%#%{${fg[default]}%} "
RPROMPT="%{${fg[cyan]}%}[%{${fg[default]}%}%*%{${fg[cyan]}%}]%{${fg[default]}%} ${git_branch}"

## Vi mode prompt

precmd() {
  RPROMPT="%{${fg[cyan]}%}[%{${fg[default]}%}%*%{${fg[cyan]}%}]%{${fg[default]}%} ${git_branch}"
}
zle-keymap-select() {
  RPROMPT="%{${fg[cyan]}%}[%{${fg[default]}%}%*%{${fg[cyan]}%}]%{${fg[default]}%} ${git_branch}"
  [[ $KEYMAP = vicmd ]] && RPROMPT="%{${fg[cyan]}%}[%{${fg[default]}%}%*%{${fg[cyan]}%}]%{${fg[default]}%} ${git_branch}%{$fg[yellow]%}(VI-MODE)"
  () { return $__prompt_status }
  zle reset-prompt
}
zle-line-init() {
  typeset -g __prompt_status="$?"
}
zle -N zle-keymap-select
zle -N zle-line-init


autoload zcalc
setopt nohashdirs

# alias ls='ls --group-directories-first --time-style=+"%d.%m.%Y %H:%M" --color=auto -F'
# alias ll='ls -l --group-directories-first --time-style=+"%d.%m.%Y %H:%M" --color=auto -F'
# alias la='ls -la --group-directories-first --time-style=+"%d.%m.%Y %H:%M" --color=auto -F'
alias lad='ls -d .*(/)'
alias l.='ls -d .* --color=auto'
alias lsnew="ls -rl *(D.om[1,10])"	# display the ten newest files
alias lsold="ls -rtlh *(D.om[1,10])"	# display the ten oldest files
alias lssmall="ls -Srl *(.oL[1,10])"	# display the ten smallest files
# alias df='df -h'                        # Human-readable sizes
alias free='free -m'                    # Show sizes in MB
alias wq='exit'
alias isitinstalled='equery list "*" | grep'
alias gitdir='cd /home/alex/.git_repos'
alias prt='cd /etc/portage'
alias dirsize='du -h --max-depth=1 "$@" | sort -k 1,1hr -k 2,2f'
alias notes='nano ~/Documents/notes.txt'
alias mergex='xrdb -merge $HOME/.Xresources'
alias myip='curl ifconfig.me'
alias ...='cd ../..'
alias ....='cd ../../..'
alias .....='cd ../../../..'
alias ......='cd ../../../../..'
alias .......='cd ../../../../../..'
alias ping='ping -c 1 8.8.8.8;echo DNS:;ping -c 2 google.com'
alias zshconfig="vim ~/.zshrc"
alias awesomeconfig="vim ~/.config/awesome/rc.lua"
alias lf="leafpad"
alias dvdplay="mpv dvd:// --dvd-device"
alias rb="sudo /sbin/shutdown -r now"
alias sd="sudo /sbin/shutdown -h now"
alias emerge="sudo emerge"
alias revdep-fix="$SUDO revdep-rebuild -i -- -avt"
alias odel="emerge -av --depclean"
alias erm="sudo emerge -cav"
alias eq="equery"
alias update="sudo emerge --sync && sudo emerge -auDN @world"
alias euses="sudo vim /etc/portage/package.use"
alias nano="nano -w"
alias suspend="sudo pm-suspend" 
alias deb="ar vx "
alias gc="git clone"
alias gp="git pull"
alias pls='sudo !!'
alias make="make -j2"
alias acceptkeywords="sudo vim /etc/portage/package.accept_keywords"
alias kernelmake="cd /usr/src/linux && sudo genkernel --menuconfig all"
alias perform="sudo cpupower frequency-set -g performance"
alias conserve="sudo cpupower frequency-set -g conservative"
alias powersave="sudo cpupower frequency-set -g powersave"
alias ondeman="sudo cpupower frequency-set -g ondemand"
alias wifioverview="nmcli dev && nmcli dev wifi"
alias dua='du -s *(/DN) | sort -nr | cut -f 2- | while read a; do du -sh "$a"; done'	# show sorted directory sizes for all directories
alias duv='du -s *(/N) | sort -nr | cut -f 2- | while read a; do du -sh "$a"; done'	# show sorted directory sizes for visible directories only
alias duh='du -s .*(/N) | sort -nr | cut -f 2- | while read a; do du -sh "$a"; done'	# show sorted directory sizes for hidden directories only
alias skype='i686-pc-linux-gnu-apulse skype'
alias h='history -f 1 | less +G'
alias hh='history'
alias hashes="cat /home/alex/.zshrc | grep 'hash -d'"

#### Global Aliases ####
alias -g sprunge='| curl -F "sprunge=<-" http://sprunge.us'
alias -g Xresources=$HOME/.Xresources
alias -g xinitrc=$HOME/.xinitrc

bindkey '^[[7~' beginning-of-line                   # Home key
bindkey '^[[8~' end-of-line                         # End key
bindkey '^[[2~' overwrite-mode                      # Insert key
bindkey '^[[3~' delete-char                         # Delete key
bindkey '^[[A'  up-line-or-history                  # Up key
bindkey '^[[B'  down-line-or-history                # Down key
bindkey '^[[C'  forward-char                        # Right key
bindkey '^[[D'  backward-char                       # Left key
bindkey '^[[5~' history-beginning-search-backward   # Page up key
bindkey '^[[6~' history-beginning-search-forward    # Page down key
bindkey '^[[Z' reverse-menu-complete
# backspace and ^h working even after
# returning from command mode
bindkey '^?' backward-delete-char
bindkey '^h' backward-delete-char
bindkey '^r' history-incremental-search-backward	# ctrl-r = search history backward
bindkey -a 'gg' beginning-of-buffer-or-history
bindkey -a G end-of-buffer-or-history
bindkey -a u undo
bindkey '^G' what-cursor-position
bindkey '\e.' insert-last-word				# alt . to insert last word

HISTFILE=~/.zhistory
HISTSIZE=100000
SAVEHIST=100000

#### ex - archive extractor ####
## usage: ex <file> ##
ex() {
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;; *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1     ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}

LADSPA_PATH=~/.ladspa:$LADSPA_PATH
export LADSPA_PATH
#LXVST_PATH=~/.vst:$LXVST_PATH
#export LXVST_PATH
#export MPD_HOST=/home/alex/.mpd/socket

hash -d D=~/Downloads/					# there are my downloads
hash -d F=/usr/share/zsh/$ZSH_VERSION/functions/	# ZSH functions
hash -d MU=/Music/					# MP3s
hash -d GT=~/.git_repos/				# HG/GIT/SVN/..- Repos
hash -d Ptl=/usr/local/portage/				# Local overlay
hash -d Pt=/etc/portage/				# portage
hash -d B=~/bin/					# (Un)tested local hacks
hash -d CF=~/.config/					# Mutt, Slrn, Vim, ..
hash -d T=~/Downloads/Torrents				# Bittorrent is evil.. isn't it?
hash -d K=/usr/src/linux/				# Linux-Kernel
hash -d VL=/var/log					# often visited ;)

zstyle ':completion:*:*:kill:*:processes' list-colors '=(#b) #([0-9]#)*=0=01;31'

#### "ctrl-e D" to insert the actual datetime YYYY/MM ####
__insert-datetime-directory() { BUFFER="$BUFFER$(date '+%Y/%m')"; CURSOR=$#BUFFER; }
zle -N __insert-datetime-directory
bindkey '^eD' __insert-datetime-directory

#### "ctrl-e d" to insert the actual datetime YYYY-MM-DD--hh-mm-ss-TZ ####
__insert-datetime-default() { BUFFER="$BUFFER$(date '+%F--%H-%M-%S-%Z')"; CURSOR=$#BUFFER; }
zle -N __insert-datetime-default
bindkey '^ed' __insert-datetime-default

#### grep for running process, like: 'any vim' ####
any() {
if [[ -z "$1" ]] ; then
echo "any - grep for process(es) by keyword" >&2
echo "Usage: any <keyword>" >&2 ; return 1
else
local STRING=$1
local LENGTH=$(expr length $STRING)
local FIRSCHAR=$(echo $(expr substr $STRING 1 1))
local REST=$(echo $(expr substr $STRING 2 $LENGTH))
ps xauwww| grep "[$FIRSCHAR]$REST"
fi
}

path=(
  /home/alex/bin
  /usr/local/{bin,sbin}
  /{bin,sbin}
  /usr/{bin,sbin} 
  $path
)


