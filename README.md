# quantx

Please read through this entire README!

## SETUP

1. init_submodules.sh (see 'SCRIPTS')
2. * For each sub repo you will have to 'git branch' as needed (it will likely put you in a detached GIT head) * 
3. Test entire system 
    - ./scripts/setup.sh 
    - ./scripts/teardown.sh 
4. Test specific docker instances within sub-repos (read their README.md)

## SCRIPTS

IMPORTANT SCRIPTS: 
- init_submodules.sh : used for setting up subrepos 
- update_submodules.sh : used for updating subrepos 
- setup.sh : sets up all the commponents 
- teardown.sh : shuts down the components 

## STRUCTURE

### DB

TimescaleDB (https://www.timescale.com/)

### Server 

FastAPI (https://fastapi.tiangolo.com/)

### Client 

React, TypeScript, Redux