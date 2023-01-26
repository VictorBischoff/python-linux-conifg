import os

homePath = "/home/$USER"

def user_input_mkdir():
    userInput = input("Do you want to create the dev directories? (y/n): ")
    
    # Create the dev directories
    if userInput == "y":
        create_dev_directory()
        create_dev_golang_directory()
        create_dev_python_directory()
        create_docker_configs()
    else:
        print("You did not want to create the dev directories.")



# Create a directory for the docker configs
def create_docker_configs():
    dockerPath = homePath + "/dockerConfigs"
    dockerPathCreate = os.path.join(homePath, dockerPath)
    os.mkdir(dockerPathCreate)

# Create a directory for the dev directory
def create_dev_directory():
    devPath = homePath + "/dev"
    devPathCreate = os.path.join(homePath, devPath)
    os.mkdir(devPathCreate)
    
# Create a directory for the dev/GoLang directory
def create_dev_golang_directory():
    devGolangPath = homePath + "/dev/GoLang"
    devGolangPathCreate = os.path.join(homePath, devGolangPath)
    os.mkdir(devGolangPathCreate)
    
# Create a directory for the dev/Python directory
def create_dev_python_directory():
    devPythonPath = homePath + "/dev/Python"
    devPythonPathCreate = os.path.join(homePath, devPythonPath)
    os.mkdir(devPythonPathCreate)