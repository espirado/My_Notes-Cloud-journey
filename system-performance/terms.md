IOPS: Input/output operations per second is a measure of the rate of data transfer operations. For disk I/O, IOPS refers to reads and writes per second.

Throughput: The rate of work performed. Especially in communications, the term is used to refer to the data rate (bytes per second or bits per second). In some contexts (e.g., databases) throughput can refer to the operation rate (operations per second or transactions per second).

Response time: The time for an operation to complete. This includes any time spent waiting and time spent being serviced (service time), including the time to transfer the result.

Latency: A measure of time an operation spends waiting to be serviced. In some contexts it can refer to the entire time for an operation, equivalent to response time. See Section 2.3, Concepts, for examples.

Utilization: For resources that service requests, utilization is a measure of how busy a resource is, based on how much time in a given interval it was actively performing work. For resources that provide storage, utilization may refer to the capacity that is consumed (e.g., memory utilization).

Saturation: The degree to which a resource has queued work it cannot service.

Bottleneck: In systems performance, a bottleneck is a resource that limits the performance of the system. Identifying and removing systemic bottlenecks is a key activity of systems performance.

Workload: The input to the system or the load applied is the workload. For a database, the workload consists of the database queries and commands sent by the clients.

Cache: A fast storage area that can duplicate or buffer a limited amount of data, to avoid communicating directly with a slower tier of storage, thereby improving performance. For economic reasons, a cache is often smaller than the slower tier.

Performance metrics are not free; at some point, CPU cycles must be spent to gather and store them. This causes overhead, which can negatively affect the performance of the target of measurement. This is called the observer effect. (It is often confused with Heisenberg’s Uncertainty Principle, which describes the limit of precision at which pairs of physical properties, such as position and momentum, may be known.)

Caching is frequently used to improve performance. A cache stores results from a slower storage tier in a faster storage tier, for reference. An example is caching disk blocks in main memory (RAM).

Algorithms
Cache management algorithms and policies determine what to store in the limited space available for a cache.

Most recently used (MRU) refers to a cache retention policy, which decides what to favor keeping in the cache: the objects that have been used most recently. Least recently used (LRU) can refer to an equivalent cache eviction policy, deciding what objects to remove from the cache when more space is needed. There are also most frequently used (MFU) and least frequently used (LFU) policies.

You may encounter not frequently used (NFU), which may be an inexpensive but less thorough version of LRU.

Hot, Cold, and Warm Caches
These words are commonly used to describe the state of the cache:

Cold: A cold cache is empty, or populated with unwanted data. The hit ratio for a cold cache is zero (or near zero as it begins to warm up).

Warm: A warm cache is one that is populated with useful data but doesn’t have a high enough hit ratio to be considered hot.

Hot: A hot cache is populated with commonly requested data and has a high hit ratio, for example, over 99%.

Warmth: Cache warmth describes how hot or cold a cache is. An activity that improves cache warmth is one that aims to improve the cache hit ratio.

The tasks of workload analysis include identifying and confirming issues—for example, by looking for latency beyond an acceptable threshold—then finding the source of the latency and confirming that the latency is improved after applying a fix. Note that the starting point is the application. Investigating latency usually involves drilling down deeper into the application, libraries, and the operating system (kernel).