Generic system performance methodologies

Section

Methodology

Type



Streetlight anti-method

Observational analysis



Random change anti-method

Experimental analysis



Blame-someone-else anti-method

Hypothetical analysis



Ad hoc checklist method

Observational and experimental analysis



Problem statement

Information gathering



Scientific method

Observational analysis



Diagnosis cycle

Analysis life cycle



Tools method

Observational analysis



USE method

Observational analysis



RED method

Observational analysis



Workload characterization

Observational analysis, capacity planning



Drill-down analysis

Observational analysis



Latency analysis

Observational analysis



Method R

Observational analysis



Event tracing

Observational analysis



Baseline statistics

Observational analysis



Static performance tuning

Observational analysis, capacity planning



Cache tuning

Observational analysis, tuning



Micro-benchmarking

Experimental analysis



Performance mantras

Tuning



Queueing theory

Statistical analysis, capacity planning



Capacity planning

Capacity planning, tuning



Quantifying performance gains

Statistical analysis



Performance monitoring

Observational analysis, capacity planning


# Linux

Methodology

Type

1.10.1

Linux performance analysis in 60s

Observational analysis

5.4.1

CPU profiling

Observational analysis

5.4.2

Off-CPU analysis

Observational analysis

6.5.5

Cycle analysis

Observational analysis

6.5.8

Priority tuning

Tuning

6.5.8

Resource controls

Tuning

6.5.9

CPU binding

Tuning

7.4.6

Leak detection

Observational analysis

7.4.10

Memory shrinking

Experimental analysis

8.5.1

Disk analysis

Observational analysis

8.5.7

Workload separation

Tuning

9.5.10

Scaling

Capacity planning, tuning

10.5.6

Packet sniffing

Observational analysis

10.5.7

TCP analysis

Observational analysis

12.3.1

Passive benchmarking

Experimental analysis

12.3.2

Active benchmarking

Observational analysis

12.3.6

Custom benchmarks

Software development

12.3.7

Ramping load

Experimental analysis

12.3.8

Sanity check

Observational analysis

# 2.5.1 Streetlight Anti-Method

This method is actually the absence of a deliberate methodology. The user analyzes performance by choosing observability tools that are familiar, found on the Internet, or just at random to see if anything obvious shows up. This approach is hit or miss and can overlook many types of issues.

# 2.5.2 Random Change Anti-Method

This is an experimental anti-methodology. The user randomly guesses where the problem may be and then changes things until it goes away. To determine whether performance has improved or not as a result of each change, a metric is studied, such as application runtime, operation time, latency, operation rate (operations per second), or throughput (bytes per second). The approach is as follows:

Pick a random item to change (e.g., a tunable parameter).

Change it in one direction.

Measure performance.

Change it in the other direction.

Measure performance.

Were the results in step 3 or step 5 better than the baseline? If so, keep the change and go back to step 1.

# 2.5.3 Blame-Someone-Else Anti-Method

This anti-methodology follows these steps:

Find a system or environment component for which you are not responsible.

Hypothesize that the issue is with that component.

Redirect the issue to the team responsible for that component.

When proven wrong, go back to step 1.

# 2.5.4 Ad Hoc Checklist Method

Stepping through a canned checklist is a common methodology used by support professionals when asked to check and tune a system, often in a short time frame. A typical scenario involves the deployment of a new server or application in production, and a support professional spending half a day checking for common issues now that the system is under real load. These checklists are ad hoc and are built from recent experience and issues for that system type.

# 2.5.5 Problem Statement

Defining the problem statement is a routine task for support staff when first responding to issues. 

# 2.5.6 Scientific Method

The scientific method studies the unknown by making hypotheses and then testing them. It can be summarized by the following steps:

Question

Hypothesis

Prediction

Test

Analysis

The question is the performance problem statement. From this you can hypothesize what the cause of poor performance may be. Then you construct a test, which may be observational or experimental, that tests a prediction based on the hypothesis. You finish with analysis of the test data collected.

# 2.5.7 Diagnosis Cycle

hypothesis → instrumentation → data → hypothesis

Like the scientific method, this method also deliberately tests a hypothesis through the collection of data. The cycle emphasizes that the data can lead quickly to a new hypothesis, which is tested and refined, and so on. This is similar to a doctor making a series of small tests to diagnose a patient and refining the hypothesis based on the result of each test.

# 2.5.8 Tools Method

The result of this is a prescriptive checklist showing which tool to run, which metrics to read, and how to interpret them. While this can be fairly effective, it relies exclusively on available (or known) tools, which can provide an incomplete view of the system, similar to the streetlight anti-method. Worse, the user is unaware that they have an incomplete view—and may remain unaware. Issues that require custom tooling (e.g., dynamic tracing) may never be identified and solved.

# 2.5.9 The USE Method

 The utilization, saturation, and errors (USE) method should be used early in a performance investigation to identify systemic bottlenecks [Gregg 13b]. It is a methodology that focuses on system resources and can be summarized as:

For every resource, check utilization, saturation, and errors.

These terms are defined as follows:

Resources: All physical server functional components (CPUs, buses, . . .). Some software resources can also be examined, provided that the metrics make sense.

Utilization: For a set time interval, the percentage of time that the resource was busy servicing work. While busy, the resource may still be able to accept more work; the degree to which it cannot do so is identified by saturation.

Saturation: The degree to which the resource has extra work that it can’t service, often waiting on a queue. Another term for this is pressure.

Errors: The count of error events.

Some software resources can be similarly examined. This usually applies to smaller components of software (not entire applications), for example:

Mutex locks: Utilization may be defined as the time the lock was held, saturation by those threads queued waiting on the lock.

Thread pools: Utilization may be defined as the time threads were busy processing work, saturation by the number of requests waiting to be serviced by the thread pool.

Process/thread capacity: The system may have a limited number of processes or threads, whose current usage may be defined as utilization; waiting on allocation may be saturation; and errors are when the allocation failed (e.g., “cannot fork”).

File descriptor capacity: Similar to process/thread capacity, but for file descriptors.


Workloads can be characterized by answering the following questions:

Who is causing the load? Process ID, user ID, remote IP address?

Why is the load being called? Code path, stack trace?

What are the load characteristics? IOPS, throughput, direction (read/write), type? Include variance (standard deviation) where appropriate.

How is the load changing over time? Is there a daily pattern?

# 2.5.12 Drill-Down Analysis
Drill-down analysis starts with examining an issue at a high level, then narrowing the focus based on the previous findings, discarding areas that seem uninteresting, and digging deeper into the interesting ones. The process can involve digging down through deeper layers of the software stack, to hardware if necessary, to find the root cause of the issue

# 2.5.13 Latency Analysis
Latency analysis examines the time taken to complete an operation and then breaks it into smaller components, continuing to subdivide the components with the highest latency so that the root cause can be identified and quantified. Similarly to drill-down analysis, latency analysis may drill down through layers of the software stack to find the origin of latency issues.

# 2.5.14 Method R
Method R is a performance analysis methodology developed for Oracle databases that focuses on finding the origin of latency, based on Oracle trace events [Millsap 03]. It is described as “a response time-based performance improvement method that yields maximum economic value to your business” and focuses on identifying and quantifying where time is spent during queries. While this is used for the study of databases, its approach could be applied to any system and is worth mentioning here as an avenue of possible study.

# 2.5.15 Event Tracing
Systems operate by processing discrete events. These include CPU instructions, disk I/O and other disk commands, network packets, system calls, library calls, application transactions, database queries, and so on. Performance analysis usually studies summaries of these events, such as operations per second, bytes per second, or average latency. Sometimes important detail is lost in the summary, and the events are best understood when inspected individually.

# 2.5.17 Static Performance Tuning
tatic performance tuning focuses on issues of the configured architecture. Other methodologies focus on the performance of the applied load: the dynamic performance [Elling 00]. Static performance analysis can be performed when the system is at rest and no load is applied.

# 2.5.18 Cache Tuning

Applications and operating systems may employ multiple caches to improve I/O performance, from the application down to the disks. See Chapter 3, Operating Systems, Section 3.2.11, Caching, for a full list. Here is a general strategy for tuning each cache level:

Aim to cache as high in the stack as possible, closer to where the work is performed, reducing the operational overhead of cache hits. This location should also have more metadata available, which can be used to improve the cache retention policy.

Check that the cache is enabled and working.

Check the cache hit/miss ratios and miss rate.

If the cache size is dynamic, check its current size.

Tune the cache for the workload. This task depends on available cache tunable parameters.

Tune the workload for the cache. Doing this includes reducing unnecessary consumers of the cache, which frees up more space for the target workload.

# 2.6 Modeling
Analytical modeling of a system can be used for various purposes, in particular scalability analysis: studying how performance scales as load or resources increase. Resources may be hardware (such as CPU cores) or software (processes or threads