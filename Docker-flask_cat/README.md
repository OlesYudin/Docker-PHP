# FLASK APP

Python application using framework FLASK that generate random cats when you refresh useragent

## Setup and run Application:

- `git clone` repository_name
- `cd /Docker-app/Docker-flask_cat`
- `docker build -t cat:v1 .` build application
- `docker run -d -p 80:5000 --name=cat cat:v1` run application using port **80**
- `ip -a` Find Docker IP address (172.17.X.X)
- Open on useragent`http://172.17.X.X`
