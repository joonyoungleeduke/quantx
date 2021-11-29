# QuantX



## Notice

**<u>If setup fails with the scripts...</u>**

- Check if it is a 'syntax error' with bash scripts. Line ending differences between Linux & Windows 10/11 have been found on our local dev machines to cause errors. One way to solve this is to manually run the commands (if they are simple one-line docker commands) or copy + paste the code in the bash script, delete the corresponding script, make a new script in the same location with the same name, and copy + paste the code back in. 
  - <u>One place where this may happen prevalently is in the server repository that uses init.sh for a cron job to ingest stock data, make sure to check that repository's README.md for more information.</u>

* If it is not a 'syntax error,' then try reading through all the repository READMEs to see if your concerns are addressed. 

## Structure 

* Consists of three linked sub-repositories.
* Each sub-linked repository and the top-level repository contain scripts relating to its Dockerfile for convenience of individual deployment. Typically the top-level repository's scripts are the ones most currently maintained, so there is no guarantee all sub-linked repository scripts will work. 
* <u>Top-level repository may not contain the most up-to-date information. Go to 'main' in each sub-repository for the most up to date code.</u>
* See the README.md within each sub-repository for more information. 

### DB 

* Uses TimescaleDB (https://www.timescale.com/)

### Server

* Uses FastAPI (https://fastapi.tiangolo.com/)
* Depends on DB
* <u>To see detailed endpoint information run the server & db together with defaults and go to (server URL)/docs, where server URL is typically localhost:80</u>

### Client

* Typical TypeScript with React/Redux 

### 

## Development

* Have docker daemon running 
* Use ./scripts/setup_server.sh or run the command inside there manually to set up server / db. Run the client separately for faster build time & reliable hot reloading.  
* To run the client into client/app and run 'yarn start' after 'yarn install'



## Deployment

* Each sub-repository is distinct so they can be deployed separately
* A sample deployment would be: 
  * Client on Netlify to take advantage of an edge-based CDN. Only client/app/src/constants.ts needs a new baseURL specified for the API. 
  * server on AWS using Docker with or without the db on the same machine (since they also have distinct Dockerfiles). 
    * db only requires editing of environment variables in db/Dockerfile 
    * server's required environment variables can be seen in app/config.py. These can be set in the environment the server is running in, otherwise it will default to defaults, which are inherently insecure. Defaults only exist for the convenience of someone to pull the git repositories and simply run locally. 
