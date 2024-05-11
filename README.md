## Running application in docker containers:
#### Using Docker CLI
```
docker network ls
docker network create --driver bridge micro_network (skip if already created)
docker build -t product-srv .
docker run -p 5002:5002 --detach --name product-service --net=micro_network product-srv
```

# Minikube hosting
```
### Start Minikube:
minikube start --driver=docker

### Set Up Docker Environment for Minikube:
minikube docker-env | Invoke-Expression
& minikube -p minikube docker-env --shell powershell | Invoke-Expression

### Build Docker Image
docker build -t product-app .

### Update Kubernetes Manifests:- set image field in frontend-deployment.yaml
image: product-app

### Tag your Docker image:- docker tag <local-image-name> <username>/<image-name>:<tag>
docker tag product-app vksan9/product-app:latest

### Log in to Docker Hub (or the registry):
docker login

### Push the Docker:- image:docker push <username>/<image-name>:<tag>
docker push vksan9/product-app:latest

### Apply Kubernetes Manifests:- 
kubectl apply -f product-deployment.yaml
kubectl apply -f product-service.yaml

### Access Your Application:- Access your application using the IP address and NodePort
### specified in the service manifest e.g http://<minikube-ip>:30000
minikube ip
minikube service product-app --url


### Check Pod Status
kubectl get pods

