# Testing openehr

## Setting up

### With docker-compose

There is a straightforward way to get openehr started.

```bash
mkdir ehrtest
cd ehrtest
# download the docker-compose.yml file to your local
wget https://github.com/ehrbase/ehrbase/raw/develop/docker-compose.yml
wget https://github.com/ehrbase/ehrbase/raw/develop/.env.ehrbase
docker-compose up

# OR: start both containers detached, without blocking the terminal
docker-compose up -d
```

Note that an .env.ehrbase is downloaded which is important, as it contains the credentials we will be using to signing into the openehr server.

https://ehrbase.readthedocs.io/en/latest/03_development/04_docker_images/01_ehrbase/02_use_image/index.html#run-ehrbase-db-with-docker-compose
