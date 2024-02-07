# Define the Docker image name
IMAGE_NAME := subash/ran:latest

# Targets without dependencies
.PHONY: deploy undeploy build

# Target: deploy
deploy:
	kubectl apply -f crd/crd.yaml
        
	kubectl create ns ran-operator

	kubectl apply -f deploy/rbac/
	
	kubectl apply -f deploy/deployment.yaml

# Target: undeploy
undeploy:
	kubectl delete -f deploy/deployment.yaml

	kubectl delete -f deploy/rbac/
	
	kubectl delete -f crd/crd.yaml

	kubectl delete ns ran-operator

# Target: build
build:
	# Build Docker image using the Dockerfile in the app/ directory
	docker build -t $(IMAGE_NAME) .

