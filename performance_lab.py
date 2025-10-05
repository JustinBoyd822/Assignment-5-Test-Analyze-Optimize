# 🔍 Problem 1: Find Most Frequent Element
def most_frequent(numbers):
    """
    Find the most frequently occurring element in a list.
    If there's a tie, return any of the most frequent.
    """
    if not numbers:
        return None
    
    # Count frequency of each number using a dictionary
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    
    # Find the number with maximum frequency
    max_count = 0
    most_freq = None
    for num, count in frequency.items():
        if count > max_count:
            max_count = count
            most_freq = num
    
    return most_freq

# Test cases for Problem 1
def test_most_frequent():
    print("Testing Problem 1: Most Frequent Element")
    assert most_frequent([1, 3, 2, 3, 4, 1, 3]) == 3
    assert most_frequent([5, 5, 5, 1, 1]) == 5
    assert most_frequent([7]) == 7
    assert most_frequent([1, 1, 2, 2, 3, 3]) in [1, 2, 3]  # Tie case
    assert most_frequent([]) == None  # Edge case: empty list
    assert most_frequent([10, 20, 10, 30, 10]) == 10
    print("✓ All tests passed for Problem 1!\n")

test_most_frequent()

"""
Time and Space Analysis for problem 1:
- Best-case: O(n) - Even if all elements are the same, we still iterate through all n elements once
- Worst-case: O(n) - We iterate through the list once to count (O(n)) and through the dictionary once to find max (O(n))
- Average-case: O(n) - Linear time regardless of input distribution
- Space complexity: O(k) where k is the number of unique elements. Worst case O(n) if all elements are unique
- Why this approach? Dictionary provides O(1) average-case lookup and insertion, making counting efficient
- Could it be optimized? We could use Python's Counter class for cleaner code, but complexity remains the same.
  We could also find the max while counting in a single pass, reducing to one iteration instead of two.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
def remove_duplicates(nums):
    """
    Remove duplicates from a list while preserving the original order.
    """
    seen = set()
    result = []
    
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    
    return result

# Test cases for Problem 2
def test_remove_duplicates():
    print("Testing Problem 2: Remove Duplicates")
    assert remove_duplicates([4, 5, 4, 6, 5, 7]) == [4, 5, 6, 7]
    assert remove_duplicates([1, 1, 1, 1]) == [1]
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert remove_duplicates([]) == []  # Edge case: empty list
    assert remove_duplicates([5]) == [5]  # Edge case: single element
    assert remove_duplicates([3, 1, 2, 3, 1, 2]) == [3, 1, 2]
    print("✓ All tests passed for Problem 2!\n")

test_remove_duplicates()

"""
Time and Space Analysis for problem 2:
- Best-case: O(n) - Must check every element even if no duplicates exist
- Worst-case: O(n) - Single pass through the list with O(1) set lookups
- Average-case: O(n) - Linear time for any input
- Space complexity: O(n) - In worst case, the 'seen' set and 'result' list both store n elements (when no duplicates)
- Why this approach? Set provides O(1) average lookup to check if we've seen an element. List maintains insertion order.
- Could it be optimized? Could use dict.fromkeys() which preserves order in Python 3.7+, but complexity is the same.
  Trade-off: Using a set + list uses more space but is very readable and efficient.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
def find_pairs(nums, target):
    """
    Find all unique pairs of numbers that sum to the target value.
    Assumes no duplicate values in input list.
    """
    seen = set()
    pairs = []
    
    for num in nums:
        complement = target - num
        if complement in seen:
            # Add pair in sorted order to ensure uniqueness
            pairs.append(tuple(sorted([num, complement])))
        seen.add(num)
    
    return pairs

# Test cases for Problem 3
def test_find_pairs():
    print("Testing Problem 3: Find Pairs That Sum to Target")
    assert set(find_pairs([1, 2, 3, 4], 5)) == {(1, 4), (2, 3)}
    assert find_pairs([1, 2, 3], 10) == []  # No pairs sum to target
    assert find_pairs([5, 5], 10) == []  # Assumes no duplicates in input
    assert find_pairs([1], 2) == []  # Single element
    assert find_pairs([], 5) == []  # Empty list
    assert set(find_pairs([0, 1, 2, 3, 4, 5], 5)) == {(0, 5), (1, 4), (2, 3)}
    assert find_pairs([10, 20, 30], 50) == [(20, 30)]
    print("✓ All tests passed for Problem 3!\n")

test_find_pairs()

"""
Time and Space Analysis for problem 3:
- Best-case: O(n) - Must check every element even if no pairs exist
- Worst-case: O(n) - Single pass through list with O(1) set operations
- Average-case: O(n) - Linear time complexity
- Space complexity: O(n) - The 'seen' set stores up to n elements, pairs list stores at most n/2 tuples
- Why this approach? Using a set allows O(1) lookups to check if complement exists. This is much better than
  nested loops which would be O(n²).
- Could it be optimized? Space-wise, we could sort the array first O(n log n) and use two pointers O(n),
  which would be O(n log n) time but O(1) extra space. However, for most cases, O(n) time is better than O(n log n).
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
def add_n_items(n):
    """
    Simulate adding n items to a dynamic list with capacity doubling.
    Prints when resizing occurs.
    """
    capacity = 1
    size = 0
    simulated_list = []
    
    print(f"Starting with capacity: {capacity}")
    
    for i in range(n):
        # Check if we need to resize
        if size >= capacity:
            old_capacity = capacity
            capacity *= 2
            print(f"  → Resizing from {old_capacity} to {capacity} (copying {size} elements)")
            # Simulate copying by creating new list
            simulated_list = simulated_list[:]  # Creates a copy
        
        simulated_list.append(i)
        size += 1
        print(f"Added item {i}, size: {size}/{capacity}")
    
    print(f"\nFinal size: {size}, Final capacity: {capacity}")
    return simulated_list

# Test Problem 4
def test_add_n_items():
    print("Testing Problem 4: Simulate List Resizing\n")
    add_n_items(10)
    print("\n✓ Problem 4 complete!\n")

test_add_n_items()

"""
Time and Space Analysis for problem 4:
- When do resizes happen? Resizes occur when size reaches capacity (at sizes 1, 2, 4, 8, 16, 32, etc.)
- What is the worst-case for a single append? O(n) when a resize is needed, because we must copy all n elements
- What is the amortized time per append overall? O(1) - Even though individual appends can cost O(n), 
  most appends are O(1). Over n operations, total cost is n + (1 + 2 + 4 + ... + n/2) ≈ 2n = O(n), 
  so average per operation is O(n)/n = O(1)
- Space complexity: O(n) where n is the number of elements. At any time, we use at most 2n space 
  (n elements in old array during resize, before it's freed)
- Why does doubling reduce the cost overall? Doubling means resizes happen less frequently (logarithmically).
  If we only increased by 1 each time, we'd resize on every operation, making it O(n²) total.
  Doubling creates geometric growth, spreading the resize cost across many cheap operations.
"""


# 🔍 Problem 5: Compute Running Totals
def running_total(nums):
    """
    Compute running totals where each element is the sum of all elements up to that index.
    """
    if not nums:
        return []
    
    result = []
    current_sum = 0
    
    for num in nums:
        current_sum += num
        result.append(current_sum)
    
    return result

# Test cases for Problem 5
def test_running_total():
    print("Testing Problem 5: Running Totals")
    assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_total([5]) == [5]
    assert running_total([]) == []  # Empty list
    assert running_total([10, -5, 3, -2]) == [10, 5, 8, 6]
    assert running_total([0, 0, 0]) == [0, 0, 0]
    assert running_total([100, 200, 300]) == [100, 300, 600]
    print("✓ All tests passed for Problem 5!\n")

test_running_total()

"""
Time and Space Analysis for problem 5:
- Best-case: O(n) - Must process every element regardless of input
- Worst-case: O(n) - Single pass through the list
- Average-case: O(n) - Linear time for any input
- Space complexity: O(n) - Result list stores n elements. We also use O(1) for the current_sum variable
- Why this approach? Maintaining a running sum is efficient because each element only needs one addition.
  This avoids recalculating sums from scratch for each position (which would be O(n²))
- Could it be optimized? This is already optimal for time O(n) and necessary space O(n) for output.
  We could do it in-place if we're allowed to modify the input list, saving the extra O(n) space,
  but that changes the input which is usually undesirable. There's no way to improve time complexity below O(n).
"""


# 🔄 OPTIMIZATION: Problem 1 Refactored
def most_frequent_optimized(numbers):
    """
    Optimized version that finds max frequency in a single pass while counting.
    """
    if not numbers:
        return None
    
    frequency = {}
    max_count = 0
    most_freq = None
    
    # Count and track max in single pass
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
        if frequency[num] > max_count:
            max_count = frequency[num]
            most_freq = num
    
    return most_freq

# Test optimized version
def test_most_frequent_optimized():
    print("Testing Optimized Problem 1")
    assert most_frequent_optimized([1, 3, 2, 3, 4, 1, 3]) == 3
    assert most_frequent_optimized([5, 5, 5, 1, 1]) == 5
    assert most_frequent_optimized([]) == None
    print("✓ Optimized version works!\n")

test_most_frequent_optimized()

"""
OPTIMIZATION COMPARISON FOR PROBLEM 1:

Original approach:
- Two passes: one to count frequencies, one to find maximum
- Time: O(n) for counting + O(k) for finding max = O(n) where k ≤ n
- Space: O(k) for frequency dictionary

Optimized approach:
- Single pass: count and track maximum simultaneously
- Time: O(n) - only one iteration through the list
- Space: O(k) - same space for frequency dictionary

Performance improvement:
- Reduced from 2 passes to 1 pass through the data
- Time complexity class remains O(n), but constant factor is better (roughly 2x faster in practice)
- Space complexity unchanged at O(k)
- More efficient when dealing with very large lists since we touch each element once

Trade-offs:
- Slightly more complex logic (tracking max while counting)
- Minimal benefit for small lists where the difference is negligible
- For very large datasets, the single-pass optimization reduces cache misses and is noticeably faster
- Code readability is slightly reduced but still maintainable
"""

print("\n" + "="*50)
print("ALL PROBLEMS COMPLETED SUCCESSFULLY!")
print("="*50)
