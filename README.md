# Build script
docker build -t al3x3i/random-image .

# Info Docker ip can be 0.0.0.0 OR 172.17.0.2
# Or either inspect:
# docker inspect CONTAINER ID | grep IPAddress

# I
docker run al3x3i/random-image
curl 0.0.0.0:3333

# II
docker run -p 7000:3333 al3x3i/random-image
curl 0.0.0.0:7000

# III
docker run -p 8888:7700 --env "DOCKER_PORT=7700" al3x3i/random-image
curl 172.17.0.2:8888

# IV
docker run --env "DOCKER_PORT=8800" --expose=8800 al3x3i/random-image
curl 172.17.0.2:8888


