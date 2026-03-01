"""
COUNTING SORT ALGORITHM VISUALIZER
----------------------------------
Counting Sort is a non-comparison-based sorting algorithm that works by counting 
the frequency of each unique element in the input array. It is highly efficient 
when the range of input values (k) is not significantly larger than the number 
of elements (n).

Complexity:
- Time: O(n + k)
- Space: O(n + k)
"""

def counting_sort(arr):
    # 1. Handle the edge case of an empty array
    if not arr:
        return arr

    # 2. Determine the range of the input data
    # We need the maximum value to define the size of our 'counting' array
    max_val = max(arr)
    min_val = min(arr)
    
    # Range is necessary if the array contains negative numbers or doesn't start at 0
    # For simplicity in this visualization, we assume non-negative integers
    range_of_elements = max_val + 1
    
    # 3. Initialize the counting array with zeros
    # This array will store the frequency of each number
    count = [0] * range_of_elements
    
    print(f"Initial Array: {arr}")
    print(f"Step 1: Created count array of size {range_of_elements} (max value + 1)")

    # 4. STORE COUNT: Iterate through the input array and increment counts
    # Visualization: Filling the 'buckets'
    for num in arr:
        count[num] += 1
    
    print(f"Step 2: Frequency Count -> {count}")
    print("        (Index represents the number, Value represents how many times it appears)")

    # 5. CUMULATIVE COUNT: Modify count array to store the position of elements
    # Each element at index 'i' will now store the sum of previous counts.
    # This tells us the actual starting position of the number in the output array.
    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    print(f"Step 3: Cumulative Count -> {count}")
    print("        (Determining the output positions for each number)")

    # 6. BUILD OUTPUT: Create the resulting sorted array
    # We iterate backwards through the original array to maintain 'Stability'
    # (Stability: equal elements retain their relative order)
    output = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        current_element = arr[i]
        # The position is found in the count array (subtract 1 for 0-based indexing)
        position = count[current_element] - 1
        output[position] = current_element
        # Decrement the count so the next identical element goes to the previous spot
        count[current_element] -= 1
    
    return output

def visualize_counting_sort(name, data):
    """
    Helper to run and illustrate the sorting process with a header
    """
    print("\n" + "="*50)
    print(f"TEST CASE: {name}")
    print("="*50)
    sorted_data = counting_sort(data)
    print(f"FINAL SORTED RESULT: {sorted_data}\n")

def illustrate_concept():
    """
    Prints an ASCII illustration of how the buckets work
    """
    print("""
    ILLUSTRATION: The 'Buckets' Concept
    Input: [1, 4, 1, 2, 0]
    
    [0]  [1]  [2]  [3]  [4]  <-- Indices (The Numbers)
    ---  ---  ---  ---  ---
    |1|  |2|  |1|  |0|  |1|  <-- Values (The Counts)
    ---  ---  ---  ---  ---
      ^    ^    ^    ^    ^
     '0'  '1s' '2'  '3'  '4'
    """)

if __name__ == "__main__":
    # Illustration of the concept
    illustrate_concept()

    # Example 1: Standard small dataset
    visualize_counting_sort("Standard Dataset", [4, 2, 2, 8, 3, 3, 1])

    # Example 2: Array with many duplicates
    visualize_counting_sort("High Redundancy", [1, 1, 1, 0, 0, 2, 1])

    # Example 3: Already sorted
    visualize_counting_sort("Already Sorted", [0, 1, 2, 3, 4, 5])

    # Example 4: Large range, small size
    # Note: Counting sort is less efficient here because of the count array size
    visualize_counting_sort("Large Range", [1, 10, 2])