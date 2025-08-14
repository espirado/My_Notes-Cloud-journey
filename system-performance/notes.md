The term capacity planning can refer to a number of the preceding activities. During design, it includes studying the resource footprint of development software to see how well the design can meet the target needs. After deployment, it includes monitoring resource usage to predict problems before they occur.

workload analysis and resource analysis, which approach the software stack from different directions.
Subjective performance can be made objective by defining clear goals, such as having a target average response time, or requiring a percentage of requests to fall within a certain latency range
Latency is a measure of time spent waiting, and is an essential performance metric. Used broadly, it can mean the time for any operation to complete, such as an application request, a database query, a file system operation, and so forth

BPF2-based observability tools, latency can now be measured from custom arbitrary points of interest and can provide data showing the full distribution of latency.
Observability refers to understanding a system through observation, and classifies the tools that accomplish this. This includes tools that use counters, profiling, and tracing. It does not include benchmark tools, which modify the state of the system by performing a workload experiment

A metric is a statistic that has been selected to evaluate or monitor a target. Most companies use monitoring agents to record selected statistics (metrics) at regular intervals, and chart them in a graphical interface to see changes over time.

 profiling usually refers to the use of tools that perform sampling: taking a subset (a sample) of measurements to paint a coarse picture of the target. 

 Tracing is event-based recording, where event data is captured and saved for later analysis or consumed on-the-fly for custom summaries and other actions. There are special-purpose tracing tools for system calls (e.g., Linux strace(1)) and network packets (e.g., Linux tcpdump(8)); and general-purpose tracing tools that can analyze the execution of all software and hardware events (e.g., Linux Ftrace, BCC, and bpftrace).

 Static instrumentation describes hard-coded software instrumentation points added to the source code. There are hundreds of these points in the Linux kernel that instrument disk I/O, scheduler events, system calls, and more. The Linux technology for kernel static instrumentation is called tracepoints. There is also a static instrumentation technology for user-space software called user statically defined tracing (USDT). USDT is used by libraries (e.g., libc) for instrumenting library calls and by many applications for instrumenting service requests.

 Dynamic instrumentation creates instrumentation points after the software is running, by modifying in-memory instructions to insert instrumentation routines. This is similar to how debuggers can insert a breakpoint on any function in running software. Debuggers pass execution flow to an interactive debugger when the breakpoint is hit, whereas dynamic instrumentation runs a routine and then continues the target software. This capability allows custom performance statistics to be created from any running software. Issues that were previously impossible or prohibitively difficult to solve due to a lack of observability can now be fixed.

BPF, which originally stood for Berkeley Packet Filter, is powering the latest dynamic tracing tools for Linux. BPF originated as a mini in-kernel virtual machine for speeding up the execution of tcpdump(8) expressions.
Methodologies are a way to document the recommended steps for performing various tasks in systems performance. Without a methodology, a performance investigation can turn into a fishing expedition: trying random things in the hope of catching a win.

Understand key performance metrics: latency, utilization, and saturation.

Develop a sense for the scale of measured time, down to nanoseconds.

Learn tuning trade-offs, targets, and when to stop analysis.

Identify problems of workload versus architecture.

Consider resource versus workload analysis.

Follow different performance methodologies, including: the USE method, workload characterization, latency analysis, static performance tuning, and performance mantras.

Understand the basics of statistics and queueing theory.


# workload analysis 
- examines the performances of applications 
   - The target for workload 
            - latency 
            - Request 
            - Completion 
- Workload characterizations - checking and summarizing workload attributes 
Methodoligies 
  streetlight anti-method  - observational analysis 
  Random change anti-method - Experimental analysis 
  Blame someone-else antimenthod  - Hypothetical analysis 
  Ad hoc checklist method    - observational and experimental analysis 
  Problem statement   - information gathering 
  scientific method    - Observational analyisis
  diagnosis cycle      -Analysis life cycle 
  Tools method        - Obsrrvational analysis 
  Use Method 
  Red method 
  Workload characterization 
  Drill down anlysis 
  Latency analyis 
  Method R 
  Event Tracing 
  Baseline statstics 
  Static performance tuning 
  Ccahe tunung 
  micro bechmarking 
  queing theory 
  Capacity planning 
  Quantifying performance gaining 
  Performance monitoring 

  I/O Scheduling - 
To schedule a set of I/O requests means to determine a good order in which to execute them. The order in which the application issues the system call is the best choice. Scheduling can improve the overall performance of the system, can share device access permission fairly to all the processes, and reduce the average waiting time, response time, and turnaround time for I/O to complete.

Buffering - 
A buffer is a memory area that stores data being transferred between two devices or between a device and an application. Buffering is done for three reasons. 
The first is to cope with a speed mismatch between the producer and consumer of a data stream. 
The second use of buffering is to provide adaptation for data that have different data-transfer sizes. 
The third use of buffering is to support copy semantics for the application I/O, "copy semantic " means, suppose that an application wants to write data on a disk that is stored in its buffer. it calls the write() system's call, providing a pointer to the buffer and the integer specifying the number of bytes to write


Caching - 
A cache is a region of fast memory that holds a copy of data. Access to the cached copy is much easier than the original file. For instance, the instruction of the currently running process is stored on the disk, cached in physical memory, and copied again in the CPU's secondary and primary cache. 

Spooling and Device Reservation - 
A spool is a buffer that holds the output of a device, such as a printer that cannot accept interleaved data streams. Although a printer can serve only one job at a time, several applications may wish to print their output concurrently, without having their output mixes together. 

Error Handling - 
An Os that uses protected memory can guard against many kinds of hardware and application errors so that a complete system failure is not the usual result of each minor mechanical glitch, Devices, and I/O transfers can fail in many ways, either for transient reasons, as when a network becomes overloaded or for permanent reasons, as when a disk controller becomes defective.

I/O Protection - 
Errors and the issue of protection are closely related. A user process may attempt to issue illegal I/O instructions to disrupt the normal function of a system. We can use the various mechanisms to ensure that such disruption cannot take place in the system

A Process Control Block (PCB) contains information about the process, i.e. registers, quantum, priority, etc. The Process Table is an array of PCBs, which logically contains a PCB for all of the current processes in the system.

A process table is a data structure maintained by the operating system to keep track of all active processes. It contains an entry for each process, known as the Process Control Block (PCB), which stores essential information like process ID, state, program counter, CPU registers, memory usage and resource allocations.

A process is the instance of a computer program in execution

Process scheduling is the activity of the process manager that handles the removal of the running process from the CPU and the selection of another process based on a particular strategy

Non-Preemptive: In this case, a process's resource cannot be taken before the process has finished running. When a running process finishes and transitions to a waiting state, resources are switched.
Preemptive: In this case, the OS can switch a process from running state to ready state. This switching happens because the CPU may give other processes priority and substitute the currently active process for the higher priority process

In order for a process execution to be continued from the same point at a later time, context switching is a mechanism to store and restore the state or context of a CPU in the Process Control block.

The three different categories of context-switching triggers are as follows.

Interrupts
Multitasking
User/Kernel switch

A thread is a single sequence stream within a process. Threads are also called lightweight processes as they possess some of the properties of processes. Each thread belongs to exactly one process.

Stack Space: Stores local variables, function calls, and return addresses specific to the thread.
Register Set: Hold temporary data and intermediate results for the thread's execution.
Program Counter: Tracks the current instruction being executed by the thread.
