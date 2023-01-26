# If you come from bash you might have to change your $PATH.
export PATH=$HOME/bin:/usr/local/bin:/usr/local/go/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Set name of the theme to load.
ZSH_THEME="powerlevel10k/powerlevel10k"

# Set list of plugins (separated by spaces).
plugins=(git)

source $ZSH/oh-my-zsh.sh

# User configuration
alias zshconfig="vim ~/.zshrc"
alias ohmyzsh="vim ~/.oh-my-zsh"

alias c="clear" # clear
alias ..="cd .." # go up one directory
alias h="history -10" # history

alias dgo="cd $HOME/dev/GoLang" # go to GoLang folder
alias dpy="cd $HOME/dev/Python" # go to Python folder
alias dcs="cd $HOME/dev/CS" # go to CS folder

alias gor="go run" # go run
alias gob="go build" # go build
alias gomi="go mod init" # go mod init
alias gomt="go mod tidy" # go mod tidy

alias gi="git init" # git init
alias gs="git status" # git status
alias gaa="git add ." # git add all
alias gc="git commit -m" # git commit -m "message"
alias gr="git remote add origin" # git remote add origin
alias gp="git push -u origin main" # git push -u origin main
