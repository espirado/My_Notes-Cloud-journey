# Week 1: Essential Math & Linear Data Structures
**FAANG Interview Focus: Quality over Quantity**

## 🎯 **This Week's Goal**
Master the mathematical foundations and linear data structures that appear in **80% of FAANG interviews**. Focus on patterns, not theory.

---

## 🧮 **INTERVIEW-CRITICAL MATHEMATICS**

### **1. Modular Arithmetic (High Priority)**
**Why it matters**: Prevents integer overflow, used in hashing, large number problems

#### **Essential Formulas**
```python
# The big 4 that solve 90% of modular problems
(a + b) % m = ((a % m) + (b % m)) % m
(a - b) % m = ((a % m) - (b % m) + m) % m  # +m prevents negative
(a * b) % m = ((a % m) * (b % m)) % m
(a^b) % m = pow(a, b, m)  # Python's built-in fast exponentiation
```

#### **Common Interview Applications**
- **Large Fibonacci numbers**: Return fib(n) % (10^9 + 7)
- **Counting problems**: Number of ways % MOD
- **Power calculations**: a^b % m efficiently

#### **Template Code**
```python
MOD = 10**9 + 7

def mod_power(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result
```

### **2. Bit Manipulation (Essential for Optimization)**
**Why it matters**: O(1) operations, memory optimization, mathematical shortcuts

#### **The 6 Critical Bit Tricks**
```python
# 1. Check if number is power of 2
def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0

# 2. Count set bits
def count_bits(n):
    count = 0
    while n:
        count += 1
        n &= (n - 1)  # Removes rightmost set bit
    return count

# 3. Get rightmost set bit
def rightmost_set_bit(n):
    return n & (-n)

# 4. Toggle i-th bit
def toggle_bit(n, i):
    return n ^ (1 << i)

# 5. XOR swap (no extra space)
def xor_swap(a, b):
    a ^= b
    b ^= a
    a ^= b
    return a, b

# 6. Check if i-th bit is set
def is_bit_set(n, i):
    return (n & (1 << i)) != 0
```

#### **Interview Pattern: XOR Properties**
```python
# Pattern: Find single number in array where all others appear twice
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num  # a ^ a = 0, a ^ 0 = a
    return result
```

### **3. Mathematical Patterns in Arrays**
**Why it matters**: Optimization techniques, prefix/suffix calculations

#### **Prefix Sums (Must Know)**
```python
# Template for range sum queries
def range_sum_query(nums):
    prefix = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]
    
    def get_range_sum(left, right):  # inclusive
        return prefix[right + 1] - prefix[left]
    
    return get_range_sum
```

#### **GCD/LCM (Common in Array Problems)**
```python
import math

def gcd_array(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result = math.gcd(result, arr[i])
    return result

def lcm(a, b):
    return (a * b) // math.gcd(a, b)
```

---

## 📊 **LINEAR DATA STRUCTURES MASTERY**

### **ARRAYS & STRINGS**

#### **1. Two Pointers Technique (70% of Array Problems)**

##### **Pattern 1: Opposite Direction Pointers**
```python
# Template for palindrome, two sum on sorted array, etc.
def two_pointers_opposite(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]
```

##### **Pattern 2: Same Direction (Fast/Slow)**
```python
# Template for removing duplicates, partition, etc.
def remove_duplicates(arr):
    if not arr:
        return 0
    
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    
    return slow + 1  # Length of unique elements
```

#### **2. Sliding Window (Essential for Substring Problems)**

##### **Fixed Size Window**
```python
# Template for fixed window problems
def max_sum_subarray(arr, k):
    if len(arr) < k:
        return -1
    
    # Calculate first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

##### **Variable Size Window**
```python
# Template for longest subarray with condition
def longest_subarray_with_sum(arr, target):
    left = 0
    current_sum = 0
    max_length = 0
    
    for right in range(len(arr)):
        current_sum += arr[right]
        
        # Shrink window if needed
        while current_sum > target and left <= right:
            current_sum -= arr[left]
            left += 1
        
        # Update max if condition met
        if current_sum == target:
            max_length = max(max_length, right - left + 1)
    
    return max_length
```

#### **3. String Algorithms (Interview Favorites)**

##### **KMP Algorithm (Advanced - Know the Concept)**
```python
# Pattern matching in O(n + m) time
def build_lps(pattern):
    """Build Longest Prefix Suffix array"""
    lps = [0] * len(pattern)
    length = 0
    i = 1
    
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    lps = build_lps(pattern)
    i = j = 0
    matches = []
    
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == len(pattern):
            matches.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return matches
```

---

### **LINKED LISTS**

#### **1. Essential Patterns**

##### **Fast/Slow Pointers (Floyd's Algorithm)**
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Pattern 1: Detect cycle
def has_cycle(head):
    if not head or not head.next:
        return False
    
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Pattern 2: Find middle element
def find_middle(head):
    if not head:
        return None
    
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

##### **Reversal Patterns**
```python
# Pattern 1: Reverse entire list
def reverse_list(head):
    prev = None
    curr = head
    
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    
    return prev

# Pattern 2: Reverse in groups
def reverse_k_group(head, k):
    # Count nodes
    count = 0
    curr = head
    while curr and count < k:
        curr = curr.next
        count += 1
    
    if count == k:
        curr = reverse_k_group(curr, k)  # Reverse rest
        
        # Reverse current group
        while count > 0:
            temp = head.next
            head.next = curr
            curr = head
            head = temp
            count -= 1
        head = curr
    
    return head
```

##### **Merge Patterns**
```python
# Merge two sorted lists
def merge_sorted_lists(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    
    # Attach remaining
    curr.next = l1 or l2
    return dummy.next
```

---

### **STACKS & QUEUES**

#### **1. Monotonic Stack (Advanced Pattern)**
```python
# Pattern: Next Greater Element
def next_greater_element(nums):
    stack = []
    result = [-1] * len(nums)
    
    for i in range(len(nums)):
        # Pop smaller elements
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    
    return result

# Pattern: Largest Rectangle in Histogram
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    index = 0
    
    while index < len(heights):
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            area = (heights[top] * 
                   ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)
    
    while stack:
        top = stack.pop()
        area = (heights[top] * 
               ((index - stack[-1] - 1) if stack else index))
        max_area = max(max_area, area)
    
    return max_area
```

#### **2. Queue Applications**
```python
from collections import deque

# Sliding Window Maximum using Deque
def max_sliding_window(nums, k):
    dq = deque()  # Store indices
    result = []
    
    for i in range(len(nums)):
        # Remove indices outside window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove smaller elements from back
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        # Add to result when window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result
```

---

## 🎯 **WEEK 1 PRACTICE STRATEGY**

### **Day 1-2: Math + Arrays**
**Focus**: Two pointers, prefix sums, bit manipulation
**Problems**: Two Sum, Three Sum, Maximum Subarray, Single Number

### **Day 3-4: Strings + Sliding Window**
**Focus**: Substring problems, character frequency
**Problems**: Longest Substring Without Repeating Characters, Minimum Window Substring

### **Day 5-6: Linked Lists**
**Focus**: Fast/slow pointers, reversal, merging
**Problems**: Reverse Linked List, Merge Two Sorted Lists, Linked List Cycle

### **Day 7: Stacks/Queues + Review**
**Focus**: Monotonic stack, deque applications
**Problems**: Valid Parentheses, Next Greater Element, Sliding Window Maximum

---

## ✅ **Week 1 Success Checklist**

### **Mathematical Skills**
- [ ] Can solve modular arithmetic problems without overflow
- [ ] Recognize when to use bit manipulation for optimization
- [ ] Apply prefix sums for range queries instantly
- [ ] Handle XOR properties for unique element problems

### **Array/String Mastery**
- [ ] Choose correct two-pointer pattern based on problem
- [ ] Implement sliding window for substring problems
- [ ] Optimize brute force solutions using mathematical insights

### **Linked List Fluency**
- [ ] Detect and handle cycles using fast/slow pointers
- [ ] Reverse linked lists iteratively and recursively
- [ ] Merge sorted lists efficiently

### **Stack/Queue Applications**
- [ ] Use monotonic stack for next/previous greater problems
- [ ] Apply deque for sliding window maximum problems
- [ ] Validate parentheses and expression evaluation

**Target**: Solve 15-20 problems this week, focusing on pattern recognition over quantity.

**Remember**: Master these patterns deeply. They form the foundation for 80% of FAANG array/string/linkedlist questions! 