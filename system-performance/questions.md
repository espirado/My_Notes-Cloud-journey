Answer the following questions about OS terminology:

What is the difference between a process, a thread, and a task?

What is a mode switch and a context switch?

What is the difference between paging and process swapping?

What is the difference between I/O-bound and CPU-bound workloads?

Answer the following conceptual questions:

Describe the role of the kernel.

Describe the role of system calls.

Describe the role of VFS and its location in the I/O stack.

Answer the following deeper questions:

List the reasons why a thread would leave the current CPU.

Describe the advantages of virtual memory and demand paging.


List some static performance tools.

What is profiling?

Why would profilers use 99 Hertz instead of 100 Hertz?

What is tracing?

What is static instrumentation?

Describe why dynamic instrumentation is important.

What is the difference between tracepoints and kprobes?

Describe the expected CPU overhead (low/medium/high) from the following:

Disk IOPS counters (as seen by iostat(1))

Tracing per-event disk I/O via tracepoints or kprobes

Tracing per-event context switches (tracepoints/kprobes)

Tracing per-event process execution (execve(2)) (tracepoints/kprobes)

Tracing per-event libc malloc() via uprobes

Describe why PMCs are valuable for performance analysis.

Given an observability tool, describe how you could determine what instrumentation sources it uses.



examine the following aspects of the static configuration:

What version of the application is running, and what are its dependencies? Are there newer versions? Do their release notes mention performance improvements?

Are there known performance issues? Is there a bug database that lists them?

How is the application configured?

If it was configured or tuned differently from the defaults, what was the reason? (Was it based on measurements and analysis, or guesswork?)

Does the application employ a cache of objects? How is it sized?

Does the application run concurrently? How is that configured (e.g., thread pool sizing)?

Is the application running in a special mode? (For example, debug mode may have been enabled and be reducing performance, or the application may be a debug build instead of a release build.)

What system libraries does the application use? What versions are they?

What memory allocator does the application use?

Is the application configured to use large pages for its heap?

Is the application compiled? What version of the compiler? What compiler options and optimizations? 64-bit?

Does the native code include advanced instructions? (Should it?) (For example, SIMD/vector instructions including Intel SSE.)

Has the application encountered an error, and is it now in a degraded mode? Or is it misconfigured and always running in a degraded mode?

Are there system-imposed limits or resource controls for CPU, memory, file system, disk, or network usage? (These are common with cloud computing.)



Answer the following questions about terminology:

What is a cache?

What is a ring buffer?

What is a spin lock?

What is an adaptive mutex lock?

What is the difference between concurrency and parallelism?

What is CPU affinity?

Answer the following conceptual questions:

What are the general pros and cons of using a large I/O size?

What is a hash table of locks used for?

Describe general performance characteristics of the runtime of compiled languages, interpreted languages, and those using virtual machines.

Explain the role of garbage collection and how it can affect performance.

Choose an application, and answer the following basic questions about it:

What is the role of the application?

What discrete operation does the application perform?

Does the application run in user mode or kernel mode?

How is the application configured? What key options are available regarding performance?

What performance metrics are provided by the application?

What logs does the application create? Do they contain performance information?

Has the most recent version of the application fixed performance issues?

Are there known performance bugs for the application?

Does the application have a community (e.g., IRC, meetups)? A performance community?

Are there books about the application? Performance books?

Are there well-known performance experts for the application? Who are they?

Choose an application that is under load, and perform these tasks (many of which may require the use of dynamic tracing):

Before taking any measurements, do you expect the application to be CPU-bound or I/O-bound? Explain your reasoning.

Determine using observability tools if it is CPU-bound or I/O-bound.

Generate a CPU flame graph for the application. You may need to fix symbols and stack traces for this to work. What is the hottest CPU code path?

Generate an off-CPU flame graph for the application. What is the longest blocking event during the application’s request (ignore idle stacks)?

Characterize the size of I/O it performs (e.g., file system reads/writes, network sends/receives).

Does the application have caches? Identify their size and hit rate.

Measure the latency (response time) for the operation that the application serves. Show the average, minimum, maximum, and full distribution.

Perform drill-down analysis of the operation, investigating the origin of the bulk of the latency.

Characterize the workload applied to the application (especially who and what).

Step through the static performance tuning checklist.

Does the application run concurrently? Investigate its use of synchronization primitives.


Answer the following questions about CPU terminology:

What is the difference between a process and a processor?

What is a hardware thread?

What is the run queue?

What is the difference between user time and kernel time?

Answer the following conceptual questions:

Describe CPU utilization and saturation.

Describe how the instruction pipeline improves CPU throughput.

Describe how processor instruction width improves CPU throughput.

Describe the advantages of multiprocess and multithreaded models.

Answer the following deeper questions:

Describe what happens when the system CPUs are overloaded with runnable work, including the effect on application performance.

When there is no runnable work to perform, what do the CPUs do?

When handed a suspected CPU performance issue, name two methodologies you would use early during the investigation, and explain why.

Develop the following procedures for your environment:

A USE method checklist for CPU resources. Include how to fetch each metric (e.g., which command to execute) and how to interpret the result. Try to use existing OS observability tools before installing or using additional software products.

A workload characterization checklist for CPU resources. Include how to fetch each metric, and try to use existing OS observability tools first.

Perform these tasks:

Calculate the load average for the following system, whose load is at steady state with no significant disk/lock load:

The system has 64 CPUs.

The system-wide CPU utilization is 50%.

The system-wide CPU saturation, measured as the total number of runnable and queued threads on average, is 2.0.

Choose an application, and profile its user-level CPU usage. Show which code paths are consuming the most CPU.

(optional, advanced) Develop bustop(1)—a tool that shows physical bus or interconnect utilization—with a presentation similar to iostat(1): a list of buses, columns for throughput in each direction, and utilization. Include saturation and error metrics if possible. This will require using PMCs.


Answer the following questions about memory terminology:

What is a page of memory?

What is resident memory?

What is virtual memory?

Using Linux terminology, what is the difference between paging and swapping?

Answer the following conceptual questions:

What is the purpose of demand paging?

Describe memory utilization and saturation.

What is the purpose of the MMU and the TLB?

What is the role of the page-out daemon?

What is the role of the OOM killer?

Answer the following deeper questions:

What is anonymous paging, and why is it more important to analyze than file system paging?

Describe the steps the kernel takes to free up more memory when free memory becomes exhausted on Linux-based systems.

Describe the performance advantages of slab-based allocation.

Develop the following procedures for your operating system:

A USE method checklist for memory resources. Include how to fetch each metric (e.g., which command to execute) and how to interpret the result. Try to use existing OS observability tools before installing or using additional software products.

Create a workload characterization checklist for memory resources. Include how to fetch each metric, and try to use existing OS observability tools first.

Perform these tasks:

Choose an application, and summarize code paths that lead to memory allocation (malloc(3)).

Choose an application that has some degree of memory growth (calling brk(2) or sbrk(2)), and summarize code paths that lead to this growth.

Describe the memory activity visible in the following Linux output alone:

Click here to view code image

# vmstat 1
procs -----------memory-------- ---swap-- -----io---- --system-- -----cpu-----
 r  b   swpd   free  buff cache   si   so    bi    bo   in   cs us sy id wa st
 2  0 413344  62284    72  6972    0    0    17    12    1    1  0  0 100  0  0
 2  0 418036  68172    68  3808    0 4692  4520  4692 1060 1939 61 38  0  1  0
 2  0 418232  71272    68  1696    0  196 23924   196 1288 2464 51 38  0 11  0
 2  0 418308  68792    76  2456    0   76  3408    96 1028 1873 58 39  0  3  0
 1  0 418308  67296    76  3936    0    0  1060     0 1020 1843 53 47  0  0  0
 1  0 418308  64948    76  3936    0    0     0     0 1005 1808 36 64  0  0  0
 1  0 418308  62724    76  6120    0    0  2208     0 1030 1870 62 38  0  0  0
 1  0 422320  62772    76  6112    0 4012     0  4016 1052 1900 49 51  0  0  0
 1  0 422320  62772    76  6144    0    0     0     0 1007 1826 62 38  0  0  0
 1  0 422320  60796    76  6144    0    0     0     0 1008 1817 53 47  0  0  0
 1  0 422320  60788    76  6144    0    0     0     0 1006 1812 49 51  0  0  0
 3  0 430792  65584    64  5216    0 8472  4912  8472 1030 1846 54 40  0  6  0
 1  0 430792  64220    72  6496    0    0  1124    16 1024 1857 62 38  0  0  0
 2  0 434252  68188    64  3704    0 3460  5112  3460 1070 1964 60 40  0  0  0
 2  0 434252  71540    64  1436    0    0 21856     0 1300 2478 55 41  0  4  0
 1  0 434252  66072    64  3912    0    0  2020     0 1022 1817 60 40  0  0  0
[...]
(optional, advanced) Find or develop metrics to show how well the kernel NUMA memory locality policies are working in practice. Develop “known” workloads that have good or poor memory locality for testing the metrics.