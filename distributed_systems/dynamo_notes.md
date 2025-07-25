Based on gossip based distributed failure dection and membership protocol 

Gossip Protocol Explained
  - The typical problems in a distributed system are the following [1], [11]:

maintaining the system state (liveness of nodes)
communication between nodes
The potential solutions to these problems are as follows [1]:

centralized state management service
peer-to-peer state management service

Centralized State Management Service
A centralized state management service such as Apache Zookeeper can be configured as the service discovery to keep track of the state of every node in the system. Although this approach provides a strong consistency guarantee, the primary drawbacks are the state management service becomes a single point of failure and runs into scalability problems for a large distributed system

Peer-To-Peer State Management Service
The peer-to-peer state management approach is inclined towards high availability and eventual consistency. The gossip protocol algorithms can be used to implement peer-to-peer state management services with high scalability and improved resilience [1].

The gossip protocol is also known as the epidemic protocol because the transmission of the messages is similar to the way how epidemics spread. The concept of communication in gossip protocol is analogous to the spread of rumors among the office staff or the dissemination of information on a social media website



point-to-point broadcast
The producer sends a message directly to the consumers in a point-to-point broadcast. The retry mechanism on the producer and deduplication mechanism on the consumers makes the point-to-point broadcast reliable.
eager reliable broadcast
Every node re-broadcasts the messages to every other node via reliable network links. This approach provides improved fault tolerance because messages are not lost when both the producer and the consumer fail simultaneously
gossip protocol

The gossip protocol is a decentralized peer-to-peer communication technique to transmit messages in an enormous distributed system [1], [8]. The key concept of gossip protocol is that every node periodically sends out a message to a subset of other random nodes [8], [2]. The entire system will receive the particular message eventually with a high probability [11], [3]. In layman’s terms, the gossip protocol is a technique for nodes to build a global map through limited local interactions

practical Byzantine Fault Tolerance(pBFT)

Byzantine Fault Tolerance(BFT) is the feature of a distributed network to reach consensus(agreement on the same value) even when some of the nodes in the network fail to respond or respond with incorrect information. The objective of a BFT mechanism is to safeguard against the system failures by employing collective decision making(both – correct and faulty nodes) which aims to reduce to influence of the faulty nodes

pBFT tries to provide a practical Byzantine state machine replication that can work even when malicious nodes are operating in the system. Nodes in a pBFT enabled distributed system are sequentially ordered with one node being the primary(or the leader node) and others referred to as secondary(or the backup nodes). Note here that any eligible node in the system can become the primary by transitioning from secondary to primary(typically, in the case of a primary node failure). The goal is that all honest nodes help in reaching a consensus regarding the state of the system using the majority rule. A practical Byzantine Fault Tolerant system can function on the condition that the maximum number of malicious nodes must not be greater than or equal to one-third of all the nodes in the system. As the number of nodes increase, the system becomes more secure. pBFT consensus rounds are broken into 4 phases(refer with the image below):

The client sends a request to the primary(leader) node.
The primary(leader) node broadcasts the request to the all the secondary(backup) nodes.
The nodes(primary and secondaries) perform the service requested and then send back a reply to the client.
The request is served successfully when the client receives ‘m+1’ replies from different nodes in the network with the same result, where m is the maximum number of faulty nodes allowed.

Dynamo differs from the aforementioned decentralized storage
systems in terms of its target requirements. First, Dynamo is
targeted mainly at applications that need an “always writeable”
data store where no updates are rejected due to failures or
concurrent writes. This is a crucial requirement for many Amazon
applications. Second, as noted earlier, Dynamo is built for an
infrastructure within a single administrative domain where all
nodes are assumed to be trusted. Third, applications that use
Dynamo do not require support for hierarchical namespaces (a
norm in many file systems) or complex relational schema
(supported by traditional databases). Fourth, Dynamo is built for
latency sensitive applications that require at least 99.9% of read
and write operations to be performed within a few hundred
milliseconds

Problem Technique Advantage
Partitioning Consistent Hashing Incremental
Scalability
High Availability
for writes
Vector clocks with
reconciliation during
reads
Version size is
decoupled from
update rates.
Handling temporary
failures
Sloppy Quorum and
hinted handoff
Provides high
availability and
durability guarantee
when some of the
replicas are not
available.

permanent failures
Anti-entropy using
Merkle trees
Synchronizes
divergent replicas in
the background.
Membership and
failure detection
Gossip-based
membership protocol
and failure detection.
Preserves symmetry
and avoids having a
centralized registry
for storing
membership and
node liveness
information. 


Vector Clocks in Distributed Systems
used to track the partial ordering of events and maintain causality across different nodes. Unlike traditional timestamps, vector clocks provide a way to determine the order of events even in the absence of a global clock, making them crucial for conflict detection and resolution.
The key idea behind vector clocks is that they allow a system to determine whether one event happened before another, whether two events are concurrent, or whether they are causally related.
This is particularly useful in distributed systems where a global clock is not available, and processes need to coordinate actions without central control.