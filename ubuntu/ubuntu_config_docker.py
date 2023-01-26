import os

def user_input_install_docker():
    userInput = input("Do you want to install Docker? (y/n): ")
    if userInput == "y":
        install_docker()
    else:
        print("You did not want to install Docker.")

def install_docker():
    os.system("sudo apt-get remove docker docker-engine docker.io containerd runc")
    os.system("sudo apt-get update")
    os.system("sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common")
    os.system("sudo mkdir -p /etc/apt/keyrings")
    os.system("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg")
    os.system('echo \ "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable \ " | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null')
    os.system("sudo apt-get update")
    os.system("sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin")