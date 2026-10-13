# LeetCode #6 — Zigzag Conversion

## Problem

The string `"PAYPALISHIRING"` is written in a zigzag pattern across a given number of rows.

After writing the characters in a zigzag pattern, read the characters row by row to create a new string.

Given a string `s` and an integer `numRows`, return the converted string.

---

## Example 1

### Input

`s = "PAYPALISHIRING"`

`numRows = 3`

### Output

`"PAHNAPLSIIGYIR"`

### Explanation

The string is arranged in three rows:

```text
P   A   H   N
A P L S I I G
Y   I   R
```

Reading row by row produces `"PAHNAPLSIIGYIR"`.

---

## Example 2

### Input

`s = "PAYPALISHIRING"`

`numRows = 4`

### Output

`"PINALSIGYAHRPI"`

### Explanation

The string is arranged in four rows:

```text
P     I    N
A   L S  I G
Y A   H R
P     I
```

Reading row by row produces `"PINALSIGYAHRPI"`.

---

## Example 3

### Input

`s = "A"`

`numRows = 1`

### Output

`"A"`

### Explanation

When there is only one row, the string remains unchanged.

---

## Constraints

* `1 <= s.length <= 1000`
* `s` consists of English letters, `','` and `'.'`.
* `1 <= numRows <= 1000`

---

## Approach

Use **Row Simulation** to arrange the characters in a zigzag pattern.

1. Create a separate collection for each row.
2. Start placing characters in the first row and move downward.
3. When the last row is reached, change direction and move upward diagonally.
4. When the first row is reached again, change direction and move downward.
5. Continue until all characters have been placed.
6. Combine the rows in order to produce the converted string.

**Special case:** If `numRows` is `1` or greater than or equal to the string length, the string remains unchanged.

---

## Complexity Analysis

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

Where `n` is the length of the input string.

Each character is processed once and stored in its corresponding row.

---

## Key Concepts

* Strings
* Simulation
* Array / List Manipulation
* Direction Tracking
* String Concatenation

---

## What I Learned

* How to simulate a zigzag pattern.
* How to change traversal direction at row boundaries.
* How to organize characters into multiple rows.
* How to reconstruct a string from grouped characters.
* How to solve string manipulation problems efficiently.

---

## LeetCode Details

* **Problem:** #6 — Zigzag Conversion
* **Difficulty:** Medium
* **Topics:** String
* **Pattern:** Simulation / Direction Tracking
