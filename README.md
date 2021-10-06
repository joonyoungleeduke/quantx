# quantx

## SETUP

1. ./scripts/init.sh 
2. Test docker-compose
3. Test specific docker instances within sub-repos 

## SCRIPTS

WARNING: Scripts get complicated by your platform. Some will work out of the gate, others will need configuring, but it is well worth getting them to work. Examples of potential configurations:
- The python (.py) scripts may need shell=True within the subprocess.calls
- The python (.py) scripts assume you have 'python3' in your system path AND that it has any necessary libraries (ie timeseriesdb dbsetup.py requires 'requests' and 'sqlparse')
    - If you don't want to install libraries globally, then create virtual environments


Please DO NOT push your local-specific (ie it's only applicable to your system) script changes to the main repo that everyone uses.

IMPORTANT SCRIPTS: 
- init.sh : used for setting up subrepos
- update.sh : used for updating subrepos (pulling)
- setup.py : sets up the docker containers AND fills the database with data 
- teardown.sh : remove docker containers 

## TECH 
- QuestDB (https://questdb.io/)
- FastAPI (https://fastapi.tiangolo.com/)

Along with Docker, Git, ...