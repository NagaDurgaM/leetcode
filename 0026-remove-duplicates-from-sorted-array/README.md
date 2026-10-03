# LeetCode #26 — Remove Duplicates from Sorted Array

## Problem

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only once.

Return the number of unique elements in `nums`.

The relative order of the elements should be maintained.

---

## Example 1

### Input

`nums = [1,1,2]`

### Output

`2`

### Explanation

After removing duplicates, the array becomes:

`[1,2,_]`

There are **2 unique elements**.

---

## Example 2

### Input

`nums = [0,0,1,1,1,2,2,3,3,4]`

### Output

`5`

### Explanation

After removing duplicates, the array becomes:

`[0,1,2,3,4,_,_,_,_,_]`

There are **5 unique elements**.

---

## Constraints

* `1 <= nums.length <= 3 * 10⁴`
* `-100 <= nums[i] <= 100`
* `nums` is sorted in non-decreasing order.

---

## Approach

Use the **Two-Pointer** technique.

Since the array is already sorted, duplicate values will always appear next to each other.

1. Keep one pointer for the position where the next unique element should be placed.
2. Use another pointer to traverse the array.
3. Compare the current element with the previous unique element.
4. If the element is different, it is a unique value.
5. Place the unique value at the next available position.
6. Continue until the entire array is processed.
7. Return the number of unique elements.

---

## Complexity Analysis

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

The array is modified **in-place**, so no additional array is required.

---

## Key Concepts

* Arrays
* Two Pointers
* In-Place Modification
* Sorted Arrays
* Duplicate Removal
* Array Traversal

---

## What I Learned

* How to remove duplicates from a sorted array.
* How the **Two-Pointer** technique works.
* How to modify an array in-place.
* How sorted data can simplify duplicate detection.
* How to achieve `O(n)` time with `O(1)` extra space.

---

## LeetCode Details

* **Problem:** #26 — Remove Duplicates from Sorted Array
* **Difficulty:** Easy
* **Topics:** Array, Two Pointers
* **Pattern:** Two Pointers / In-Place Array
