# LeetCode #66 — Plus One

## Problem

You are given a large integer represented as an array of digits, where each `digits[i]` is the \(i\)-th digit of the integer.

The digits are ordered from **most significant to least significant**, from left to right.

Increment the large integer by one and return the resulting array of digits.

The integer does not contain any leading zeros.

---

## Example 1

### Input

`digits = [1,2,3]`

### Output

`[1,2,4]`

### Explanation

The array represents the integer `123`.

Adding one gives `123 + 1 = 124`.

Therefore, the result is `[1,2,4]`.

---

## Example 2

### Input

`digits = [4,3,2,1]`

### Output

`[4,3,2,2]`

### Explanation

The array represents the integer `4321`.

Adding one gives `4321 + 1 = 4322`.

Therefore, the result is `[4,3,2,2]`.

---

## Example 3

### Input

`digits = [9]`

### Output

`[1,0]`

### Explanation

The array represents the integer `9`.

Adding one gives `9 + 1 = 10`.

Since the result contains two digits, the output is `[1,0]`.

---

## Example 4

### Input

`digits = [9,9,9]`

### Output

`[1,0,0,0]`

### Explanation

The array represents the integer `999`.

Adding one gives `999 + 1 = 1000`.

Therefore, the result is `[1,0,0,0]`.

---

## Constraints

* `1 <= digits.length <= 100`
* `0 <= digits[i] <= 9`
* The array does not contain any leading zeros.
* The integer is represented without any leading zeros, except for the number zero itself.

---

## Approach

Use **Array Traversal and Carry Handling** to increment the number.

1. Start from the last digit of the array.
2. If the digit is less than `9`, increment it by one and return the array.
3. If the digit is `9`, change it to `0` and carry the increment to the previous digit.
4. Continue moving from right to left while the digits are `9`.
5. If every digit is `9`, add `1` at the beginning of the array.
6. Return the updated array.

---

## Complexity Analysis

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)` in the worst case when an additional leading digit is required.

Where `n` is the length of the input array.

---

## Key Concepts

* Arrays
* Array Traversal
* Carry Handling
* Arithmetic Operations
* In-Place Modification

---

## What I Learned

* How to increment a number represented as an array.
* How to handle carry propagation.
* How to process digits from right to left.
* How to handle edge cases such as all digits being `9`.
* How to perform arithmetic operations without converting the entire array into an integer.

---

## LeetCode Details

* **Problem:** #66 — Plus One
* **Difficulty:** Easy
* **Topics:** Array, Math
* **Pattern:** Digit Manipulation / Carry Propagation
