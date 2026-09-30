# Two Sum

## Problem Description

Given an array of integers `nums` and an integer `target`, return the **indices of the two numbers** such that they add up to the given target.

You may assume that:

* Each input has **exactly one solution**.
* You cannot use the same element twice.
* The answer can be returned in any order.

---

## Example 1

### Input

```text
nums = [2, 7, 11, 15]
target = 9
```

### Output

```text
[0, 1]
```

### Explanation

`nums[0] + nums[1] = 2 + 7 = 9`

Therefore, the answer is:

```text
[0, 1]
```

---

## Example 2

### Input

```text
nums = [3, 2, 4]
target = 6
```

### Output

```text
[1, 2]
```

### Explanation

`nums[1] + nums[2] = 2 + 4 = 6`

---

## Example 3

### Input

```text
nums = [3, 3]
target = 6
```

### Output

```text
[0, 1]
```

### Explanation

`nums[0] + nums[1] = 3 + 3 = 6`

---

## Constraints

* `2 <= nums.length <= 10⁴`
* `-10⁹ <= nums[i] <= 10⁹`
* `-10⁹ <= target <= 10⁹`
* Exactly one valid answer exists.
* The same element cannot be used twice.

---

## Approach

A simple and efficient approach is to use a **Hash Map**.

For each number:

1. Calculate the required value:

   ```text
   complement = target - nums[i]
   ```
2. Check whether the complement already exists in the Hash Map.
3. If it exists, return its index and the current index.
4. Oth
