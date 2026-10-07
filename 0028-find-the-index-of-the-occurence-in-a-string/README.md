# LeetCode #28 — Find the Index of the First Occurrence in a String

## Problem

Given two strings `haystack` and `needle`, return the **index of the first occurrence** of `needle` in `haystack`.

If `needle` is not part of `haystack`, return `-1`.

---

## Example 1

### Input

`haystack = "sadbutsad"`

`needle = "sad"`

### Output

`0`

### Explanation

The substring `"sad"` occurs at index `0` for the first time.

---

## Example 2

### Input

`haystack = "leetcode"`

`needle = "leeto"`

### Output

`-1`

### Explanation

The substring `"leeto"` does not occur in `"leetcode"`.

---

## Example 3

### Input

`haystack = "hello"`

`needle = "ll"`

### Output

`2`

### Explanation

The first occurrence of `"ll"` starts at index `2`.

---

## Example 4

### Input

`haystack = "aaaaa"`

`needle = "bba"`

### Output

`-1`

### Explanation

The substring `"bba"` does not exist in `"aaaaa"`.

---

## Constraints

* `1 <= haystack.length, needle.length <= 10⁴`
* `haystack` and `needle` consist of only lowercase English letters.

---

## Approach

Use a **String Matching** approach.

1. Start checking from the beginning of `haystack`.
2. Compare the characters of `needle` with the corresponding characters in `haystack`.
3. If all characters of `needle` match, return the starting index.
4. If a mismatch occurs, move to the next possible starting position.
5. Continue until `needle` is found or there are no more possible positions.
6. If `needle` is not found, return `-1`.

---

## Complexity Analysis

* **Time Complexity:** `O(n × m)`
* **Space Complexity:** `O(1)`

Where:

* `n` = length of `haystack`
* `m` = length of `needle`

---

## Key Concepts

* Strings
* String Matching
* Substrings
* Indexing
* String Traversal
* Pattern Searching

---

## What I Learned

* How to search for one string inside another string.
* How to find the first occurrence of a substring.
* How string indexing works.
* How to compare characters between two strings.
* How to return `-1` when a substring does not exist.

---

## LeetCode Details

* **Problem:** #28 — Find the Index of the First Occurrence in a String
* **Difficulty:** Easy
* **Topics:** String, String Matching
* **Pattern:** Substring Search / String Traversal
