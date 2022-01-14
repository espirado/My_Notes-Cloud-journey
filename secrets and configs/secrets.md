While deploying an application, we may need to pass such runtime parameters like configuration details, permissions, passwords, keys, certificates, or tokens.

Let's assume we need to deploy ten different applications for our customers, and for each customer, we need to display the name of the company in the UI. Then, instead of creating ten different Docker images for each customer, we may just use the same template image and pass customers' names as runtime parameters. In such cases, we can use the ConfigMap API resource.

ConfigMaps allow us to decouple the configuration details from the container image. Using ConfigMaps, we pass configuration data as key-value pairs, which are consumed by Pods or any other system components and controllers, in the form of environment variables, sets of commands and arguments, or volumes. We can create ConfigMaps from literal values, from configuration files, from one or more files or directories. 

A ConfigMap can be created with the kubectl create command, and we can display its details using the kubectl get command.

Create the ConfigMap

$ kubectl create configmap my-config --from-literal=key1=value1 --from-literal=key2=value2


Display the ConfigMap Details for my-config


$ kubectl get configmaps my-config -o yaml


First, we need to create a file permission-reset.properties with the following configuration data:

the Secret object can help by allowing us to encode the sensitive information before sharing it. With Secrets, we can share sensitive information like passwords, tokens, or keys in the form of key-value pairs, similar to ConfigMaps; thus, we can control how the information in a Secret is used, reducing the risk for accidental exposures. In Deployments or other resources, the Secret object is referenced, without exposing its content.


Secrets are consumed by Containers in Pods as mounted data volumes, or as environment variables, and are referenced in their entirety or specific key-values.

