Kubernetes has a very rich object model, representing different persistent entities in the Kubernetes cluster. Those entities describe:
  what container we are running
   Nodes we are running 
   Resources we are consuming
   policies attached 


  For every object we declare intent (desired state of the object) in specs. Examples of Kubernetes objects are Pods, ReplicaSets, Deployments, Namespaces, etc.   apiVersion field is the first required field, and it specifies the API endpoint on the API server which we want to connect to. he second required field is kind, specifying the object type - in our case it is Deployment. The third required field metadata, holds the object's basic information, such as name, labels, namespace, etc. 

# Pods
  A pod is the smallest and simpliest kubernet  object. It is a unit of deployment.
  A Pod is a logical collection of one or more containers, which:

                  Are scheduled together on the same host with the Pod
                  Share the same network namespace, meaning that they share a single IP address originally assigned to the Pod
                  Have access to mount the same external storage (volumes).
    Pods are ephemeral in nature, and they do not have the capability to self-heal themselves.

 # Labels
  are key-value pairs attached to Kubernetes objects (e.g. Pods, ReplicaSets, Nodes, Namespaces, Persistent Volumes). Labels are used to organize and select a subset of objects, based on the requirements in place. 

     i.e app:frontend     app:backend      app:frontend   app:backend
         env:dev          env:dev          env:qa         env:qa

 we have two lables app and env,which can select and group apps app=frontend and env= qa

 # Label Selectors
Controllers use Label Selectors to select a subset of objects. 
        Equality-Based Selectors - Equality-Based Selectors allow filtering of objects based on Label keys and values. i.e env == dev or env != dev 
        Set-Based Selectors - Set-Based Selectors allow filtering of objects based on a set of values. i.e env in (qa,dev)

 # ReplicationControllers
    ensures a specified number of replicas of a Pod is running at any given time, by constantly comparing the actual state with the desired state of the managed application. The default recommended controller is the Deployment which configures a ReplicaSet controller to manage Pods' lifecycle

 # ReplicaSets I
     in part, the next-generation ReplicationController, as it implements the replication and self-healing aspects of the ReplicationController. 

 # Deployments 
    objects provide declarative updates to Pods and ReplicaSets. The DeploymentController is part of the master node's controller manager, and as a controller it also ensures that the current state always matches the desired state.

  A rolling update is triggered when we update specific properties of the Pod Template for a deployment.
  # Namespaces
  If multiple users and teams use the same Kubernetes cluster we can partition the cluster into virtual sub-clusters                




   # Service 
   Service is a method for exposing a network application that is running as one or more Pods in your cluster