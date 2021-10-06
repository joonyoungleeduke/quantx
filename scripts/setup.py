import os 
import subprocess 

CURR_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURR_DIR)

TIME_SERIES_DIR = os.path.join(BASE_DIR, 'timeseriesdb')
TIME_SERIES_SCRIPTS = os.path.join(TIME_SERIES_DIR, 'scripts')

PYTHON = 'python3'

SETUP_SCRIPT = "setup.sh"

def main():
    subprocess.call(os.path.join(CURR_DIR, SETUP_SCRIPT))
    subprocess.call([PYTHON, os.path.join(TIME_SERIES_SCRIPTS, 'dbsetup.py')])

if __name__ == "__main__":
    main()