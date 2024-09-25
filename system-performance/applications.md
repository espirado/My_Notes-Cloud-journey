Before diving into application performance, you should familiarize yourself with the role of the application, its basic characteristics, and its ecosystem in the industry. This forms the context within which you can understand application activity. It also gives you opportunities to learn about common performance issues and tuning and provides avenues for further study. To learn this context, try answering the following questions:

Function: What is the role of the application? Is it a database server, web server, load balancer, file server, object store?

Operation: What requests does the application serve, or what operations does it perform? Databases serve queries (and commands), web servers serve HTTP requests, and so on. This can be measured as a rate, to gauge load and for capacity planning.

Performance requirements: Does the company running the application have a service level objective (SLO) (e.g., 99.9% of requests at < 100 ms latency)?

CPU mode: Is the application implemented as user-level or kernel-level software? Most applications are user-level, executing as one or more processes, but some are implemented as kernel services (for example, NFS), and BPF programs are also kernel-level.

Configuration: How is the application configured, and why? This information may be found in a configuration file or via administration tools. Check if any tunable parameters related to performance have been changed, including buffer sizes, cache sizes, parallelism (processes or threads), and other options.

Host: What hosts the application? A server or cloud instance? What are the CPUs, memory topology, storage devices, etc.? What are their limits?

Metrics: Are application metrics provided, such as an operation rate? They may be provided by bundled tools or third-party tools, via API requests, or by processing operation logs.

Logs: What operation logs does the application create? What logs can be enabled? What performance metrics, including latency, are available from the logs? For example, MySQL supports a slow query log, providing valuable performance details for each query slower than a certain threshold.

Version: Is the application the latest version? Have performance fixes or improvements been noted in the release notes for recent versions?

Bugs: Is there a bug database for the application? What are the “performance” bugs for your version of the application? If you have a current performance issue, search the bug database to see if anything like it has happened before, how it was investigated, and what else was involved.

Source code: Is the application open source? If so, code paths identified by profilers and tracers can be studied, potentially leading to performance wins. You may be able to modify the application code yourself to improve performance, and submit your improvements upstream for inclusion in the official application.

Community: Is there a community for the application where performance findings are shared? Communities may include forums, blogs, Internet Relay Chat (IRC) channels, other chat channels (e.g., Slack), meetups, and conferences. Meetups and conferences often post slides and videos online, which are useful resources for years afterward. They may also have a community manager who shares community updates and news.

Books: Are there books about the application and/or its performance? Are they good books (e.g., written by an expert, practical/actionable, makes good use of reader’s time, up to date, etc.)?

Experts: Who are the recognized performance experts for the application? Learning their names can help you find material they have authored.


Apdex
Some companies use a target application performance index (ApDex or Apdex) as an objective and as a metric to monitor. It can better convey customer experience and involves first classifying customer events as to whether they are “satisfactory,” “tolerable,” or “frustrating.” The Apdex is then calculated using [Apdex 20]:

Apdex = (satisfactory + 0.5 × tolerable + 0 × frustrating) / total events

The resulting Apdex ranges from 0 (no satisfied customers) to 1 (all satisfied customers).

One way to efficiently improve application performance is to find the most common code path for the production workload and begin by improving that. If the application is CPU-bound, that may mean the code paths that are frequently on-CPU. If the application is I/O-bound, you should be looking at the code paths that frequently lead to I/O. These can be determined by analysis and profiling of the application, including studying stack traces and flame graphs

application performance can be improved: selecting an I/O size, caching, buffering, polling, concurrency and parallelism, non-blocking I/O, and processor binding


 Selecting an I/O Size
Costs associated with performing I/O can include initializing buffers, making a system call, mode or context switching, allocating kernel metadata, checking process privileges and limits, mapping addresses to devices, executing kernel and driver code to deliver the I/O, and, finally, freeing metadata and buffers. “Initialization tax” is paid for small and large I/O alike. For efficiency, the more data transferred by each I/O, the better.


Caching
The operating system uses caches to improve file system read performance and memory allocation performance; applications often use caches for a similar reason. Instead of always performing an expensive operation, the results of commonly performed operations may be stored in a local cache for future use. An example is the database buffer cache, which stores data from commonly performed database queries.

Buffering
To improve write performance, data may be coalesced in a buffer before being sent to the next level. This increases the I/O size and efficiency of the operation. Depending on the type of writes, it may also increase write latency, as the first write to a buffer waits for subsequent writes before being sent.

Polling
Polling is a technique in which the system waits for an event to occur by checking the status of the event in a loop, with pauses between checks. There are some potential performance problems with polling when there is little work to do:

Concurrency and Parallelism
Time-sharing systems (including all derived from Unix) provide program concurrency: the ability to load and begin executing multiple runnable programs. While their runtimes may overlap, they do not necessarily execute on-CPU at the same instant

To take advantage of a multiprocessor system, an application must execute on multiple CPUs at the same time. This is parallelism, which an application may accomplish by using multiple processes (multiprocess) or multiple threads (multithreaded),

Three common models of multithreaded programming are:

Service thread pool: A pool of threads services network requests, where each thread services one client connection at a time.

CPU thread pool: One thread is created per CPU. This is commonly used by long-duration batch processing, such as video encoding.

Staged event-driven architecture (SEDA): Application requests are decomposed into stages that may be processed by pools of one or more threads.

Hash Tables
A hash table of locks can be used to employ the optimum number of locks for a large number of data structures. 

Processor Binding
For NUMA environments, it can be advantageous for a process or thread to remain running on a single CPU and to run on the same CPU as it did previously after performing I/O. This can improve the memory locality of the application, reducing the cycles for memory I/O and improving overall application performance. Operating systems are well aware of this and are designed to keep application threads on the same CPUs (CPU affinity)