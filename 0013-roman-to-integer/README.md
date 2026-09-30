# LeetCode #13 - Roman to Integer

## Problem

Given a string `s` representing a **Roman numeral**, convert it into an integer.

Roman numerals use the following symbols:

| Symbol | Value |
| ------ | ----: |
| I      |     1 |
| V      |     5 |
| X      |    10 |
| L      |    50 |
| C      |   100 |
| D      |   500 |
| M      |  1000 |

---

## Example 1

**Input:**

```text
s = "III"
```

**Output:**

```text
3
```

**Explanation:**

```text
III = 1 + 1 + 1 = 3
```

---

## Example 2

**Input:**

```text
s = "LVIII"
```

**Output:**

```text
58
```

**Explanation:**

```text
L = 50
V = 5
III = 3

50 + 5 + 3 = 58
```

---

## Example 3

**Input:**

```text
s = "MCMXCIV"
```

**Output:**

```text
1994
```

**Explanation:**

```text
M    = 1000
CM   = 900
XC   = 90
IV   = 4

1000 + 900 + 90 + 4 = 1994
```

---

## Approach

Use a mapping of Roman symbols to their integer values.

* Read the Roman numeral from left to right.
* If a smaller value appears before a larger value, subtract it.
* Otherwise, add the value.
* Continue until
