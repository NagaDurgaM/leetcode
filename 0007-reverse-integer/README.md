# LeetCode #7 — Reverse Integer

## Problem

Given a signed 32-bit integer `x`, return the integer obtained by reversing its digits.

If reversing the integer causes the value to fall outside the signed 32-bit integer range, return `0`.

Assume the environment does not allow you to store 64-bit integers.

The signed 32-bit integer range is:

* Minimum: `-2³¹`
* Maximum: `2³¹ - 1`

---

## Example 1

### Input

`x = 123`

### Output

`321`

### Explanation

Reversing the digits of `123` gives `321`.

---

## Example 2

### Input

`x = -123`

### Output

`-321`

### Explanation

The negative sign is preserved, and the digits are reversed.

---

## Example 3

### Input

`x = 120`

### Output

`21`

### Explanation

Reversing `120` gives `021`.

Leading zeros are removed, so the result is `21`.

---

## Example 4

### Input

`x = 1534236469`

### Output

`0`

### Explanation

Reversing the digits produces a value outside the signed 32-bit integer range.

Therefore, the result is `0`.

---

## Constraints

* `-2³¹ <= x <= 2³¹ - 1`

---

## Approach

Use **Digit Manipulation** to reverse the integer.

1. Identify whether the number is positive or negative.
2. Extract the last digit of the number repeatedly.
3. Build the reversed number by adding each extracted digit to the next position.
4. Continue until all digits have been processed.
5. Check whether the reversed number falls within the signed 32-bit integer range.
6. If it exceeds the permitted range, return `0`.
7. Otherwise, return the reversed integer with its original sign.

---

## Complexity Analysis

* **Time Complexity:** `O(log |x|)`
* **Space Complexity:** `O(1)`

Where `x` is the input integer. The number of digits determines the number of operations.

---

## Key Concepts

* Integer Manipulation
* Mathematics
* Modulo Operation
* Integer Division
* Overflow Handling
* Signed Integers

---

## What I Learned

* How to reverse the digits of an integer.
* How to handle positive and negative numbers.
* How to remove leading zeros from a reversed number.
* How to check signed 32-bit integer boundaries.
* How to solve digit-manipulation problems with constant extra space.

---

## LeetCode Details

* **Problem:** #7 — Reverse Integer
* **Difficulty:** Medium
* **Topics:** Math
* **Pattern:** Digit Manipulation / Overflow Handling
