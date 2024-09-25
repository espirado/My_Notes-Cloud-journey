a process is an instance of a program in execution.
Kernel creates a new process when a user initiates a program or executes a command,and the process runs in its own virtual address space 
The kernel uses a scheduler to determine which process to run next based on a set of scheduling policies and prioroties.

Process state 
  -  state represents the current state of the process either running,sleeping,waiting or stopped

  Memory layout - describes the virtual address spaces of the process i.e text segmenent,data segment etc 

 File descriptor - represents the files or other resources that the process has open 

 process memory layout
  - in linux memory is divided into several segments 
       - text segment - contains the executable code of the process 
       - Data segment - contains global and static variables used by the process 
       - BSS segment - contains uniti,ized data for the process
       - heap segment - used for dynamic memory allocation 
       - stack segment - used to store local variables and function calls duering program execution 
       - memory-mapped file segments - used for memory mapped files which allows files to be accessed 


       process lifecycle 
         - first stage of process lifecyle creation. This involves using a system call like fork() or clone().

         fork() - creates a copy of the current process while clone creates a new process with shared resources 

         Executing the program
          - The next stage is executing the program. This involves using a system call like exec() to replace the current process memory space with a new program. The program loads into memory and its main() function is executed.Parent process calls the wait() sys call to recive exit status of the child process and clean up child resources .

          Process Termination
           - final stage is process termination which involves calling exit()

           process suspension and resumption 
             - A process may be suspended and resumed by tje kernel. Systme call that manage the suspended state are wait(),waitpid(),kill().

        Inter process communication(IPC)
          - process can communicate with each other using processes like pipe(),socket(),mmap(). 

        Zombie and orphan process 
        - A zombie process is a proces that has completed execution but still has entry in the process table. This happens when the parent process fails to call waiy() to collect the status of terminated child process. 

        you can find zombie process by ps aux . any process with a Z in the STAT column

        An orphan process is a  process that is still running but has lost its parent process. 