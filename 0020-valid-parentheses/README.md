# LeetCode #20 — Valid Parentheses

## Problem

Given a string `s` containing only the characters:

`(`, `)`, `{`, `}`, `[`, and `]`

Determine if the input string is valid.

A string is valid if:

* Every opening bracket has a corresponding closing bracket.
* Brackets are closed in the correct order.
* Every closing bracket matches the most recent unmatched opening bracket.

---

## Example 1

### Input

`s = "()"`

### Output

`true`

### Explanation

The opening bracket `(` is correctly closed by `)`.

---

## Example 2

### Input

`s = "()[]{}"`

### Output

`true`

### Explanation

All brackets are correctly matched.

---

## Example 3

### Input

`s = "(]"`

### Output

`false`

### Explanation

`(` must be closed by `)`, but the string contains `]`.

---

## Example 4

### Input

`s = "([)]"`

### Output

`false`

### Explanation

The brackets are not closed in the correct order.

---

## Example 5

### Input

`s = "{[]}"`

### Output

`true`

### Explanation

All brackets are correctly nested and matched.

---

## Constraints

* `1 <= s.length <= 10⁴`
* `s` consists only of parentheses, curly brackets, and square brackets.
* Valid brackets are `()`, `{}`, and `[]`.

---

## Approach

Use a **Stack** to keep track of opening brackets.

For each character:

1. If it is an opening bracket, add it to the stack.
2. If it is a closing bracket, check the most recently added opening bracket.
3. Make sure the opening and closing brackets match.
4. Remove the matched opening bracket from the stack.
5. If a closing bracket does not match, the string is invalid.
6. After checking all characters, the stack must be empty for the string to be valid.

---

## Complexity Analysis

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

Where `n` is the length of the string.

---

## Key Concepts

* Stack
* LIFO (Last In, First Out)
* String
* Bracket Matching
* Nested Structures

---

## What I Learned

* How stacks are used to validate nested structures.
* How to match opening and closing brackets.
* How the LIFO principle works.
* How to handle nested parentheses efficiently.
* How to solve the problem with `O(n)` time complexity.

---

## LeetCode Details

* **Problem:** #20 — Valid Parentheses
* **Difficulty:** Easy
* **Topics:** String, Stack
* **Pattern:** Stack / Matching Pairs
