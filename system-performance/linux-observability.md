 # Static Performance Tools
 There is another type of observability that examines attributes of the system at rest rather than under active workload. This was described as the static performance tuning methodolog

 # Crisis Tools

 Package

Provides

procps

ps(1), vmstat(8), uptime(1), top(1)

util-linux

dmesg(1), lsblk(1), lscpu(1)

sysstat

iostat(1), mpstat(1), pidstat(1), sar(1)

iproute2

ip(8), ss(8), nstat(8), tc(8)

numactl

numastat(8)

linux-tools-common linux-tools-$(uname -r)

perf(1), turbostat(8)

bcc-tools (aka bpfcc-tools)

opensnoop(8), execsnoop(8), runqlat(8), runqlen(8), softirqs(8), hardirqs(8), ext4slower(8), ext4dist(8), biotop(8), biosnoop(8), biolatency(8), tcptop(8), tcplife(8), trace(8), argdist(8), funccount(8), stackcount(8), profile(8), and many more

bpftrace

bpftrace, basic versions of opensnoop(8), execsnoop(8), runqlat(8), runqlen(8), biosnoop(8), biolatency(8), and more

perf-tools-unstable

Ftrace versions of opensnoop(8), execsnoop(8), iolatency(8), iosnoop(8), bitesize(8), funccount(8), kprobe(8)

trace-cmd

trace-cmd(1)

nicstat

nicstat(1)

ethtool

ethtool(8)

tiptop

tiptop(1)

msr-tools

rdmsr(8), wrmsr(8)

github.com/brendangregg/msr-cloud-tools

showboost(8), cpuhot(8), cputemp(8)

github.com/brendangregg/pmc-cloud-tools

pmcarch(8), cpucache(8), icache(8), tlbstat(8), resstalls(8)


vmstat(8): Virtual and physical memory statistics, system-wide

mpstat(1): Per-CPU usage

iostat(1): Per-disk I/O usage, reported from the block device interface

nstat(8): TCP/IP stack statistics

sar(1): Various statistics; can also archive them for historical reporting

ps(1): Shows process status, shows various process statistics, including memory and CPU usage.

top(1): Shows top processes, sorted by CPU usage or another statistic.

pmap(1): Lists process memory segments with usage statistics.



Profiling characterizes the target by collecting a set of samples or snapshots of its behavior. CPU usage is a common target of profiling, where timer-based samples are taken of the instruction pointer or stack trace to characterize CPU-consuming code paths. 

System-wide Linux profilers include:

perf(1): The standard Linux profiler, which includes profiling subcommands.

profile(8): A BPF-based CPU profiler from the BCC repository (covered in Chapter 15, BPF) that frequency counts stack traces in kernel context.

Intel VTune Amplifier XE: Linux and Windows profiling, with a graphical interface including source browsing.

Process-oriented profilers include:

gprof(1): The GNU profiling tool, which analyzes profiling information added by compilers (e.g., gcc -pg).

cachegrind: A tool from the valgrind toolkit, can profile hardware cache usage (and more) and visualize profiles using kcachegrind.

Java Flight Recorder (JFR): Programming languages often have their own special-purpose profilers that can inspect language context. For example, JFR for Java.

These tracing tools examine system-wide activity in the context of system software or hardware resources, using kernel tracing facilities. Linux tools include:

tcpdump(8): Network packet tracing (uses libpcap)

biosnoop(8): Block I/O tracing (uses BCC or bpftrace)

execsnoop(8): New processes tracing (uses BCC or bpftrace)

perf(1): The standard Linux profiler, can also trace events

perf trace: A special perf subcommand that traces system calls system-wide

Ftrace: The Linux built-in tracer

BCC: A BPF-based tracing library and toolkit

bpftrace: A BPF-based tracer (bpftrace(8)) and toolkit

strace(1): System call tracing

gdb(1): A source-level debugger


Linux observability sources

Type

Source

Per-process counters

/proc

System-wide counters

/proc, /sys

Device configuration and counters

/sys

Cgroup statistics

/sys/fs/cgroup

Per-process tracing

ptrace

Hardware counters (PMCs)

perf_event

Network statistics

netlink

Network packet capture

libpcap

Per-thread latency metrics

Delay accounting

System-wide tracing

Function profiling (Ftrace), tracepoints, software events, kprobes, uprobes, perf_event


Those related to per-process performance observability include:

limits: In-effect resource limits

maps: Mapped memory regions

sched: Various CPU scheduler statistics

schedstat: CPU runtime, latency, and time slices

smaps: Mapped memory regions with usage statistics

stat: Process status and statistics, including total CPU and memory usage

statm: Memory usage summary in units of pages

status: stat and statm information, labeled

fd: Directory of file descriptor symlinks (also see fdinfo)

cgroup: Cgroup membership information

task: Directory of per-task (thread) statistics



System-wide files related to performance observability include:

cpuinfo: Physical processor information, including every virtual CPU, model name, clock speed, and cache sizes.

diskstats: Disk I/O statistics for all disk devices

interrupts: Interrupt counters per CPU

loadavg: Load averages

meminfo: System memory usage breakdowns

net/dev: Network interface statistics

net/netstat: System-wide networking statistics

net/tcp: Active TCP socket information

pressure/: Pressure stall information (PSI) files

schedstat: System-wide CPU scheduler statistics

self: A symlink to the current process ID directory, for convenience

slabinfo: Kernel slab allocator cache statistics

stat: A summary of kernel and system resource statistics: CPUs, disks, paging, swap, processes

zoneinfo: Memory zone information


Linux systems with the CONFIG_TASK_DELAY_ACCT option track time per task in the following states:

Scheduler latency: Waiting for a turn on-CPU

Block I/O: Waiting for a block I/O to complete

Swapping: Waiting for paging (memory pressure)

Memory reclaim: Waiting for the memory reclaim routine


NETLINK_ROUTE: Route information (there is also /proc/net/route)

NETLINK_SOCK_DIAG: Socket information

NETLINK_SELINUX: SELinux event notifications

NETLINK_AUDIT: Auditing (security)

NETLINK_SCSITRANSPORT: SCSI transports

NETLINK_CRYPTO: Kernel crypto information