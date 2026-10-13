# LeetCode #58 — Length of Last Word

## Problem

Given a string `s` consisting of words and spaces, return the **length of the last word** in the string.

A word is defined as a **maximal substring consisting of non-space characters only**.

---

## Example 1

### Input

`s = "Hello World"`

### Output

`5`

### Explanation

The last word is `"World"`, which has a length of `5`.

---

## Example 2

### Input

`s = " fly me to the moon "`

### Output

`4`

### Explanation

The last word is `"moon"`, which has a length of `4`.

---

## Example 3

### Input

`s = "luffy is still joyboy"`

### Output

`6`

### Explanation

The last word is `"joyboy"`, which has a length of `6`.

---

## Constraints

* `1 <= s.length <= 10⁴`
* `s` consists of only English letters and spaces.
* There is at least one word in `s`.

---

## Approach

Use **String Traversal** to find the last word efficiently.

1. Start from the end of the string.
2. Skip any trailing spaces.
3. Count the characters of the last word.
4. Stop when a space or the beginning of the string is reached.
5. Return the total character count.

---

## Complexity Analysis

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

Where `n` is the length of the string.

The string is traversed from the end, and no additional data structure is required.

---

## Key Concepts

* Strings
* String Traversal
* Character Counting
* Indexing
* Space Handling

---

## What I Learned

* How to find the last word in a string.
* How to handle leading and trailing spaces.
* How to count characters efficiently.
* How to traverse a string backward.
* How to solve a string problem with `O(n)` time and `O(1)` extra space.

---

## LeetCode Details

* **Problem:** #58 — Length of Last Word
* **Difficulty:** Easy
* **Topics:** String
* **Pattern:** Reverse Traversal / String Manipulation
