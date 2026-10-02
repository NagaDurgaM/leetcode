# LeetCode #21 — Merge Two Sorted Lists

## Problem

You are given the heads of two sorted linked lists, `list1` and `list2`.

Merge the two lists into **one sorted linked list**.

The merged list should be made by connecting the nodes of the two given lists.

Return the head of the merged linked list.

---

## Example 1

### Input

`list1 = [1,2,4]`

`list2 = [1,3,4]`

### Output

`[1,1,2,3,4,4]`

### Explanation

Both lists are already sorted.

Merge them by comparing the elements from both lists:

`1 → 1 → 2 → 3 → 4 → 4`

---

## Example 2

### Input

`list1 = []`

`list2 = []`

### Output

`[]`

### Explanation

Both linked lists are empty, so the result is also empty.

---

## Example 3

### Input

`list1 = []`

`list2 = [0]`

### Output

`[0]`

### Explanation

The first list is empty, so the result contains the elements from the second list.

---

## Constraints

* The number of nodes in both lists is in the range `[0, 50]`.
* `-100 <= Node.val <= 100`
* Both `list1` and `list2` are sorted in non-decreasing order.

---

## Approach

Use a **Two-Pointer** approach to compare the nodes of both linked lists.

1. Start with the first node of both lists.
2. Compare the values of the current nodes.
3. Add the smaller value to the merged list.
4. Move the pointer of the list from which the node was selected.
5. Continue comparing until one list reaches the end.
6. Attach the remaining nodes from the other list.
7. Return the head of the merged linked list.

---

## Complexity Analysis

* **Time Complexity:** `O(n + m)`
* **Space Complexity:** `O(1)`

Where:

* `n` = number of nodes in `list1`
* `m` = number of nodes in `list2`

The existing nodes are reused, so no additional list is required.

---

## Key Concepts

* Linked List
* Two Pointers
* Traversal
* Comparing Sorted Data
* Merging Lists
* Iteration

---

## What I Learned

* How to traverse a linked list.
* How to compare nodes from two sorted lists.
* How to merge two sorted linked lists.
* How the two-pointer technique works with linked lists.
* How to achieve `O(n + m)` time complexity with `O(1)` extra space.

---

## LeetCode Details

* **Problem:** #21 — Merge Two Sorted Lists
* **Difficulty:** Easy
* **Topics:** Linked List, Recursion
* **Pattern:** Two Pointers / Merge
