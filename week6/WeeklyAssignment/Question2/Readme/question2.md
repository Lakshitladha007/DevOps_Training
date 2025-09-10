Steps:

1. Build the docker image using the commands:
```bash
docker build -t dotnet_image .
```
![alt text](Screenshots/1.png) 

2. Now, create the container from the image that we build in step1
```bash
docker run --name=my_dotnet_container -p 8000:8080 dotnet_image:latest
```
![alt text](Screenshots/2.png)

3. Now go to your browser and search for "localhost:8000", you will be able to see you dotnet application running.

![alt text](Screenshots/3.png)