<h1 align="center">Counting Sort</h1>

## Overview

**Counting Sort** is a non-comparison sorting algorithm that sorts elements by counting how many times each value appears.

Instead of comparing elements like quicksort or merge sort, it uses the values themselves as indexes in a counting array.

It is known for being:

* ✅ Very fast for small integer ranges
* ✅ Stable when implemented properly
* ✅ O(n + k) time complexity
* ❌ Works only with integers (or values that can be mapped to integers)
* ❌ Inefficient when the value range is very large

*(Here, `n` = number of elements, `k` = range of values)*

<a href="/src/main.py">Check out for source code</a>

---

## ⚙️ How Counting Sort Works

Counting Sort follows these steps:

1. Find the maximum value in the array
2. Create a counting array of size `max + 1`
3. Count how many times each number appears
4. Compute cumulative counts (positions)
5. Place elements into the output array in sorted order

---

### Example Walkthrough

Sort this list:

```
[4, 2, 2, 8, 3, 3, 1]
```

#### Step 1 — Count occurrences

```
Value:   0 1 2 3 4 5 6 7 8
Count:   0 1 2 2 1 0 0 0 1
```

#### Step 2 — Build cumulative counts

```
Value:   0 1 2 3 4 5 6 7 8
Count:   0 1 3 5 6 6 6 6 7
```

#### Step 3 — Build sorted output

```
[1, 2, 2, 3, 3, 4, 8]
```

---

## ⏱️ Time & Space Complexity

| Case  | Complexity |
| ----- | ---------- |
| Time  | O(n + k)   |
| Space | O(k)       |

Counting Sort is extremely fast when `k` (value range) is small.

---

## 🧠 Python Implementation

```python
def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)

    # Create counting array
    count = [0] * (max_val + 1)

    # Count occurrences
    for num in arr:
        count[num] += 1

    # Build sorted array
    output = []
    for i in range(len(count)):
        output.extend([i] * count[i])

    return output


# Example usage
numbers = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(numbers))
# Output: [1, 2, 2, 3, 3, 4, 8]
```

---

## 🧪 Example Runs

### Example 1

Input:

```
[1, 4, 1, 2, 7, 5, 2]
```

Output:

```
[1, 1, 2, 2, 4, 5, 7]
```

### Example 2

Input:

```
[9, 6, 3, 6, 2, 1]
```

Output:

```
[1, 2, 3, 6, 6, 9]
```

---

## 👍 Advantages

* Extremely fast for small ranges
* No comparisons required
* Stable sorting algorithm (when using prefix sums placement)
* Simple concept

---

## 👎 Disadvantages

* Requires extra memory
* Not suitable for large value ranges
* Only works with integers or mapped values

---

## 📌 When to Use Counting Sort

Use Counting Sort when:

* Values are small integers
* The range of numbers is limited
* You need linear-time sorting
* Stability is required

Common uses include:

* Sorting exam scores
* Sorting ages or small IDs
* As a subroutine in Radix Sort

---

## 🏁 Summary

Counting Sort is one of the fastest sorting algorithms when the input values fall within a small range. While it is not suitable for every dataset, its linear performance makes it extremely powerful in the right situations.
