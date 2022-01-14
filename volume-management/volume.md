Kubernetes uses Volumes of several types and a few other forms of storage resources for container data management.

As we know, containers running in Pods are ephemeral in nature. All data stored inside a container is deleted if the container crashes. However, the kubelet will restart it with a clean slate, which means that it will not have any of the old data.

A directory which is mounted inside a Pod is backed by the underlying Volume Type.

emptyDir
An empty Volume is created for the Pod as soon as it is scheduled on the worker node. The Volume's life is tightly coupled with the Pod. If the Pod is terminated, the content of emptyDir is deleted forever.  
hostPath
With the hostPath Volume Type, we can share a directory between the host and the Pod. If the Pod is terminated, the content of the Volume is still available on the host.
gcePersistentDisk
With the gcePersistentDisk Volume Type, we can mount a Google Compute Engine (GCE) persistent disk into a Pod.
awsElasticBlockStore
With the awsElasticBlockStore Volume Type, we can mount an AWS EBS Volume into a Pod. 
azureDisk
With azureDisk we can mount a Microsoft Azure Data Disk into a Pod.
azureFile
With azureFile we can mount a Microsoft Azure File Volume into a Pod.
cephfs
With cephfs, an existing CephFS volume can be mounted into a Pod. When a Pod terminates, the volume is unmounted and the contents of the volume are preserved.
nfs
With nfs, we can mount an NFS share into a Pod.
iscsi
With iscsi, we can mount an iSCSI share into a Pod.
secret
With the secret Volume Type, we can pass sensitive information, such as passwords, to Pods.
configMap
With configMap objects, we can provide configuration data, or shell commands and arguments into a Pod.
persistentVolumeClaim
We can attach a PersistentVolume to a Pod using a persistentVolumeClaim. 


Kubernetes resolves this problem with the PersistentVolume (PV) subsystem, which provides APIs for users and administrators to manage and consume persistent storage.

A Persistent Volume is a storage abstraction backed by several storage technologies, which could be local to the host where the Pod is deployed with its application container(s), network attached storage, cloud storage, or a distributed storage solution.


PersistentVolumes can be dynamically provisioned based on the StorageClass resource. A StorageClass contains pre-defined provisioners and parameters to create a PersistentVolume. Using PersistentVolumeClaims, a user sends the request for dynamic PV creation, which gets wired to the StorageClass resource


A PersistentVolumeClaim (PVC) is a request for storage by a user. Users request for PersistentVolume resources based on type, access mode, and size. There are three access modes: ReadWriteOnce (read-write by a single node), ReadOnlyMany (read-only by many nodes), and ReadWriteMany (read-write by many nodes). Once a suitable PersistentVolume is found, it is bound to a PersistentVolumeClaim. 

 Storage vendors and community members from different orchestrators started working together to standardize the Volume interface; a volume plugin built using a standardized Container Storage Interface (CSI) designed to work on different container orchestrators

 