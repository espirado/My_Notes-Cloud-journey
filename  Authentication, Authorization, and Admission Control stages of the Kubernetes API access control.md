Each access request goes through the following access control stages:

Authentication
    Logs in a user.
Authorization
   Authorizes the API requests submitted by the authenticated user.
Admission Control
   Software modules that validate and/or modify user requests based.


   # Authentication 
   Kubernetes does not have an object called user, nor does it store usernames or other related details in its object store.

      Kubernetes supports two kinds of users: 
           Normal Users - They are managed outside of the Kubernetes cluster via independent services like User/Client Certificates, a file listing usernames/passwords, Google accounts, etc.

           Service Accounts - Service Accounts allow in-cluster processes to communicate with the API server to perform various operations.

   Kubernetes uses a series of authentication modules:


         X509 Client Certificates - To enable client certificate authentication, we need to reference a file containing one or more certificate authorities by passing the --client-ca-file=SOMEFILE option to the API server.

         Static Token File - We can pass a file containing pre-defined bearer tokens with the --token-auth-file=SOMEFILE option to the API server. 

         Bootstrap Tokens 

         Service Account Tokens -Automatically enabled authenticators that use signed bearer tokens to verify requests. These tokens get attached to Pods using the ServiceAccount Admission Controller, which allows in-cluster processes to talk to the API server.

         OpenID Connect Tokens - OpenID Connect helps us connect with OAuth2 providers, such as Azure Active Directory, Salesforce, and Google, to offload the authentication to external services.

         Webhook Token Authentication - With Webhook-based authentication, verification of bearer tokens can be offloaded to a remote service.

         Authenticating Proxy - Allows for the programming of additional authentication logic.

 # Authorization 
    Some of the API request attributes that are reviewed by Kubernetes include user, group, extra, Resource, Namespace, or API group, to name a few. Next, these attributes are evaluated against policies. If the evaluation is successful, then the request is allowed, otherwise it is denied

    Authorization modes 
        Node - Node authorization is a special-purpose authorization mode which specifically authorizes API requests made by kubelets.
    Attribute-Based Access Control (ABAC) - With the ABAC authorizer, Kubernetes grants access to API requests, which combine policies with attributes.

    Webhook - In Webhook mode, Kubernetes can request authorization decisions to be made by third-party services, which would return true for successful authorization, and false for failure.

    Role-Based Access Control (RBAC) - with RBAC we regulate the access to resources based on the Roles of individual users. In Kubernetes, multiple Roles can be attached to subjects like users, service accounts, etc.
         wo kinds of Roles: 
              Role
                  A Role grants access to resources within a specific Namespace.

              ClusterRole
                   A ClusterRole grants the same permissions as Role does, but its scope is cluster-wide.                    


          two kinds of RoleBindings:
              RoleBinding - It allows us to bind users to the same namespace as a Role. 
              ClusterRoleBinding - It allows us to grant access to resources at a cluster-level and to all Namespaces.

    Admission Control - are used to specify granular access control policies, which include allowing privileged containers, checking on resource quota, etc                        