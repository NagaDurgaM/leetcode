# LeetCode #10 — Regular Expression Matching

## Problem

Given an input string `s` and a pattern `p`, implement regular expression matching with support for:

* `.` — Matches any single character.
* `*` — Matches zero or more occurrences of the preceding element.

The matching should cover the **entire input string**, not just a part of it.

---

## Example 1

### Input

`s = "aa"`

`p = "a"`

### Output

`false`

### Explanation

The pattern `"a"` matches only one `a`, while the input contains two `a` characters.

---

## Example 2

### Input

`s = "aa"`

`p = "a*"`

### Output

`true`

### Explanation

`*` allows the preceding character `a` to appear zero or more times.

Therefore, `"a*"` can match `"aa"`.

---

## Example 3

### Input

`s = "ab"`

`p = ".*"`

### Output

`true`

### Explanation

`.` matches any character and `*` allows it to match multiple characters.

Therefore, `".*"` can match `"ab"`.

---

## Example 4

### Input

`s = "aab"`

`p = "c*a*b"`

### Output

`true`

### Explanation

* `c*` matches zero occurrences of `c`.
* `a*` matches two occurrences of `a`.
* `b` matches `b`.

Therefore, the complete string `"aab"` is matched.

---

## Example 5

### Input

`s = "mississippi"`

`p = "mis*is*p*."`

### Output

`false`

### Explanation

The pattern cannot match the complete input string according to the rules for `.` and `*`.

---

## Constraints

* `1 <= s.length <= 20`
* `1 <= p.length <= 20`
* `s` contains only lowercase English letters.
* `p` contains only lowercase English letters, `.` and `*`.
* It is guaranteed that every `*` has a valid preceding element.

---

## Approach

Use **Dynamic Programming** to determine whether different portions of the string match different portions of the pattern.

For each position in the string and pattern:

1. Check whether the current characters match.
2. A character matches when:

   * Both characters are the same, or
   * The pattern character is `.`
3. If the next pattern character is `*`, there are two possibilities:

   * Treat `*` as matching **zero occurrences**.
   * Treat `*` as matching **one or more occurrences**, if the current characters match.
4. Continue checking the remaining portions of the string and pattern.
5. The final result is `true` only when the **entire string** matches the **entire pattern**.

---

## Complexity Analysis

* **Time Complexity:** `O(m × n)`
* **Space Complexity:** `O(m × n)`

Where:

* `m` = length of the input string `s`
* `n` = length of the pattern `p`

---

## Key Concepts

* Strings
* Regular Expressions
* Dynamic Programming
* Pattern Matching
* Recursion / Memoization
* State Transitions

---

## What I Learned

* How regular expression matching works with `.` and `*`.
* How `*` can represent zero or multiple occurrences.
* How to handle multiple matching possibilities.
* How Dynamic Programming can avoid repeated calculations.
* How to ensure the **entire string** matches the pattern.

---

## LeetCode Details

* **Problem:** #10 — Regular Expression Matching
* **Difficulty:** Hard
* **Topics:** String, Dynamic Programming, Recursion
* **Pattern:** Dynamic Programming / Pattern Matching
