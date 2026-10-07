# LeetCode #35 — Search Insert Position

## Problem

Given a **sorted array** of distinct integers `nums` and a target value `target`, return the index if the target is found.

If the target is not found, return the index where it would be inserted in order.

You must write an algorithm with **O(log n)** runtime complexity.

---

## Example 1

### Input

`nums = [1,3,5,6]`

`target = 5`

### Output

`2`

### Explanation

The target `5` already exists in the array at index `2`.

---

## Example 2

### Input

`nums = [1,3,5,6]`

`target = 2`

### Output

`1`

### Explanation

`2` is not present in the array.

It should be inserted between `1` and `3`, so the correct index is `1`.

---

## Example 3

### Input

`nums = [1,3,5,6]`

`target = 7`

### Output

`4`

### Explanation

`7` is greater than every element in the array, so it should be inserted at the end.

---

## Example 4

### Input

`nums = [1,3,5,6]`

`target = 0`

### Output

`0`

### Explanation

`0` is smaller than every element, so it should be inserted at the beginning.

---

## Constraints

* `1 <= nums.length <= 10⁴`
* `-10⁴ <= nums[i] <= 10⁴`
* `nums` contains distinct values sorted in ascending order.
* `-10⁴ <= target <= 10⁴`

---

## Approach

Use **Binary Search** because the array is already sorted.

1. Set two pointers:

   * `left` at the beginning of the array.
   * `right` at the end of the array.
2. Find the middle position.
3. Compare the middle element with the target.
4. If the middle element equals the target, return its index.
5. If the target is greater, search the right half.
6. If the target is smaller, search the left half.
7. Continue until the correct position is found.
8. If the target does not exist, the `left` pointer represents the correct insertion position.

---

## Complexity Analysis

* **Time Complexity:** `O(log n)`
* **Space Complexity:** `O(1)`

Binary Search eliminates half of the remaining search space at every step.

---

## Key Concepts

* Arrays
* Binary Search
* Sorted Arrays
* Two Pointers
* Searching
* Insertion Position

---

## What I Learned

* How Binary Search works on a sorted array.
* How to find an element efficiently.
* How to determine where a missing element should be inserted.
* Why Binary Search has `O(log n)` time complexity.
* How to use left and right pointers to reduce the search space.

---

## LeetCode Details

* **Problem:** #35 — Search Insert Position
* **Difficulty:** Easy
* **Topics:** Array, Binary Search
* **Pattern:** Binary Search
