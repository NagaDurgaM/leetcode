# LeetCode #9 - Palindrome Number

## Problem

Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

A palindrome number reads the same **forward and backward**.

---

## Example 1

**Input:**

```text
x = 121
```

**Output:**

```text
true
```

**Explanation:**

```text
121 → 121
```

The number is the same when read forward and backward.

---

## Example 2

**Input:**

```text
x = -121
```

**Output:**

```text
false
```

**Explanation:**

```text
-121 → 121-
```

The number is not the same when reversed.

---

## Example 3

**Input:**

```text
x = 10
```

**Output:**

```text
false
```

**Explanation:**

```text
10 → 01
```

The number is not the same when reversed.

---

## Approach

Instead of reversing the entire number, reverse **only half of the digits**.

* Negative numbers are not palindromes.
* Numbers ending in `0` are not palindromes, except `0` itself.
* Reverse the second half of the number.
* Compare the first half with the reversed half.
* For numbers with an odd number of digits, ignore the middle digit.

---

## Complexity

**Time Complexity:** `O(log n)`

**Space Complexity:** `O(1)`

---

## Concepts Used

* Numbers
* Modulus `%`
* Integer Division `//`
* While Loop
* Number Reversal
* Palindrome
* Edge Cases
* Time Complexity
* Space Complexity

---

## Important Cases

* Positive palindrome → `121`
* Negative number → `-121`
* Number ending in `0` → `10`
* Single digit → `7`
* Zero → `0`

---

## LeetCode Details

| Detail     | Value             |
| ---------- | ----------------- |
| Problem    | Palindrome Number |
| Number     | #9                |
| Difficulty | Easy              |
| Topic      | Math              |

---

## Author

**Naga Durga Lakshmi**

GitHub: [NagaDurgaM](https://github.com/NagaDurgaM)

LinkedIn: [Naga Durga Lakshmi](https://www.linkedin.com/in/nagadurgalakshmimetti/)
