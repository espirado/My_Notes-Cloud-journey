 Ingress API resource, which represents another layer of abstraction, deployed in front of the Service API resources, offering a unified method of managing access to our applications from the external world.

 With Services, routing rules are associated with a given Service. They exist for as long as the Service exists, and there are many rules because there are many Services in the cluster. If we can somehow decouple the routing rules from the application and centralize the rules management, we can then update our application without worrying about its external access. This can be done using the Ingress resource.

 To allow the inbound connection to reach the cluster Services, Ingress configures a Layer 7 HTTP/HTTPS load balancer for Services and provides the following:

TLS (Transport Layer Security)
Name-based virtual hosting 
Fanout routing
Loadbalancing
Custom rules.

The ingress is fulfilled by an Ingress Controller, which is a reverse proxy responsible for traffic routing based on rules defined in the Ingress resource. 

An Ingress Controller is an application watching the Master Node's API server for changes in the Ingress resources and updates the Layer 7 Load Balancer accordingly.

Horizontal Pod Autoscaler (HPA)
HPA is an algorithm-based controller API resource which automatically adjusts the number of replicas in a ReplicaSet, Deployment or Replication Controller based on CPU utilization.
Vertical Pod Autoscaler (VPA)
VPA automatically sets Container resource requirements (CPU and memory) in a Pod and dynamically adjusts them in runtime, based on historical utilization data, current resource availability and real-time events.
Cluster Autoscaler
Cluster Autoscaler automatically re-sizes the Kubernetes cluster when there are insufficient resources available for new Pods expecting to be scheduled or when there are underutilized nodes in the cluster.

A Job creates one or more Pods to perform a given task. The Job object takes the responsibility of Pod failures. It makes sure that the given task is completed successfully. Once the task is complete, all the Pods have terminated automatically. Job configuration options include:

parallelism - to set the number of pods allowed to run in parallel;
completions - to set the number of expected completions;
activeDeadlineSeconds - to set the duration of the Job;
backoffLimit - to set the number of retries before Job is marked as failed;
ttlSecondsAfterFinished - to delay the clean up of the finished Jobs.


with CronJobs, where a new Job object is created about once per each execution cycle. The CronJob configuration options include:

startingDeadlineSeconds - to set the deadline to start a Job if scheduled time was missed;
concurrencyPolicy - to allow or forbid concurrent Jobs or to replace old Jobs with new ones. 

In cases when we need to collect monitoring data from all nodes, or to run a storage daemon on all nodes, then we need a specific type of Pod running on all nodes at all times. A DaemonSet is the object that allows us to do just that. It is a critical controller API resource for multi-node Kubernetes clusters. The kube-proxy agent running as a Pod on every single node in the cluster is managed by a DaemonSet.  


The StatefulSet controller is used for stateful applications which require a unique identity, such as name, network identifications, or strict ordering. For example, MySQL cluster, etcd cluster.

The StatefulSet controller provides identity and guaranteed ordering of deployment and scaling to Pods. Similar to Deployments, StatefulSets use ReplicaSets as intermediary Pod controllers and support rolling updates and rollbacks.


With Kubernetes Cluster Federation we can manage multiple Kubernetes clusters from a single control plane. We can sync resources across the federated clusters and have cross-cluster discovery. This allows us to perform Deployments across regions, access them using a global DNS record, and achieve High Availability. 

Although still an Alpha feature, the Federation is very useful when we want to build a hybrid solution, in which we can have one cluster running inside our private datacenter and another one in the public cloud, allowing us to avoid provider lock-in. We can also assign weights for each cluster in the Federation, to distribute the load based on custom rules. 

At times we need to define specific privileges and access control settings for Pods and Containers. Security Contexts allow us to set Discretionary Access Control for object access permissions, privileged running, capabilities, security labels, etc. However, their effect is limited to the individual Pods and Containers where such context configuration settings are incorporated in the spec section. 

In order to apply security settings to multiple Pods and Containers cluster-wide, we can define Pod Security Policies. They allow more fine-grained security settings to control the usage of the host namespace, host networking and ports, file system groups, usage of volume types, enforce Container user and group ID, root privilege escalation, etc. 

Kubernetes was designed to allow all Pods to communicate freely, without restrictions, with all other Pods in cluster Namespaces. In time it became clear that it was not an ideal design, and mechanisms needed to be put in place in order to restrict communication between certain Pods and applications in the cluster Namespace. Network Policies are sets of rules which define how Pods are allowed to talk to other Pods and resources inside and outside the cluster. Pods not covered by any Network Policy will continue to receive unrestricted traffic from any endpoint. 

Network Policies are very similar to typical Firewalls. They are designed to protect mostly assets located inside the Firewall but can restrict outgoing traffic as well based on sets of rules and policies. 

The Network Policy API resource specifies podSelectors, Ingress and/or Egress policyTypes, and rules based on source and destination ipBlocks and ports. Very simplistic default allow or default deny policies can be defined as well. As a good practice, it is recommended to define a default deny policy to block all traffic to and from the Namespace, and then define sets of rules for specific traffic to be allowed in and out of the Namespace. 

Let's keep in mind that not all the networking solutions available for Kubernetes support Network Policies. Review the Pod-to-Pod Communication section from the Kubernetes Architecture chapter if needed. By default, Network Policies are namespaced API resources, but certain network plugins provide additional features so that Network Policies can be applied cluster-wide. 

In Kubernetes, we have to collect resource usage data by Pods, Services, nodes, etc., to understand the overall resource consumption and to make decisions for scaling a given application. Two popular Kubernetes monitoring solutions are the Kubernetes Metrics Server and Prometheus. 

Metrics Server 
Metrics Server is a cluster-wide aggregator of resource usage data - a relatively new feature in Kubernetes. 
Prometheus
Prometheus, now part of CNCF (Cloud Native Computing Foundation), can also be used to scrape the resource usage from different Kubernetes components and objects. Using its client libraries, we can also instrument the code of our application. 
Another important aspect for troubleshooting and debugging is Logging, in which we collect the logs from different components of a given system. In Kubernetes, we can collect logs from different cluster components, objects, nodes, etc. Unfortunately, however, Kubernetes does not provide cluster-wide logging by default, therefore third party tools are required to centralize and aggregate cluster logs. A popular method to collect logs is using Elasticsearch together with fluentd with custom configuration as an agent on the nodes. fluentd is an open source data collector, which is also part of CNCF. 

To deploy a complex application, we use a large number of Kubernetes manifests to define API resources such as Deployments, Services, PersistentVolumes, PersistentVolumeClaims, Ingress, or ServiceAccounts. It can become counter productive to deploy them one by one. We can bundle all those manifests after templatizing them into a well-defined format, along with other metadata. Such a bundle is referred to as Chart. These Charts can then be served via repositories, such as those that we have for rpm and deb packages. 

Helm is a package manager (analogous to yum and apt for Linux) for Kubernetes, which can install/update/delete those Charts in the Kubernetes cluster.

Helm is a CLI client that may run side-by-side with kubectl on our workstation, that also uses kubeconfig to securely communicate with the Kubernetes API server. 

The helm client queries the Chart repositories for Charts based in search parameters, downloads a desired Chart, and then it requests the API server to deploy in the cluster the resources defined in the Chart. Charts submitted for Kubernetes are available here. 

Service Mesh is a third party solution to the Kubernetes native application connectivity and exposure achieved with Services paired with Ingress Controllers. Service Mesh tools are gaining popularity especially with larger organizations managing larger, dynamic Kubernetes clusters. These third party solutions introduce features such as service discovery, multi-cloud routing, and traffic telemetry. 

A Service Mesh is an implementation that relies on a proxy component part of the Data Plane, which is then managed through a Control Plane. The Control Plane runs agents responsible for the service discovery, telemetry, load balancing, network policy, and gateway. The Data Plane proxy component is typically injected into Pods, and it is responsible for handling all Pod-to-Pod communication, while maintaining a constant communication with the Control Plane of the Service Mesh.


