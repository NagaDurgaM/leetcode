# LeetCode #3 - Longest Substring Without Repeating Characters

## Problem

Given a string `s`, find the length of the **longest substring** without duplicate characters.

---

## Example 1

**Input:**

```text
s = "abcabcbb"
```

**Output:**

```text
3
```

**Explanation:**

The longest substring is `"abc"`.

Length = `3`

---

## Example 2

**Input:**

```text
s = "bbbbb"
```

**Output:**

```text
1
```

**Explanation:**

The longest substring is `"b"`.

Length = `1`

---

## Example 3

**Input:**

```text
s = "pwwkew"
```

**Output:**

```text
3
```

**Explanation:**

The longest substring is `"wke"`.

Length = `3`

`"pwke"` is not a substring because the characters are not continuous.

---

## Approach

Use the **Sliding Window** technique.

* Start with an empty window.
* Move through the string character by character.
* Keep track of characters already in the window.
* If a duplicate is found, move the starting position forward.
* Keep the maximum length found.

---

## Complexity

**Time Complexity:** `O(n)`

**Space Complexity:** `O(n)`

---

## Concepts Used

* String
* Sliding Window
* Two Pointers
* Set
* Duplicate Detection
* Time Complexity
* Space Complexity

---

## Constraints

* `0 <= s.length <= 10⁵`
* `s` contains English letters, digits, symbols, and spaces.

---

## LeetCode Details

| Detail     | Value                                          |
| ---------- | ---------------------------------------------- |
| Problem    | Longest Substring Without Repeating Characters |
| Number     | #3                                             |
| Difficulty | Medium                                         |
| Topic      | String, Sliding Window                         |

---

## Author

**Naga Durga Lakshmi**

GitHub: [NagaDurgaM](https://github.com/NagaDurgaM)

LinkedIn: [Naga Durga Lakshmi](https://www.linkedin.com/in/nagadurgalakshmimetti/)
