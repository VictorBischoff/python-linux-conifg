import os

def user_input_install_go():
    userInput = input("Do you want to install Go? (y/n): ")
    if userInput == "y":
        install_go()
    else:
        print("You did not want to install Go.")
        
def install_go():
    os.system("wget https://go.dev/dl/go1.19.5.linux-amd64.tar.gz")
    os.system("sudo tar -C /usr/local -xzf go1.19.5.linux-amd64.tar.gz")