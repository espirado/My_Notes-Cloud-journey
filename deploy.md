Let's learn how to deploy an nginx webserver using the nginx Docker container image. 

we will be using webUI for kubernetes


Start Minikube and verify that it is running
Run this command first:

$ minikube start

Then verify Minikube status:

$ minikube status

Start the Minikube Dashboard
To access the Kubernetes Web IU, we need to run the following command:

 $ minikube dashboard

 From the dashboard, click on the "+" sign at the top right corner of the Dashboard

 Deploy a webserver using the nginx image
From the dashboard, click on the "+" sign at the top right corner of the Dashboard. That will open the create interface as seen below:

 

Create a New Application - Interface

Create a New Application - Interface

 

From there, we can create an application using a valid YAML/JSON configuration data, from a file, or manually


List the Deployments
We can list all the Deployments in the default Namespace using the kubectl get deployments command:

$ kubectl get deployments

List the ReplicaSets
We can list all the ReplicaSets in the default Namespace using the kubectl get replicasets command:

List the Pods
We can list all the Pods in the default namespace using the kubectl get pods command:

$ kubectl get pods

Exploring Labels and Selectors I


Look at a Pod's Details
We can look at an object's details using kubectl describe command

kubectl describe pod $podName


List the Pods, along with their attached Labels
With the -L option to the kubectl get pods command, we add extra columns in the output to list Pods with their attached Label keys and their values



Deploying an Application Using the CLI 

Create a deployment yaml file

Using kubectl, we will create the Deployment from the YAML configuration file. Using the -f option with the kubectl create command, we can pass a YAML file as an object's specification, or a URL to a configuration file from the web. In the following example, we are creating a webserver Deployment:

$ kubectl create -f

This will also create a ReplicaSet and Pods, as defined in the YAML configuration file.

Exposing an Application

With ServiceTypes we can define the access method for a Service. For a NodePort ServiceType, Kubernetes opens up a static port on all the worker nodes. If we connect to that port from any node, we are proxied to the ClusterIP of the Service. Next, let's use the NodePort ServiceType while creating a Service.

we create an svc file 


Using kubectl, create the Service:

$ kubectl create -f 


A more direct method of creating a Service is by exposing the previously created Deployment (this method requires an existing Deployment).

Expose a Deployment with the kubectl expose command:

$ kubectl expose deployment webserver --name=web-service --type=NodePort

List the Services:

$ kubectl get services

kubectl describe service web-service


Accessing an Application

Our application is running on the Minikube VM node. To access the application from our workstation, let's first get the IP address of the Minikube VM:

$ minikube ip


We could also run the following minikube command which displays the application in our browser:

$ minikube service web-service


Liveness and Readiness Probes
While containerized applications are scheduled to run in pods on nodes across our cluster, at times the applications may become unresponsive or may be delayed during startup. Implementing Liveness and Readiness Probes allows the kubelet to control the health of the application running inside a Pod's container and force a container restart of an unresponsive application. When defining both Readiness and Liveness Probes, it is recommended to allow enough time for the Readiness Probe to possibly fail a few times before a pass, and only then check the Liveness Probe. If Readiness and Liveness Probes overlap there may be a risk that the container never reaches ready state, being stuck in an infinite re-create - fail loop.

Liveness Probes can be set by defining:

Liveness command
Liveness HTTP request
TCP Liveness probe. 
