from ubuntu.ubuntu_config_mkdir import user_input_mkdir
from ubuntu.ubuntu_config_docker import user_input_install_docker
from ubuntu.ubuntu_config_zsh import user_input_install_zsh

def main():
    # Install ZSH
    user_input_install_zsh()
    # Install Docker
    user_input_install_docker()
    # Create the dev directories
    user_input_mkdir()

    