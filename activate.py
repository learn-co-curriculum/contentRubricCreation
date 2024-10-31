import os
import platform
import subprocess

def activate_venv():
    # Check if the virtual environment exists
    if not os.path.exists("./rubric-env"):
        print("Virtual environment not found. Creating a new virtual environment...")
        subprocess.call(["python3", "-m", "venv", "rubric-env"])
    
    # Detect the operating system
    user_os = platform.system()

    if user_os == "Linux" or user_os == "Darwin":  # Darwin is macOS
        venv_activate = "./rubric-env/bin/activate"
        install_command = f"source {venv_activate} && pip install -r requirements.txt && python rubric_script.py"
    elif user_os == "Windows":
        venv_activate = ".\\rubric-env\\Scripts\\activate"
        install_command = f"{venv_activate} && pip install -r requirements.txt && python rubric_script.py"
    else:
        raise Exception("Unsupported operating system.")

    # Activate the virtual environment, install dependencies, and run the script
    print(f"Activating virtual environment for {user_os}, installing dependencies, and running the script...")
    subprocess.call(install_command, shell=True)

if __name__ == "__main__":
    activate_venv()
