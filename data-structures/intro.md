Bio O

Big O time is the language and metric we use to describe the efficiency of algorithms.
Electronic Transfer: 0( s ), where s is the size of the file. This means that the time to transfer the file
increases linearly with the size of the file. (Yes, this is a bit of a simplification, but that's okay for these
purposes.)

Airplane Transfer: 0( 1) with respect to the size of the file. As the size of the file increases, it won't take
any longer to get the file to your friend. The time is constant

   use big 0, big 0 (theta), and big O (omega) to describe runtimes.
           O (big 0): In academia, big O describes an upper bound on the time. An algorithm that prints all the
values in an array could be described as O(N), but it could also be described as O(N 2 ), O(N 3 ), or 0( 2 N )
(or many other big O times). Basically any value above 0(N)

0 (big omega): In academia, 0 is the equivalent concept but for lower bound. Printing the values in
an array is O(N) as well as O(log N) and 0(1). After all, you know that it won't be faster than those
runtimes

0 (big theta): In academia, e means both O
0( N). 0 gives a tight bound on runtime.

Best Case: If all elements are equal, then quick sort will, on average, just traverse through the array once.
This is O ( N). (This actually depends slightly on the implementation of quick sort. There are implementa­
tions, though, that will run very quickly on a sorted array.


Worst Case: What if we get really unlucky and the pivot is repeatedly
the biggest element in the array?
(Actually, this can easily happen. If the pivot is chosen to be the first element in the subarray and the
array is sorted in reverse order, we'll have this situation.) In this case, our recursion doesn't divide the
array in half and recurse on each half. It just shrinks the subarray by one element. This will degenerate
to anO(N 2 ) runtime

Expected Case: Usually,
though, these wonderful or terrible situations won't happen. Sure, sometimes
the pivot will be very low or very high, but it won't happen over and over again. We can expect a runtime
ofO(N log N)


Objectives of algorithms and data structures
Communicating solution to others
       a)Prove Correctness of solution
       b)Argue Efficiency of solution