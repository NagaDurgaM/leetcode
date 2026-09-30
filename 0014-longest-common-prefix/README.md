# LeetCode #14 - Longest Common Prefix

## Problem

Write a function to find the **longest common prefix** string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

---

## Example 1

**Input:**

```text id="p9x8rm"
strs = ["flower","flow","flight"]
```

**Output:**

```text id="6m8l0s"
"fl"
```

**Explanation:**

The strings all start with `"fl"`.

---

## Example 2

**Input:**

```text id="jv8j9y"
strs = ["dog","racecar","car"]
```

**Output:**

```text id="l1r4j3"
""
```

**Explanation:**

There is no common prefix among the given strings.

---

## Approach

Compare the characters of the strings from left to right.

* Start with the first string as the prefix.
* Compare it with the next string.
* Remove characters from the prefix until it matches.
* Continue until all strings have been checked.
* Return the remaining prefix.

### Example

```text id="n8h7up"
["flower", "flow", "flight"]
```

Common characters:

```text id="g4tqz7"
f
l
```

So the longest common prefix is:

```text id="m0m1m9"
"fl"
```

---

## Complexity

**Time Complexity:** `O(n × m)`

**Space Complexity:** `O(1)`

Where:

* `n` = number of strings
* `m` = length of the shortest string

---

## Concepts Used

* Strings
* Arrays
* String Comparison
* Loops
* Prefix Matching
* Conditional Statements
* Time Complexity
* Space Complexity

---

## Important Cases

* All strings are the same
* No common prefix
* Only one string
* Empty string
* One string is a prefix of another

---

## LeetCode Details

| Detail     | Value                 |
| ---------- | --------------------- |
| Problem    | Longest Common Prefix |
| Number     | #14                   |
| Difficulty | Easy                  |
| Topic      | String, Array         |

---

## Author

**Naga Durga Lakshmi**

GitHub: [NagaDurgaM](https://github.com/NagaDurgaM)

LinkedIn: [Naga Durga Lakshmi](https://www.linkedin.com/in/nagadurgalakshmimetti/)
