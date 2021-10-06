import os 
import subprocess 

CURR_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURR_DIR)

PYTHON = 'python3'

def main():
    subprocess.call([PYTHON, os.path.join(CURR_DIR, "setup.py")])
    subprocess.call(os.path.join(CURR_DIR, 'teardown.sh'))

if __name__ == "__main__":
    main()