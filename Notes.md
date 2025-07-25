# 8-Week FAANG Interview Preparation Guide
**Target: Meta, Google, Amazon, Netflix, Apple Level Problems**

## Overview
By the end of 8 weeks, you should be able to:
- Solve medium/hard problems without reference
- Write optimal code without looking up syntax
- Recognize patterns instantly
- Handle behavioral and system design questions
- Think through edge cases systematically

---

## 📚 **CORE MATHEMATICAL FOUNDATIONS**

### **Number Theory & Arithmetic**
- **Modular Arithmetic**: `(a + b) % m = ((a % m) + (b % m)) % m`
- **GCD/LCM**: Euclidean algorithm, relationship `gcd(a,b) * lcm(a,b) = a * b`
- **Prime Numbers**: Sieve of Eratosthenes, prime factorization
- **Fast Exponentiation**: `a^n` in O(log n) time
- **Fibonacci Sequence**: Matrix exponentiation, golden ratio

### **Combinatorics & Probability**
- **Permutations**: P(n,r) = n!/(n-r)!
- **Combinations**: C(n,r) = n!/(r!(n-r)!)
- **Catalan Numbers**: Binary trees, valid parentheses
- **Pigeonhole Principle**: Collision detection, duplicate finding
- **Expected Value**: For probabilistic algorithms

### **Bit Manipulation Essentials**
- **Basic Operations**: AND(&), OR(|), XOR(^), NOT(~), shifts(<<, >>)
- **Common Tricks**: 
  - `x & (x-1)` removes rightmost set bit
  - `x & -x` isolates rightmost set bit
  - `x ^ x = 0`, `x ^ 0 = x`
- **Applications**: Subset generation, single number problems

### **Logarithms & Complexity**
- **Log Properties**: log(ab) = log(a) + log(b), log(a^b) = b*log(a)
- **Time Complexity**: Understanding log n, n log n patterns
- **Binary Search Applications**: Beyond sorted arrays

---

## 🏗️ **DATA STRUCTURES MASTERY**

### **Week 1-2: Linear Data Structures**
#### **Arrays & Strings**
- **Techniques**: Two pointers, sliding window, prefix sums
- **Common Problems**: Subarray sum, palindromes, anagrams
- **Advanced**: Kadane's algorithm, Dutch national flag

#### **Linked Lists**
- **Operations**: Reversal, cycle detection, merging
- **Patterns**: Fast/slow pointers, dummy nodes
- **Advanced**: Skip lists, LRU cache implementation

#### **Stacks & Queues**
- **Applications**: Expression evaluation, monotonic stacks
- **Patterns**: Next greater element, sliding window maximum
- **Advanced**: Deque, priority queues

### **Week 3-4: Hierarchical Structures**
#### **Binary Trees**
- **Traversals**: Inorder, preorder, postorder (iterative & recursive)
- **Properties**: Height, diameter, path sums
- **Advanced**: Serialize/deserialize, lowest common ancestor

#### **Binary Search Trees**
- **Operations**: Insert, delete, search, validate
- **Advanced**: Balanced BSTs (AVL, Red-Black concepts)

#### **Tries (Prefix Trees)**
- **Applications**: Autocomplete, word search, prefix matching
- **Advanced**: Compressed tries, suffix trees

#### **Heaps**
- **Implementation**: Min/Max heaps, heapify operations
- **Applications**: Priority queues, top K problems, median finding
- **Advanced**: Fibonacci heaps (concept)

### **Week 5-6: Graph Structures**
#### **Graph Representations**
- **Adjacency List vs Matrix**: Trade-offs and use cases
- **Weighted vs Unweighted**: Algorithm implications

#### **Graph Traversal**
- **DFS**: Recursive and iterative, cycle detection
- **BFS**: Level-order, shortest path in unweighted graphs
- **Applications**: Connected components, topological sort

#### **Advanced Graph Algorithms**
- **Shortest Path**: Dijkstra's, Bellman-Ford, Floyd-Warshall
- **Minimum Spanning Tree**: Kruskal's, Prim's algorithms
- **Network Flow**: Max flow concepts (for advanced problems)

### **Week 7: Advanced Structures**
#### **Union-Find (Disjoint Set)**
- **Operations**: Find with path compression, union by rank
- **Applications**: Cycle detection, connected components, Kruskal's

#### **Segment Trees & Fenwick Trees**
- **Use Cases**: Range queries, range updates
- **Applications**: Sum/min/max queries in O(log n)

---

## 🧠 **ALGORITHMIC PARADIGMS**

### **Week 1-2: Fundamental Techniques**
#### **Sorting & Searching**
- **Comparison Sorts**: Quick, merge, heap sort - O(n log n)
- **Non-comparison**: Counting, radix, bucket sort
- **Binary Search**: Template, search space reduction
- **Applications**: First/last occurrence, peak finding

#### **Two Pointers & Sliding Window**
- **Two Pointers**: Same/opposite direction, 3Sum, trapping water
- **Sliding Window**: Fixed/variable size, substring problems
- **Fast/Slow Pointers**: Cycle detection, middle element

### **Week 3-4: Divide & Conquer**
- **Paradigm**: Divide, conquer, combine
- **Examples**: Merge sort, binary search, closest pair
- **Advanced**: Master theorem for complexity analysis

### **Week 5-6: Dynamic Programming**
#### **DP Fundamentals**
- **Memoization vs Tabulation**: Top-down vs bottom-up
- **State Definition**: What does dp[i] represent?
- **Transition**: How to build current state from previous states

#### **Classic DP Patterns**
- **Linear DP**: Fibonacci, house robber, coin change
- **2D DP**: Edit distance, longest common subsequence
- **Interval DP**: Matrix chain multiplication, palindrome partitioning
- **Tree DP**: Diameter, maximum path sum
- **Bitmask DP**: Traveling salesman, subset problems

#### **Advanced DP**
- **State Space Reduction**: Rolling array, space optimization
- **DP on Graphs**: Shortest paths with constraints
- **Digit DP**: Numbers with specific properties

### **Week 7: Greedy Algorithms**
- **Paradigm**: Local optimal choices → global optimal
- **Proof Techniques**: Exchange argument, greedy stays ahead
- **Examples**: Activity selection, Huffman coding, minimum coins
- **When Greedy Works**: Matroid theory (conceptual understanding)

### **Week 8: Backtracking**
- **Template**: Choose, explore, unchoose
- **Pruning**: Early termination for efficiency
- **Examples**: N-Queens, sudoku solver, permutations
- **Advanced**: Branch and bound, alpha-beta pruning

---

## 🎯 **PROBLEM-SOLVING PATTERNS**

### **Pattern Recognition Checklist**
1. **Array/String Problems**
   - Two pointers for sorted arrays
   - Sliding window for subarrays/substrings
   - Hash map for frequency/lookup
   - Prefix sums for range queries

2. **Tree Problems**
   - DFS for path-related problems
   - BFS for level-by-level processing
   - Post-order for bottom-up calculations
   - In-order for BST properties

3. **Graph Problems**
   - DFS for connected components/cycles
   - BFS for shortest path (unweighted)
   - Topological sort for dependencies
   - Union-Find for connectivity

4. **DP Problems**
   - Optimization problems (min/max)
   - Counting problems
   - Decision problems (possible/not possible)
   - Look for overlapping subproblems

### **Common Problem Templates**

#### **Binary Search Template**
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

#### **DFS Template**
```python
def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)
    # Process node
    for neighbor in node.neighbors:
        dfs(neighbor, visited)
```

#### **DP Template**
```python
def dp_problem(n):
    # Step 1: Define state
    dp = [0] * (n + 1)
    # Step 2: Base case
    dp[0] = base_value
    # Step 3: Transition
    for i in range(1, n + 1):
        dp[i] = transition_function(dp, i)
    return dp[n]
```

---

## 📅 **8-WEEK STUDY SCHEDULE**

### **Week 1: Arrays, Strings, Two Pointers**
- **Days 1-2**: Array manipulation, prefix sums
- **Days 3-4**: String algorithms, KMP (optional)
- **Days 5-7**: Two pointers, sliding window problems
- **Practice**: 15-20 LeetCode problems

### **Week 2: Linked Lists, Stacks, Queues**
- **Days 1-3**: Linked list operations and patterns
- **Days 4-5**: Stack applications, monotonic stack
- **Days 6-7**: Queue, deque, and circular structures
- **Practice**: 15-20 LeetCode problems

### **Week 3: Trees and Tree Algorithms**
- **Days 1-2**: Binary tree traversals and properties
- **Days 3-4**: Binary search trees
- **Days 5-6**: Tree DP and advanced problems
- **Day 7**: Review and harder tree problems
- **Practice**: 20-25 LeetCode problems

### **Week 4: More Trees and Heaps**
- **Days 1-2**: Tries and string matching
- **Days 3-4**: Heaps and priority queues
- **Days 5-7**: Advanced tree problems, LCA, serialization
- **Practice**: 20-25 LeetCode problems

### **Week 5: Graphs**
- **Days 1-2**: Graph representations, DFS, BFS
- **Days 3-4**: Shortest path algorithms
- **Days 5-6**: Topological sort, cycle detection
- **Day 7**: Advanced graph problems
- **Practice**: 20-25 LeetCode problems

### **Week 6: Dynamic Programming**
- **Days 1-2**: Basic DP, memoization vs tabulation
- **Days 3-4**: 2D DP, string DP
- **Days 5-6**: Advanced DP patterns
- **Day 7**: DP optimization techniques
- **Practice**: 25-30 LeetCode problems

### **Week 7: Advanced Topics**
- **Days 1-2**: Union-Find, segment trees
- **Days 3-4**: Greedy algorithms
- **Days 5-7**: Backtracking and advanced problems
- **Practice**: 20-25 LeetCode problems

### **Week 8: Mock Interviews and Review**
- **Days 1-3**: Daily mock interviews (2-3 problems each)
- **Days 4-5**: Review weak areas
- **Days 6-7**: Final mock interviews, system design basics
- **Practice**: Focus on timed problem solving

---

## 🎯 **FAANG-SPECIFIC PREPARATION**

### **Behavioral Questions (STAR Method)**
- **Leadership**: "Tell me about a time you led a project"
- **Conflict Resolution**: "Describe a disagreement with a colleague"
- **Failure**: "Tell me about your biggest failure"
- **Innovation**: "Describe a time you had to think outside the box"

### **System Design Basics** (for Senior roles)
- **Scalability**: Load balancing, caching, database sharding
- **Reliability**: Redundancy, failover, circuit breakers
- **Consistency**: CAP theorem, eventual consistency
- **Common Systems**: URL shortener, chat system, social media feed

### **Company-Specific Focus**
- **Google**: Algorithms, math-heavy problems, clean code
- **Meta**: Behavioral (culture fit), medium-hard algorithms
- **Amazon**: Leadership principles, system design, optimization
- **Apple**: Clean code, attention to detail, hardware-software integration
- **Netflix**: Scalability, real-time systems, A/B testing

---

## 🔧 **PRACTICE STRATEGY**

### **Daily Routine**
1. **Morning (1-2 hours)**: New concept learning
2. **Afternoon (1-2 hours)**: Problem solving practice
3. **Evening (30 minutes)**: Review and pattern recognition

### **Problem Selection Strategy**
- **Easy**: 20% (for confidence and speed)
- **Medium**: 60% (core interview level)
- **Hard**: 20% (for advanced pattern recognition)

### **Progress Tracking**
- **Week 1-2**: Focus on correctness
- **Week 3-4**: Optimize for time complexity
- **Week 5-6**: Optimize for space complexity
- **Week 7-8**: Solve under time pressure (45 minutes per problem)

### **Mock Interview Schedule**
- **Week 4**: First mock interview
- **Week 6**: Second mock interview  
- **Week 8**: Daily mock interviews (final week)

---

## 📈 **SUCCESS METRICS**

### **Technical Skills**
- [ ] Can solve 80% of medium problems in 30 minutes
- [ ] Can solve 40% of hard problems in 45 minutes
- [ ] Can optimize solutions for both time and space
- [ ] Can explain approach clearly before coding
- [ ] Can handle follow-up questions and variations

### **Soft Skills**
- [ ] Can communicate thought process clearly
- [ ] Can handle hints and feedback gracefully
- [ ] Can manage time effectively during interviews
- [ ] Can stay calm under pressure
- [ ] Can ask clarifying questions when needed

**Remember**: Consistency beats intensity. Practice daily, review patterns, and simulate real interview conditions!