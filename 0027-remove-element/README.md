# LeetCode #27 — Remove Element

## Problem

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` **in-place**.

The order of the remaining elements may be changed.

Return the number of elements in `nums` that are not equal to `val`.

---

## Example 1

### Input

`nums = [3,2,2,3]`

`val = 3`

### Output

`2`

### Explanation

Remove all occurrences of `3`.

The array becomes:

`[2,2,_,_]`

There are **2 elements** that are not equal to `3`.

---

## Example 2

### Input

`nums = [0,1,2,2,3,0,4,2]`

`val = 2`

### Output

`5`

### Explanation

Remove all occurrences of `2`.

The remaining elements are:

`[0,1,3,0,4,_,_,_]`

There are **5 elements** that are not equal to `2`.

---

## Constraints

* `0 <= nums.length <= 100`
* `0 <= nums[i] <= 50`
* `0 <= val <= 100`

---

## Approach

Use the **Two-Pointer** technique to modify the array in-place.

1. Start with a pointer that represents the position where the next valid element should be placed.
2. Traverse every element in the array.
3. If the current element is **not equal** to `val`, place it at the next available position.
4. Move the position pointer forward.
5. Ignore elements that are equal to `val`.
6. After processing the entire array, return the number of remaining valid elements.

---

## Complexity Analysis

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

The array is modified in-place, so no additional array is required.

---

## Key Concepts

* Arrays
* Two Pointers
* In-Place Modification
* Array Traversal
* Filtering Elements

---

## What I Learned

* How to remove specific elements from an array.
* How to use the **Two-Pointer** technique.
* How to modify an array in-place.
* How to filter unwanted elements efficiently.
* How to achieve `O(n)` time complexity with `O(1)` extra space.

---

## LeetCode Details

* **Problem:** #27 — Remove Element
* **Difficulty:** Easy
* **Topics:** Array, Two Pointers
* **Pattern:** Two Pointers / In-Place Array
