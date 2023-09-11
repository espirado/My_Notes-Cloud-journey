What is Gitops ?
 is a set of best practices where the entire code delivery is controlled by Git. This includes infrastucture and application definition code. 

 Key principles in GitOps
  - the entire system is declarative declared(infra & application code)
  - Desired system state is GIT versioned 
  - Changes approved are automated and applied to the system 
  - software agents ensure correctness and alert on divergence 

GitOps use cases 
 - Configuration management and drift detection 
 - Continous deployment of application
 - Continous deployment of infrastucture 
 - Continous deployment of cluster resources 
 - Multicluster deployment 
 
 Argo CD is agnostic on the type of manifests you can use. It supports plain Kubernetes manifests, Helm charts, Kustomize definitions, and other templating mechanisms.
 

Argo CD (GitOps controller)
Argo Rollouts (Progressive Delivery controller)
Argo Workflows (Workflow engine for Kubernetes)
Argo Events (Event handling for Kubernetes)

Managing secretes in GitOps 
 - You can use any secret manager tool to store secrets 
 - Built in kubernets secret manager - using confif maps to store secrets in plain text and mount them on your cluster 