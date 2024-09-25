Operating system: This refers to the software and files that are installed on a system so that it can boot and execute programs. It includes the kernel, administration tools, and system libraries.

Kernel: The kernel is the program that manages the system, including (depending on the kernel model) hardware devices, memory, and CPU scheduling. It runs in a privileged CPU mode that allows direct access to hardware, called kernel mode.

Process: An OS abstraction and environment for executing a program. The program runs in user mode, with access to kernel mode (e.g., for performing device I/O) via system calls or traps into the kernel.

Thread: An executable context that can be scheduled to run on a CPU. The kernel has multiple threads, and a process contains one or more.

Task: A Linux runnable entity, which can refer to a process (with a single thread), a thread from a multithreaded process, or kernel threads.

BPF program: A kernel-mode program running in the BPF1 execution environment.

Main memory: The physical memory of the system (e.g., RAM).

Virtual memory: An abstraction of main memory that supports multitasking and oversubscription. It is, practically, an infinite resource.

Kernel space: The virtual memory address space for the kernel.

User space: The virtual memory address space for processes.

User land: User-level programs and libraries (/usr/bin, /usr/lib...).

Context switch: A switch from running one thread or process to another. This is a normal function of the kernel CPU scheduler, and involves switching the set of running CPU registers (the thread context) to a new set.

Mode switch: A switch between kernel and user modes.

System call (syscall): A well-defined protocol for user programs to request the kernel to perform privileged operations, including device I/O.

Processor: Not to be confused with process, a processor is a physical chip containing one or more CPUs.

Trap: A signal sent to the kernel to request a system routine (privileged action). Trap types include system calls, processor exceptions, and interrupts.

Hardware interrupt: A signal sent by physical devices to the kernel, usually to request servicing of I/O. An interrupt is a type of trap.

# 3.2.1 Kernel
The kernel is the core software of the operating system. What it does depends on the kernel model: Unix-like operating systems including Linux and BSD have a monolithic kernel that manages CPU scheduling, memory, file systems, network protocols, and system devices (disks, network interfaces, etc.).

Linux has recently changed its model by allowing a new software type: Extended BPF, which enables secure kernel-mode applications along with its own kernel API: BPF helpers. This allows some applications and system functions to be rewritten in BPF

The kernel is a large program, typically millions of lines of code. It primarily executes on demand, when a user-level program makes a system call, or a device sends an interrupt. Some kernel threads operate asynchronously for housekeeping, which may include the kernel clock routine and memory management tasks, but these try to be lightweight and consume very little CPU resources.

Workloads that perform frequent I/O, such as web servers, execute mostly in kernel context. Workloads that are compute-intensive usually run in user mode, uninterrupted by the kernel. It may be tempting to think that the kernel cannot affect the performance of these compute-intensive workloads, but there are many cases where it does. The most obvious is CPU contention, when other threads are competing for CPU resources and the kernel scheduler needs to decide which will run and which will wait. The kernel also chooses which CPU a thread will run on and can choose CPUs with warmer hardware caches or better memory locality for the process, to significantly improve performance.

Kernel and user mode are implemented on processors using privilege rings

In a traditional kernel, a system call is performed by switching to kernel mode and then executing the system call code

Switching between user and kernel modes is a mode switch.

All system calls mode switch. Some system calls also context switch: those that are blocking, such as for disk and network I/O, will context switch so that another thread can run while the first is blocked.

User-mode syscalls: It is possible to implement some syscalls in a user-mode library alone. The Linux kernel does this by exporting a virtual dynamic shared object (vDSO) that is mapped into the process address space, which contains syscalls such as gettimeofday(2) and getcpu(2) [Drysdale 14].

Memory mappings: Used for demand paging (see Chapter 7, Memory, Section 7.2.3, Demand Paging), it can also be used for data stores and other I/O, avoiding syscall overheads.

Kernel bypass: This allows user-mode programs to access devices directly, bypassing syscalls and the typical kernel code path. For example, DPDK for networking: the Data Plane Development Kit.

Kernel-mode applications: These include the TUX web server [Lever 00], implemented in-kernel, and more recently the extended BPF technology

# 3.2.3 System Calls
System calls request the kernel to perform privileged system routines. There are hundreds of system calls available, but some effort is made by kernel maintainers to keep that number as small as possible, to keep the kernel simple


Key system calls

System Call

Description

read(2)

Read bytes

write(2)

Write bytes

open(2)

Open a file

close(2)

Close a file

fork(2)

Create a new process

clone(2)

Create a new process or thread

exec(2)

Execute a new program

connect(2)

Connect to a network host

accept(2)

Accept a network connection

stat(2)

Fetch file statistics

ioctl(2)

Set I/O properties, or other miscellaneous functions

mmap(2)

Map a file to the memory address space

brk(2)

Extend the heap pointer

futex(2)

Fast user-space mutex


ioctl(2): This is commonly used to request miscellaneous actions from the kernel, especially for system administration tools, where another (more obvious) system call isn’t suitable. See the example that follows.

mmap(2): This is commonly used to map executables and libraries to the process address space, and for memory-mapped files. It is sometimes used to allocate the working memory of a process, instead of the brk(2)-based malloc(2), to reduce the syscall rate and improve performance (which doesn’t always work due to the trade-off involved: memory-mapping management).

brk(2): This is used to extend the heap pointer, which defines the size of the working memory of the process. It is typically performed by a system memory allocation library, when a malloc(3) (memory allocate) call cannot be satisfied from the existing space in the heap. See Chapter 7, Memory.

futex(2): This syscall is used to handle part of a user space lock: the part that is likely to block.


# 3.2.4 Interrupts
An interrupt is a signal to the processor that some event has occurred that needs processing, and interrupts the current execution of the processor to handle it. It typically causes the processor to enter kernel mode if it isn’t already, save the current thread state, and then run an interrupt service routine (ISR) to process the event.

A process is an environment for executing a user-level program. It consists of a memory address space, file descriptors, thread stacks, and registers. In some ways, a process is like a virtual early computer, where only one program is executing with its own registers and stacks.

Processes are multitasked by the kernel, which typically supports the execution of thousands of processes on a single system. They are individually identified by their process ID (PID), which is a unique numeric identifier.

A process contains one or more threads, which operate in the process address space and share the same file descriptors.

 A thread is an executable context consisting of a stack, registers, and an instruction pointer (also called a program counter)

Multiple threads allow a single process to execute in parallel across multiple CPUs. On Linux, threads and processes are both tasks.

The first process launched by the kernel is called “init,” from /sbin/init (by default), with PID 1, which launches user space services

In Unix this involved running start scripts from /etc, a method now referred to as SysV (after Unix System V).

Processes are normally created using the fork(2) system call on Unix systems


On Linux, C libraries typically implement the fork function by wrapping around the versatile clone(2) syscall. These syscalls create a duplicate of the process, with its own process ID. The exec(2) system call (or a variant, such as execve(2)) can then be called to begin execution of a different program.

The fork(2) or clone(2) syscall may use a copy-on-write (COW) strategy to improve performance. This adds references to the previous address space rather than copying all of the contents.

Process life cycle

The on-proc state is for running on a processor (CPU). The ready-to-run state is when the process is runnable but is waiting on a CPU run queue for its turn on a CPU. Most I/O will block, putting the process in the sleep state until the I/O completes and the process is woken up. The zombie state occurs during process termination, when the process waits until its process status has been reaped by the parent process or until it is removed by the kernel.

A stack is a memory storage area for temporary data, organized as a last-in, first-out (LIFO) list. It is used to store less important data than that which fits in the CPU register set. When a function is called, the return address is saved to the stack. Some registers may be saved to the stack as well if their values are needed after the call.10 When the called function has finished, it restores any required registers and, by fetching the return address from the stack, passes execution to the calling function. The stack can also be used for passing parameters to functions. The set of data on a stack related to a function’s execution is called a stack frame.

The call path to the currently executing function can be seen by examining the saved return addresses across all the stack frames in the thread’s stack (a process called stack walking).11 This call path is referred to as a stack back trace or a stack trace. In performance engineering it is often called just a “stack” for short. These stacks can answer why something is executing, and are an invaluable tool for debugging and performance analysis.


While virtual memory allows main memory to be extended using secondary storage, the kernel strives to keep the most active data in main memory. There are two kernel schemes for this:

Process swapping moves entire processes between main memory and secondary storage.

Paging moves small units of memory called pages
The scheduling of processes on processors and individual CPUs is performed by the scheduler, a key component of the operating system kernel

Workloads can be categorized as either:

CPU-bound: Applications that perform heavy compute, for example, scientific and mathematical analysis, which are expected to have long runtimes (seconds, minutes, hours, days, or even longer). These become limited by CPU resources.

I/O-bound: Applications that perform I/O, with little compute, for example, web servers, file servers, and interactive shells, where low-latency responses are desirable. When their load increases, they are limited by I/O to storage or network resources.                                                                                                                                                                                                                                                  