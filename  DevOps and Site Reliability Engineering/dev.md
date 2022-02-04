Implementing SLOs
Service level objectives (SLOs) specify a target level for the reliability of your service.

In order to adopt an error budget-based approach to Site Reliability Engineering, you need to reach a state where the following hold true:

There are SLOs that all stakeholders in the organization have approved as being fit for the product.
The people responsible for ensuring that the service meets its SLO have agreed that it is possible to meet this SLO under normal circumstances.
The organization has committed to using the error budget for decision making and prioritizing. This commitment is formalized in an error budget policy.
There is a process in place for refining the SLO.

SLI is an indicator of the level of service that you are providing

SLI specification

The assessment of service outcome that you think matters to users, independent of how it is measured.

SLI implementation

The SLI specification and a way to measure it.

The easiest way to get started with setting SLIs is to abstract your system into a few common types of components.  
        Request-driven

The user creates some type of event and expects a response. For example, this could be an HTTP service where the user interacts with a browser or an API for a mobile application.
      Pipeline

A system that takes records as input, mutates them, and places the output somewhere else. This might be a simple process that runs on a single instance in real time, or a multistage batch process that takes many hours.


Storage

A system that accepts data (e.g., bytes, records, files, videos) and makes it available to be retrieved at a later date.

We have a couple potential approaches to measure correctness:

Inject data with known outputs into the system, and count the proportion of times that the output matches our expectations.
Use a method to calculate correct output based on input that is distinct from our pipeline itself (and likely more expensive, and therefore not suitable for our pipeline). Use this to sample input/output pairs, and count the proportion of correct output records. This methodology assumes that creating such a system is both possible and practical.



# Databases
ACID properties

Set of properties that guarantee data integrity of DB transactions

Atomicity: Each transaction is atomic (succeeds or fails completely)
Consistency: Transactions only result in valid state (which includes rules, constraints, triggers etc.)
Isolation: Each transaction is executed independently of others safely within a concurrent system
Durability: Completed transactions will not be lost due to any later failures