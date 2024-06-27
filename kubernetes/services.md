 objects used to abstract the communication between cluster internal microservices, or with the external world.  A Service offers a single DNS entry for a containerized application managed by the Kubernetes cluster, regardless of the number of replicas, by providing a common load balancing access point to a set of pods logically grouped and managed by a controller such as a Deployment, ReplicaSet, or DaemonSet. 

 # Connecting Users or Applications to Pods
   A logical set of a Pod's IP address, along with the targetPort is referred to as a Service endpoint. 

   kube-proxy 
     that watches the API server on the master node for the addition, updates, and removal of Services and endpoints

     is responsible for implementing the Service configuration on behalf of an administrator or developer, in order to enable traffic routing to an exposed application running in Pods.

     Service Discovery - 
        Environment Variables - the kubelet daemon running on that node adds a set of environment variables in the Pod for all active Services.


        DNS - which creates a DNS record for each Service and its format is my-svc.my-namespace.svc.cluster.local. Services within the same Namespace find other Services just by their names. If we add a Service redis-master in my-ns Namespace, all Pods in the same my-ns Namespace lookup the Service just by its name, redis-master.

     ServiceType - Access scope is decided by ServiceType property, defined when creating the Service. 

     A Service receives a Virtual IP address, known as its ClusterIP. This Virtual IP address is used for communicating with the Service and is accessible only from within the cluster

     The NodePort ServiceType is useful when we want to make our Services accessible from the external world. The end-user connects to any worker node on the specified high-port, which proxies the request internally to the ClusterIP of the Service, then the request is forwarded to the applications running inside the cluster   


     ServiceType: LoadBalancer 
                 ServiceType will only work if the underlying infrastructure supports the automatic creation of Load Balancers and have the respective support in Kubernetes, as is the case with the Google Cloud Platform and AWS


     ServiceType: ExternalIP
                        


      
Telepresence is an open source tool that lets developers code and test microservices locally against a remote Kubernetes cluster. Telepresence facilitates more efficient development workflows while relieving the need to worry about other service dependencies                  