# quantx

Please read through this entire README!

## DEVELOPMENT

- There IS hot reloading for the client in docker-compose
- Use rebuild scripts to rebuild parts of the stack during development

## SETUP

1. init_submodules.sh (see 'SCRIPTS')
2. For each sub repo you will have to 'git branch' as needed (it will likely put you in a detached GIT head) 
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
- rebuild_... : rebuild ... part of stack 
    - client.sh 
    - db.sh
    - server.sh 

## STRUCTURE

### DB

TimescaleDB (https://www.timescale.com/)

### Server 

FastAPI (https://fastapi.tiangolo.com/)

### Client 

- Netlify 
  - https://quantx-algo.netlify.app/ (quantx taken)

React, TypeScript, Redux
- Monaco Editor (https://microsoft.github.io/monaco-editor/)
- TradingView (https://www.tradingview.com/HTML5-stock-forex-bitcoin-charting-library/)