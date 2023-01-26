from ubuntu.ubuntu_config_mkdir import user_input_mkdir as user_input_mkdir_ubuntu
from ubuntu.ubuntu_config_docker import user_input_install_docker as user_input_install_docker_ubuntu
from ubuntu.ubuntu_config_zsh import user_input_install_zsh as user_input_install_zsh_ubuntu
from ubuntu.ubuntu_config_go import user_input_install_go as user_input_install_go_ubuntu

def main():
    
    userOs = input("What OS are you using? (Ubuntu): ")
    userOs = userOs.lower().strip()
    while True:
        if userOs == "ubuntu":
            # Install ZSH
            user_input_install_zsh_ubuntu()
            # Install Go
            user_input_install_go_ubuntu()
            # Install Docker
            user_input_install_docker_ubuntu()
            # Create the dev directories
            user_input_mkdir_ubuntu()
        else:
            print("You did not enter a valid OS.")

    
if __name__ == "__main__":
    main()