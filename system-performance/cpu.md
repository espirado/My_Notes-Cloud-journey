Priority inversion occurs when a lower-priority thread holds a resource and blocks a higher-priority thread from running. This reduces the performance of the higher-priority work, as it is blocked waiting.

This can be solved using a priority inheritance scheme. Here is an example of how this can work (based on a real-world case):

Thread A performs monitoring and has a low priority. It acquires an address space lock for a production database, to check memory usage.

Thread B, a routine task to perform compression of system logs, begins running.

There is insufficient CPU to run both. Thread B preempts A and runs.

Thread C is from the production database, has a high priority, and has been sleeping waiting for I/O. This I/O now completes, putting thread C back into the runnable state.

Thread C preempts B, runs, but then blocks on the address space lock held by thread A. Thread C leaves CPU.

The scheduler picks the next-highest-priority thread to run: B.

With thread B running, a high-priority thread, C, is effectively blocked on a lower-priority thread, B. This is priority inversion.

Priority inheritance gives thread A thread C’s high priority, preempting B, until it releases the lock. Thread C can now run.


uptime/top: Check the load averages to see if load is increasing or decreasing over time. Bear this in mind when using the following tools, as load may be changing during your analysis.

vmstat: Run vmstat(1) with a one-second interval and check the system-wide CPU utilization (“us” + “sy”). Utilization approaching 100% increases the likelihood of scheduler latency.

mpstat: Examine statistics per-CPU and check for individual hot (busy) CPUs, identifying a possible thread scalability problem.

top: See which processes and users are the top CPU consumers.

pidstat: Break down the top CPU consumers into user- and system-time.

perf/profile: Profile CPU usage stack traces for both user- or kernel-time, to identify why the CPUs are in use.

perf: Measure IPC as an indicator of cycle-based inefficiencies.

showboost/turboboost: Check the current CPU clock rates, in case they are unusually low.

dmesg: Check for CPU temperature stall messages (“cpu clock throttled”).



Tool

Description

6.6.1

uptime

Load averages

6.6.2

vmstat

Includes system-wide CPU averages

6.6.3

mpstat

Per-CPU statistics

6.6.4

sar

Historical statistics

6.6.5

ps

Process status

6.6.6

top

Monitor per-process/thread CPU usage

6.6.7

pidstat

Per-process/thread CPU breakdowns

6.6.8

time, ptime

Time a command, with CPU breakdowns

6.6.9

turboboost

Show CPU clock rate and other states

6.6.10

showboost

Show CPU clock rate and turbo boost

6.6.11

pmcarch

Show high-level CPU cycle usage

6.6.12

tlbstat

Summarize TLB cycles

6.6.13

perf

CPU profiling and PMC analysis

6.6.14

profile

Sample CPU stack traces

6.6.15

cpudist

Summarize on-CPU time

6.6.16

runqlat

Summarize CPU run queue latency

6.6.17

runqlen

Summarize CPU run queue length

6.6.18

softirqs

Summarize soft interrupt time

6.6.19

hardirqs

Summarize hard interrupt time

6.6.20

bpftrace

Tracing programs for CPU analysis


6.6.1 uptime
uptime(1) is one of several commands that print the system load averages:
Load Averages
The load averages indicate the demand for system resources: higher means more demand.

6.6.2 vmstat
The virtual memory statistics command, vmstat(8), prints system-wide CPU averages in the last few columns, and a count of runnable threads in the first column.

6.6.3 mpstat
The multiprocessor statistics tool, mpstat(1), can report statistics per CPU. 

6.6.4 sar
The system activity reporter, sar(1), can be used to observe current activity and can be configured to archive and report historical statistics.

6.6.5 ps
The process status command, ps(1), can list details on all processes, including CPU usage statistics

The top(1) command monitors top running processes, updating the screen at regular intervals.

6.6.7 pidstat
The Linux pidstat(1) tool prints CPU usage by process or thread, including user- and system-time breakdowns.

6.6.8 time, ptime
The time(1) command can be used to run programs and report CPU usage. It is provided in the operating system under /usr/bin, and as a shell built-i

6.6.9 turbostat
turbostat(1) is a model-specific register (MSR)–based tool that shows the state of the CPUs, and is often available in a linux-tools-common package
\
6.6.11 pmcarch
pmcarch(8) shows a high-level view of CPU cycle performance. It is a PMC-based tool based on the Intel “architectural set” of PMCs

6.6.12 tlbstat
tlbstat(8) is another tool from pmc-cloud-tools, which shows the TLB cache statistics

6.6.15 cpudist
cpudist(8)12 is a BCC tool for showing the distribution of on-CPU time for each thread wakeup. This can be used to help characterize CPU workloads, providing details for later tuning and design decisions.

6.6.16 runqlat
runqlat(8)13 is a BCC and bpftrace tool for measuring CPU scheduler latency, often called run queue latency (even when no longer implemented using run queues). It is useful for identifying and quantifying issues of CPU saturation, where there is more demand for CPU resources than they can service. The metric measured by runqlat(8) is the time each thread (task) spends waiting for its turn on CPU.

6.6.17 runqlen
runqlen(8)14 is a BCC and bpftrace tool for sampling the length of the CPU run queues, counting how many tasks are waiting their turn, and presenting this as a linear histogram.

6.6.18 softirqs
softirqs(8)15 is a BCC tool that shows the time spent servicing soft IRQs (soft interrupts). The system-wide time in soft interrupts is readily available from different tools. For example, mpstat(1) shows it as %soft. There is also /proc/softirqs to show counts of soft IRQ events. The BCC softirqs(8) tool differs in that it can show time per soft IRQ rather than an event count



.6.19 hardirqs
hardirqs(8)16 is a BCC tool that shows time spent servicing hard IRQs (hard interrupts). The system-wide time in hard interrupts is readily available from different tools. For example, mpstat(1) shows it as %irq. There is also /proc/interrupts to show counts of hard IRQ events. The BCC hardirqs(8) tool differs in that it can show time per hard IRQ rather than an event count.


6.6.20 bpftrace
bpftrace is a BPF-based tracer that provides a high-level programming language, allowing the creation of powerful one-liners and short scripts. It is well suited for custom application analysis based on clues from other tools. 