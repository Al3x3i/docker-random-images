This is personal project to get more knowledge in using Docker with AWS.
After running the project you will see random images which can change after couple of seconds.

There are two different ways of getting the app up and running with Docker. To learn more about how these two differ, check out the docker curriculum.

There can be different ways to run the project with Docker. The project is uploaded to 
docker hub. Below are listed commands for the docker to run image with different circumstances

### Build script
```
docker build -t al3x3i/random-image .
```
### Run docker image

Below are listed various options how to run the docker using different ports. Use curl to verify the website works properly or not

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
docker_id=$(docker ps --filter ancestor=al3x3i/random-image -q)

ip_address=$(docker inspect $docker_id |  grep -Po '"IPAddress": \K"[^"]*"' -m1 | sed 's/"//g')
```
##### Remove double quotes from string = sed 's/"//g' 
#### OR
```
ip_address=$(docker inspect $docker_id | jq ".[].NetworkSettings.IPAddress")

curl $ip_address:$app_port
```
