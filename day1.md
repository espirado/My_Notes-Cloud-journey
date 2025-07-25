# Day 1: Math Foundations & Two Pointers
**Focus: Build the foundation that 80% of array problems rely on**

## 🎯 **Today's Learning Objectives**
By end of day, you should be able to:
- Apply modular arithmetic to prevent integer overflow
- Use 4 essential bit manipulation tricks
- Recognize and implement both two-pointer patterns
- Solve Two Sum variations without thinking

---

## ⏰ **Day 1 Schedule (3-4 hours total)**

### **Morning Session (1.5 hours): Math Foundations**
- **30 min**: Modular Arithmetic + Templates
- **45 min**: Bit Manipulation + Practice
- **15 min**: Quick Review & Pattern Recognition

### **Afternoon Session (1.5-2 hours): Two Pointers Mastery**
- **45 min**: Pattern 1 - Opposite Direction Pointers
- **45 min**: Pattern 2 - Same Direction (Fast/Slow)
- **30 min**: Problem Practice

---

## 🧮 **MORNING: CRITICAL MATH CONCEPTS**

### **1. Modular Arithmetic (30 minutes)**

#### **Why This Matters**
```python
# Without modular arithmetic - OVERFLOW!
def fibonacci_wrong(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b  # This will overflow for large n
    return a

# With modular arithmetic - SAFE!
def fibonacci_safe(n):
    MOD = 10**9 + 7
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % MOD
    return a
```

#### **The 4 Essential Formulas (Memorize These)**
```python
MOD = 10**9 + 7

# Formula 1: Addition
def mod_add(a, b, mod=MOD):
    return ((a % mod) + (b % mod)) % mod

# Formula 2: Subtraction (Note the +mod to handle negatives)
def mod_sub(a, b, mod=MOD):
    return ((a % mod) - (b % mod) + mod) % mod

# Formula 3: Multiplication  
def mod_mul(a, b, mod=MOD):
    return ((a % mod) * (b % mod)) % mod

# Formula 4: Power (Use Python's built-in)
def mod_pow(base, exp, mod=MOD):
    return pow(base, exp, mod)  # This is O(log exp)
```

#### **Practice Problem: Fibonacci with Modular Arithmetic**
```python
def fibonacci_mod(n):
    """Return nth Fibonacci number modulo 10^9 + 7"""
    if n <= 1:
        return n
    
    MOD = 10**9 + 7
    a, b = 0, 1
    
    for i in range(2, n + 1):
        a, b = b, (a + b) % MOD
    
    return b

# Test it
print(fibonacci_mod(50))  # Should work without overflow
```

### **2. Bit Manipulation (45 minutes)**

#### **The Essential 4 (Master These Today)**

##### **Trick 1: Check if Power of 2**
```python
def is_power_of_2(n):
    """
    Logic: Power of 2 has only one bit set
    Example: 8 = 1000, 8-1 = 0111, 1000 & 0111 = 0000
    """
    return n > 0 and (n & (n - 1)) == 0

# Practice
print(is_power_of_2(8))   # True
print(is_power_of_2(6))   # False
print(is_power_of_2(16))  # True
```

##### **Trick 2: Count Set Bits (Brian Kernighan's Algorithm)**
```python
def count_set_bits(n):
    """
    Each iteration removes the rightmost set bit
    Much faster than checking each bit position
    """
    count = 0
    while n:
        count += 1
        n &= (n - 1)  # Remove rightmost set bit
    return count

# Practice
print(count_set_bits(7))   # 3 (binary: 111)
print(count_set_bits(8))   # 1 (binary: 1000)
```

##### **Trick 3: XOR Magic for Single Number**
```python
def single_number(nums):
    """
    Find the number that appears once when all others appear twice
    Logic: a ^ a = 0, a ^ 0 = a
    """
    result = 0
    for num in nums:
        result ^= num
    return result

# Practice
print(single_number([2, 2, 1]))        # 1
print(single_number([4, 1, 2, 1, 2]))  # 4
```

##### **Trick 4: Get/Set/Clear Specific Bit**
```python
def get_bit(n, i):
    """Check if i-th bit is set"""
    return (n & (1 << i)) != 0

def set_bit(n, i):
    """Set i-th bit to 1"""
    return n | (1 << i)

def clear_bit(n, i):
    """Set i-th bit to 0"""
    return n & ~(1 << i)

# Practice
n = 5  # binary: 101
print(get_bit(n, 0))    # True (rightmost bit)
print(get_bit(n, 1))    # False (middle bit)
print(set_bit(n, 1))    # 7 (binary: 111)
print(clear_bit(n, 2))  # 1 (binary: 001)
```

---

## 📊 **AFTERNOON: TWO POINTERS MASTERY**

### **Pattern 1: Opposite Direction Pointers (45 minutes)**

#### **When to Use**: Sorted arrays, palindromes, target sum problems

#### **Template (Memorize This)**
```python
def two_sum_sorted(nums, target):
    """
    Find two numbers that add up to target in sorted array
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1   # Need bigger sum
        else:
            right -= 1  # Need smaller sum
    
    return [-1, -1]  # Not found
```

#### **Problem 1: Two Sum (Sorted Array)**
```python
def two_sum(nums, target):
    """LeetCode 167: Two Sum II - Input array is sorted"""
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []

# Test
print(two_sum([2, 7, 11, 15], 9))  # [1, 2]
```

#### **Problem 2: Three Sum**
```python
def three_sum(nums):
    """
    LeetCode 15: Find all unique triplets that sum to 0
    Key insight: Fix first element, use two pointers for rest
    """
    nums.sort()  # Critical step
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates for first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        target = -nums[i]
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return result

# Test
print(three_sum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
```

### **Pattern 2: Same Direction (Fast/Slow) (45 minutes)**

#### **When to Use**: Remove duplicates, move elements, partition arrays

#### **Template (Memorize This)**
```python
def remove_duplicates_template(nums):
    """
    Remove duplicates in-place from sorted array
    slow: position to write next unique element
    fast: scanning through array
    """
    if not nums:
        return 0
    
    slow = 0  # Write pointer
    
    for fast in range(1, len(nums)):  # Read pointer
        if nums[fast] != nums[slow]:  # Found new unique element
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1  # Length of unique array
```

#### **Problem 1: Remove Duplicates**
```python
def remove_duplicates(nums):
    """LeetCode 26: Remove Duplicates from Sorted Array"""
    if not nums:
        return 0
    
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1

# Test
nums = [1, 1, 2, 2, 2, 3]
length = remove_duplicates(nums)
print(nums[:length])  # [1, 2, 3]
```

#### **Problem 2: Move Zeros**
```python
def move_zeros(nums):
    """
    LeetCode 283: Move all zeros to end while maintaining order
    """
    slow = 0  # Position for next non-zero element
    
    # Move all non-zero elements to front
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
    
    # Fill remaining positions with zeros
    while slow < len(nums):
        nums[slow] = 0
        slow += 1

# Test
nums = [0, 1, 0, 3, 12]
move_zeros(nums)
print(nums)  # [1, 3, 12, 0, 0]
```

---

## 🎯 **PRACTICE PROBLEMS FOR TODAY**

### **Must Solve (Core Understanding)**
1. **LeetCode 1**: Two Sum (brute force first, then optimize)
2. **LeetCode 167**: Two Sum II (sorted array)
3. **LeetCode 15**: Three Sum
4. **LeetCode 26**: Remove Duplicates from Sorted Array
5. **LeetCode 136**: Single Number (bit manipulation)

### **Additional Practice (If Time Permits)**
6. **LeetCode 283**: Move Zeros
7. **LeetCode 344**: Reverse String (two pointers)
8. **LeetCode 125**: Valid Palindrome
9. **LeetCode 342**: Power of Four (bit manipulation)

---

## ✅ **Day 1 Success Checklist**

### **Math Mastery**
- [ ] Can apply modular arithmetic to prevent overflow
- [ ] Memorized the 4 essential modular formulas
- [ ] Can solve Fibonacci with large numbers using modulo
- [ ] Can check if number is power of 2 using bit manipulation
- [ ] Can count set bits efficiently
- [ ] Can find single number using XOR properties

### **Two Pointers Mastery**
- [ ] Can identify when to use opposite vs same direction pointers
- [ ] Can solve Two Sum in O(n) time and O(1) space
- [ ] Can solve Three Sum correctly handling duplicates
- [ ] Can remove duplicates from sorted array in-place
- [ ] Can move zeros to end while maintaining order

### **Pattern Recognition**
- [ ] Immediately recognize sorted array → two pointers
- [ ] Immediately recognize "find pair/triplet" → two pointers
- [ ] Immediately recognize "remove/move elements" → fast/slow pointers
- [ ] Immediately recognize large numbers → modular arithmetic
- [ ] Immediately recognize "single element" → XOR

---

## 🔥 **Key Takeaways for Tomorrow**

1. **Two pointers solve 70% of array problems** - master the patterns
2. **Modular arithmetic prevents overflow** - always use for large numbers
3. **Bit manipulation provides O(1) optimizations** - learn the tricks
4. **Pattern recognition is key** - see the pattern, apply the template

**Tomorrow**: We'll build on these foundations with sliding window techniques and string algorithms!

---

## 💡 **Pro Tips**
- **Time yourself**: Aim to solve Two Sum in 5 minutes, Three Sum in 15 minutes
- **Code without looking**: Practice writing the templates from memory
- **Explain your approach**: Practice verbalizing your thought process
- **Handle edge cases**: Empty arrays, single elements, no solution cases

**You've got this! Day 1 is about building rock-solid foundations. Master these patterns and you're already ahead of 70% of candidates! 🚀** 