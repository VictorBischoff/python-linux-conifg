import os

def user_input_install_zsh():
    userInput = input("Do you want to install ZSH? (y/n): ")
    if userInput == "y":
        install_zsh()
    else:
        print("You did not want to install ZSH.")
        
def install_zsh():
    os.system("sudo apt install zsh")
    os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
    os.system("sudo apt install powerline fonts-powerline")
    os.system('git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k')
    os.system("mv ~/.zshrc ~/.zshrc.bak")
    os.system("cp ~/automation-scripts/ubuntu/.zshrc ~/.zshrc")