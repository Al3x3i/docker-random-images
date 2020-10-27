This is a personal project to get more knowledge in using Docker with AWS. \
After running the project you will see random images that can change after a couple of seconds.

```Dockerrun.aws.json``` - Docker file for AWS \
```build-docker-image.sh```	- Build Dockerfile command \
```install-dependencies.sh```	- Install python3 dependencies \
```start.sh``` - Run web app

There are different ways to run the project with Docker. The project is uploaded to the docker hub. Below are listed commands to run docker image with different circumstances

Docker has a flask light weigh application that displays random images from https://source.unsplash.com/random. The index.html is stored in the template folder.

### Build script
```
docker build -t al3x3i/random-image .
```
### Run docker image

Below are listed various options on how to run the docker using different ports. Use curl to verify the website works properly or not

#### I
```
docker run al3x3i/random-image
app_port=3333
```

#### II
```
docker run -p 7000:3333 al3x3i/random-image
app_port=7000
```

#### III
```
docker run -p 8888:7700 --env "DOCKER_PORT=7700" al3x3i/random-image
app_port=8888
```

#### IV
```
docker run --env "DOCKER_PORT=8800" --expose=8800 al3x3i/random-image
app_port=8800
```
#### Curl
```
ip_address=0.0.0.0
curl $ip_address:$app_port
```

##### If for some reason IP address does not work you can inspect docker image IP. Below commands

```
docker_id=$(docker ps --filter ancestor=al3x3i/random-image -q)
ip_address=$(docker inspect $docker_id |  grep -Po '"IPAddress": \K"[^"]*"' -m1 | sed 's/"//g')
curl $ip_address:$app_port
```
OR
```
docker_id=$(docker ps --filter ancestor=al3x3i/random-image -q)
ip_address=$(docker inspect $docker_id | jq ".[].NetworkSettings.IPAddress")
curl $ip_address:$app_port
```
##### Note:
Remove double quotes from string = ```sed 's/"//g'```
