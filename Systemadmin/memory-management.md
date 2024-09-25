mmu - a hardware component in cpu that plays a critical role in memory managementof a process in linux.MMU translates the virtual address used by the process into physical addresses used by the hardware.

memory allocation 
  - a user keeps inputting values to the program and a linked list needs to keep adding nodes for each input value. To dynamically allocate memory the program can increase the size of the heap or stack.

  Using the heap 
   heap is a region of memory in a process virtual address space that is ued to dynamic memory allocation. In linux kernel heap is managed using two system call brk() and sbrk().

   When a program starts the kernel sets the program break. which is the end of the process data segment to a fixed addresss in memory. This marks the initial end of the heap and all memory beyond it is unallocated. The brk() can be used to set the new program break new value effectively resizing the heap. The new value must be greater or equal to the current program break and less than or equal to the maximum size of the process address space. 

   The sbrk( ) is uesd to increment a specified amount of program break effectively allocating additional memory. 

   Malloc and free 
     - Malloc is used to dynamicalluy allocate memory on heap while free is used to deallocate memory that was previously alloacted by malloc.

     Using stacks
      - Memory for the stack is allocated automatically when a new thread or process is created. 