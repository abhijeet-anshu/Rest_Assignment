A web application which loads a CSV on startup and then exposes an API to explore the file.

The project has a single django app(api) which uses tastypie to implement rest
The App has following file structure
api
├── admin.py
├── admin.pyc
├── apps.py
├── __init__.py
├── models.py
├── models.pyc
├── resources.py
├── tests.py
└── views.py

The App has a model named Data having 2 attributes key and value. 

To map to a resource, resources.py is created that uses tastypie to map Data model to a resource.

```
Data Load
```

1. The CSV to be input has to be named Corpus.csv and placed in the project directory before docker build
2. On startup, docker calls start.sh to run
3. The start.sh applies migration if any, loads data and then starts the server on 8000 port.


```
Build instructions
```

Enter a docker-machine container as below:

1. Create a docker container
    docker-machine create development --driver virtualbox --virtualbox-disk-size "5000" --virtualbox-cpu-count 2 --virtualbox-memory "4096"
2. docker-machine start development
3. docker-machine env development
4. eval "$(docker-machine env development)"

Add docker image to container as below:
1. cd <project root directory>
2. docker build -t abhijeetbaranwal/goibibo-app-rest_assignment .

Add port forwarding rule
1. VBoxManage controlvm "development" natpf1 "tcp-port8000,tcp,,8000,,8000";

Start the image by

1. docker run -it -p 8000:8000 abhijeetbaranwal/goibibo-app-rest_assignment

