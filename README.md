# CSL7510-VCC-assignment - 1

*Name : Srikhetra Sarthak Mohanty* <br/>
*Roll No : M21AIE260*

#Items in this assignment

## 1. Creating a Dockerfile
1. Importing ubuntu 20.4 image from docker repo
2. Updating all libraries using apt-get update and installing python 3.8
3. Copying all files and directory from current directory on host to app directory inside container
4. Setting working directory inside container to app
5. Installing all dependencies using pip and requirements.txt
6. Running the app file through python entrypoint

## 2. Building the docker image
```sh
sudo docker build -t "question2" .
```

## 3. Running the container and mapping to another port
```sh
sudo docker run -p 7000:5000 -t "question2"
```

Note - Using sudo is not compulsory. Incoming port can be anything. 

### The app will be loaded and can be viewed at the external ip address at port 7000

## About the webapp

The webapp is a simple example where the current date time & day of the week gets printed dynamically. It has been created using flask and simple python datetime libraries. Please refer the code for detailed comments

## Author
Name - Srikhetra Sarthak Mohanty <br/>
Roll No - M21AIE260 

