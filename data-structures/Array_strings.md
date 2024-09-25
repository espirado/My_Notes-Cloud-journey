// Hash Tables 
   - Map  key to value for high efficient lookup 
     -  compute the key's hash code,we use linked list and hash code function. two different keys might have the same hash codes.
     - We map the hash codes to index of array could be done with something like keys % len_array. Two different hash codes could map to same index
     - At index there is a linked list of keys and values. Store the key and value in th index. we must use a linked list because of collisions. You could have different keys with same hash code or different hash codes that map to the same index.
     - High collision O(N) where N is the number of keys. Minimum collisions O(1)
     - With binary search tree gives O(log N)

     //ArrayList&Resizable Arrays 
      - also called list in some languages
      - Will grow as you append items
      - In Java array size cant change once created
