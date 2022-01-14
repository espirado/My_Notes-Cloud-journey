what is gitops - running operations via git with goal of setting up cd of cloud native applications 

    - iac - writing infrastucture as code 
    - Git - version control system
    - ci/cd - automated and continpus process to deliver software,configurations
    - conversions platforms - converge desired state to current state



- releases strategies 
         - canary 
         - blue green 
         - rolling update
- infrastucture rollouts 
          - ingress controlers
          - namespaces
          - rbac policies
          - network policies
          - crds
- diasater recovery 
        - recover from failure 

- sync secrets

- Drift detections 
             - reconcile 
             - Notify
- Deploy to multiple kubernetes clusters
- securely handoff deployments to dev
            - no cluster access to devs
            - multi tenancy 
            - separtion of concerns

- Autoupdate kubernetes yaml on new image on registry



Principles of Gitops
  - Write 100% declaritive configurations
      - helm 
      - kustomize
  - Store desired state in git 
  - Aplly approved changes automatically 
  - Check and correct with a software agent

  - pull vs pull model
      - pull - secure 
             - flexible 
             - scalble 
             - two way sync

       - push - simple (single reconciler )
              - sequence,dependencies management is easir
              - bandwidtch/requests  optimized            
Fluxcd  vs argocd
jenkinsx
  

flux fleet repo - contains intfrastucture confiurations

Deployment repo - contains deployment repo 

main repo contains code for continous intergrations

cluster wide components - i.e nginx ingress 

flagger - does continous delivery aspects i.e set up canary deployment or blue green deployments

flux set canary to manage releases 


With GitOps, the use of software agents can alert on any divergence between Git with what's running in a cluster, and if there's a difference, Kubernetes reconcilers automatically update or rollback the cluster depending on the case. With Git at the center of your delivery pipelines, developers use familiar tools to make pull requests to accelerate and simplify both application deployments and operations tasks to Kubernetes.

Principles of GitOps

  #1. The entire system described declaratively.
     - Declarative means that configuration is guaranteed by a set of facts instead of by a set of instructions. With your application’s declarations versioned in Git, you have a single source of truth. Your apps can then be easily deployed and rolled back to and from Kubernetes. And even more importantly, when disaster strikes, your cluster’s infrastructure can also be dependably and quickly reproduced.
  
  #2. The canonical desired system state versioned in Git.
     - This trivializes rollbacks; where you can use a `Git revert` to go back to your previous application state. With Git’s excellent security guarantees, you can also use your SSH key to sign commits that enforce strong security guarantees about the authorship and provenance of your code.

  #3. Approved changes that can be automatically applied to the system.  
      - Once you have the declared state kept in Git, the next step is to allow any changes to that state to be automatically applied to your system. What's significant about this is that you don't need cluster credentials to make a change to your system. With GitOps, there is a segregated environment of which the state definition lives outside. This allows you to separate what you do and how you're going to do it.

  #4. Software agents to ensure correctness and alert on divergence.
      - Once the state of your system is declared and kept under version control, software agents can inform you whenever reality doesn’t match your expectations.  The use of agents also ensures that your entire system is self-healing. And by self-healing, we don’t just mean when nodes or pods fail—those are handled by Kubernetes—but in a broader sense, like in the case of human error.  In this case, software agents act as the feedback and control loop for your operations.
      

  Continuous Delivery and GitOps
  
             