# LeetCode Solutions

A structured collection of my **LeetCode problem-solving solutions**, focused on strengthening Data Structures, Algorithms, problem-solving skills, and coding interview preparation.

The repository contains solutions written primarily in **Python**, organized by problem and topic for easy learning and reference.

---

## About This Repository

This repository documents my journey of solving coding problems on **LeetCode**.

### Objectives

* Strengthen Data Structures and Algorithms fundamentals
* Improve logical and problem-solving skills
* Practice writing clean and optimized code
* Understand time and space complexity
* Prepare for technical coding interviews
* Maintain a consistent coding practice record

---

## Tech Stack

* **Language:** Python
* **Platform:** LeetCode
* **Version Control:** Git & GitHub
* **IDE:** VS Code

---

## Topics Covered

The repository will cover problems from the following areas:

| Topic               | Concepts                           |
| ------------------- | ---------------------------------- |
| Arrays              | Traversal, Searching, Manipulation |
| Strings             | Character Operations, Patterns     |
| Hash Tables         | Dictionaries, Frequency Counting   |
| Two Pointers        | Pair Searching, Array Optimization |
| Sliding Window      | Subarrays, Substrings              |
| Stack               | LIFO, Valid Parentheses            |
| Queue               | FIFO, BFS                          |
| Linked List         | Traversal, Reversal                |
| Binary Search       | Search Optimization                |
| Trees               | DFS, BFS, Traversal                |
| Graphs              | BFS, DFS, Connectivity             |
| Recursion           | Recursive Problem Solving          |
| Dynamic Programming | Memoization, Tabulation            |
| Sorting             | Sorting Algorithms                 |
| Greedy              | Local Optimization                 |
| Backtracking        | Combinations, Permutations         |

---

## Repository Structure

```text
leetcode-solutions/
│
├── Arrays/
│   ├── Two_Sum.py
│   └── Best_Time_to_Buy_and_Sell_Stock.py
│
├── Strings/
│   └── Valid_Palindrome.py
│
├── Hash_Table/
│   └── Contains_Duplicate.py
│
├── Two_Pointers/
│   └── Two_Sum_II.py
│
├── Binary_Search/
│   └── Binary_Search.py
│
├── Linked_List/
│   └── Reverse_Linked_List.py
│
├── Stack/
│   └── Valid_Parentheses.py
│
├── Trees/
│   └── Binary_Tree_Traversal.py
│
└── README.md
```

---

## Featured Problem

### Two Sum

**Difficulty:** Easy
**Topics:** Array, Hash Table

Given an array of integers and a target value, find the indices of two numbers whose sum equals the target.

### Example

```text
Input:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]
```

### Approach

Use a Hash Map to store previously visited numbers and their indices.

```python
class Solution:
    def twoSum(self, nums, target):
        num_map = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_map:
                return [num_map[complement], i]

            num_map[num] = i
```

### Complexity

```text
Time Complexity:  O(n)
Space Complexity: O(n)
```

---

## Problem Progress

| Category            | Solved | Status      |
| ------------------- | -----: | ----------- |
| Arrays              |        | In Progress |
| Strings             |        | In Progress |
| Hash Tables         |        | In Progress |
| Two Pointers        |        | Planned     |
| Sliding Window      |        | Planned     |
| Stack               |        | Planned     |
| Linked List         |        | Planned     |
| Binary Search       |        | Planned     |
| Trees               |        | Planned     |
| Graphs              |        | Planned     |
| Dynamic Programming |        | Planned     |

---

## Problem-Solving Approach

For each problem, I follow these steps:

1. Understand the problem statement
2. Identify the input and expected output
3. Consider a brute-force approach
4. Identify a more efficient approach
5. Implement the solution
6. Analyze time and space complexity
7. Test the solution with different cases
8. Document the key concept learned

---

## Coding Principles

The solutions aim to follow:

* Clean and readable code
* Meaningful variable names
* Efficient algorithms
* Appropriate data structures
* Proper time and space complexity analysis
* Edge-case consideration
* Interview-oriented problem solving

---

## Learning Goals

Through this repository, I am working toward improving my ability to:

* Solve algorithmic problems independently
* Select appropriate data structures
* Optimize inefficient solutions
* Analyze algorithm complexity
* Write production-quality Python code
* Approach technical interview problems systematically

---

## Progress Tracking

I will continuously update this repository as I solve more problems.

**Goal:** Build strong fundamentals in **Data Structures & Algorithms** through consistent problem solving.

---

## Connect

**GitHub:** [NagaDurgaM](https://github.com/NagaDurgaM)

**LinkedIn:** [Naga Durga Lakshmi](https://www.linkedin.com/in/nagadurgalakshmimetti/)

---

## Disclaimer

This repository is maintained for **learning, practice, and interview preparation**. The solutions represent my own problem-solving practice and may be improved as I learn more efficient approaches.

---

**Keep Learning. Keep Solving. Keep Improving.**
