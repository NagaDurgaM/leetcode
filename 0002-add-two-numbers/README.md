# LeetCode #2 - Add Two Numbers

## Problem

You are given two **non-empty linked lists** representing two non-negative integers.

The digits are stored in **reverse order**. Add the two numbers and return the result as a linked list.

---

## Example 1

**Input:**

```text
l1 = [2,4,3]
l2 = [5,6,4]
```

**Output:**

```text
[7,0,8]
```

**Explanation:**

```text
342 + 465 = 807
```

Since the digits are stored in reverse order:

```text
807 → [7,0,8]
```

---

## Example 2

**Input:**

```text
l1 = [0]
l2 = [0]
```

**Output:**

```text
[0]
```

---

## Example 3

**Input:**

```text
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
```

**Output:**

```text
[8,9,9,9,0,0,0,1]
```

---

## Approach

Add the numbers **digit by digit** while keeping track of the carry.

* Start from the first node of both linked lists.
* Add the two digits.
* Add the previous `carry`.
* Store the resulting digit.
* Move to the next nodes.
* Continue until both lists are completely processed.
* Add the final carry if one remains.

---

## Complexity

**Time Complexity:** `O(n)`

**Space Complexity:** `O(n)`

Where `n` is the length of the longer linked list.

---

## Conc
