# LeetCode #5 — Longest Palindromic Substring

## Problem

Given a string `s`, return the **longest palindromic substring** in `s`.

A **palindrome** is a string that reads the same forward and backward.

---

## Example 1

### Input

`s = "babad"`

### Output

`"bab"`

### Explanation

`"bab"` is a palindrome.

`"aba"` is also a valid answer because it is also a palindrome of the same length.

---

## Example 2

### Input

`s = "cbbd"`

### Output

`"bb"`

### Explanation

`"bb"` is the longest palindromic substring.

---

## Example 3

### Input

`s = "a"`

### Output

`"a"`

### Explanation

A single character is always a palindrome.

---

## Example 4

### Input

`s = "ac"`

### Output

`"a"`

### Explanation

Both `"a"` and `"c"` are palindromes, but either one can be returned because they have the same length.

---

## Constraints

* `1 <= s.length <= 1000`
* `s` consists of only English letters and digits.

---

## Approach

Use the **Expand Around Center** technique.

A palindrome can have:

* A single character as its center.
* Two characters as its center.

For every character in the string:

1. Consider it as the center of an odd-length palindrome.
2. Expand outward while the characters on both sides are equal.
3. Also consider the space between the current character and the next character as the center of an even-length palindrome.
4. Expand outward while the characters match.
5. Keep track of the longest palindrome found.
6. Return the longest palindromic substring.

---

## Complexity Analysis

* **Time Complexity:** `O(n²)`
* **Space Complexity:** `O(1)`

Where `n` is the length of the string.

---

## Key Concepts

* Strings
* Palindromes
* Two Pointers
* Expand Around Center
* Substrings
* String Traversal

---

## What I Learned

* How to identify palindromic substrings.
* How to use the **Expand Around Center** technique.
* The difference between odd-length and even-length palindromes.
* How to compare characters from both sides.
* How to find the longest palindrome efficiently without creating additional data structures.

---

## LeetCode Details

* **Problem:** #5 — Longest Palindromic Substring
* **Difficulty:** Medium
* **Topics:** String, Dynamic Programming
* **Pattern:** Expand Around Center
