### Input is an Array or String:

- Is the array sorted?

  - Yes: Use `Binary Search` or `Two Pointers`.
  - No: Move to the next checks.

- What is the question asking?

  - Number of ways to do something / Max-Min of something:
    - If decisions are dependent on each other, use `Dynamic Programming`.
    - If decisions are independent, use `Greedy`.
  - Is something possible?:
    - Try `Backtracking`.

- Does it involve string manipulation?

  - Prefix matching: Use `Trie`.
  - Building strings or finding distances
    - Use `Stack` or `Monotonic Stack`.

- Is it about finding a specific element?

  - Use a `Hash Map` or `Set`.

- Does it involve elements being added/removed in a sliding window fashion?

  - Use a `Sliding Window` or Counting `Hash Map`.

- Is the problem about continuously finding the max/min element or removing them?
  - Use a `Heap` or `Monotonic Queue`.

---

### Input is a Graph:

- Does the question involve finding the shortest path or the fewest steps?
- Yes: Use Breadth-First Search (BFS).
- No: Use Depth-First Search (DFS).

---

### Input is a Tree (probably binary):

- Does the question involve specific depths/levels?
  - Yes: Use `Breadth-First Search (BFS)`.
  - No: Use `Depth-First Search (DFS)`.

---

### Input is a Linked List:

- Does it involve detecting cycles?
  - Use `Fast and Slow Pointers`.
- Does it involve reversing or modifications?
  - Use a `“prev” pointer` for reversing.
  - Use a `“dummy” pointer` for maintaining the original head.

---

1.  Sliding Window

    - Description: This pattern is used to find a subset of elements in a data structure (usually an array or string) that satisfies certain conditions. You maintain a window (a subset of elements) and slide it across the structure to solve the problem efficiently.
    - Use cases: Problems related to subarrays, substrings, or sequences of elements.
    - Example:

      - Problem: Find the maximum sum of any subarray of size k in an array.
      - Solution:

        ```python
        def max_subarray_sum(arr, k):
            window_sum, max_sum = 0, 0

            for i in range(k):
                window_sum += arr[i]

            max_sum = window_sum

            for i in range(k, len(arr)):
                window_sum += arr[i] - arr[i - k]
                max_sum = max(max_sum, window_sum)

            return max_sum
        ```

2.  Two Pointers

    - Description: This pattern involves using two pointers to traverse the input structure, often used to solve problems involving arrays or linked lists.
    - Use cases: Problems involving arrays, sorting, or searching.
    - Example:

      - Problem: Find if a pair of numbers in a sorted array sums up to a target value.
      - Solution:

      ```python
      def two_sum(arr, target):
         left, right = 0, len(arr) - 1
         while left < right:
             current_sum = arr[left] + arr[right]
             if current_sum == target:
                 return True
             elif current_sum < target:
                 left += 1
             else:
                 right -= 1
         return False
      ```

3.  Fast and Slow Pointers

    - Description: This pattern uses two pointers that move at different speeds. It's often used to detect cycles in a data structure or to find the middle of a structure.
    - Use cases: Cycle detection, linked list problems, finding middle of a list, etc.
    - Example:

      - Problem: Detect a cycle in a linked list.
      - Solution:

        ```python
        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next

        def has_cycle(head):
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True

            return False
        ```

4.  Merge Intervals

    - Description: This pattern is used to merge overlapping intervals in problems where you have a set of intervals, and you need to combine them or check for overlaps.
    - Use cases: Interval problems, scheduling problems, meeting rooms, etc.
    - Example:

      - Problem: Merge overlapping intervals.
      - Solution:

      ```python
      def merge_intervals(intervals):
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
      ```

5.  Backtracking

    - Description: In this pattern, you explore all possible solutions by making choices at each step, and if a choice leads to a dead end, you "backtrack" and try a different path. It's often used in problems involving permutations, combinations, or paths.
    - Use cases: Solving puzzles, generating permutations/combinations, solving mazes, etc.
    - Example:

      - Problem: Generate all permutations of a list of numbers.
      - Solution:

        ```python
        def permute(nums):

            def backtrack(start):
                if start == len(nums):
                    result.append(nums[:])
                    return

                for i in range(start, len(nums)):
                    nums[start], nums[i] = nums[i], nums[start]
                    backtrack(start + 1)
                    nums[start], nums[i] = nums[i], nums[start]

            result = []
            backtrack(0)
            return result
        ```

6.  Divide and Conquer

    - Description: This pattern involves dividing the problem into smaller subproblems, solving each subproblem independently, and then combining the results to solve the original problem.
    - Use cases: Sorting algorithms (e.g., Merge Sort, Quick Sort), binary search, etc.
    - Example:

      - Problem: Merge Sort.
      - Solution:

        ```python
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)

        def merge(left, right):
            result = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        ```

7.  Greedy Algorithms

    - Description: In this pattern, you make the locally optimal choice at each stage with the hope of finding the global optimum.
    - Use cases: Problems involving intervals, coin change, activity selection, etc.
    - Example:

      - Problem: Coin change problem (minimum number of coins to make a value).
      - Solution:

        ```python
        def coin_change(coins, amount):
            dp = [float('inf')] * (amount + 1)
            dp[0] = 0
            for coin in coins:
                for i in range(coin, amount + 1):
                    dp[i] = min(dp[i], dp[i - coin] + 1)

            if dp[amount] != float('inf')
                return dp[amount]
            else -1
        ```

8.  Dynamic Programming

    - Description: This pattern involves solving problems by breaking them down into overlapping subproblems and solving each subproblem only once, storing the results to avoid redundant work.
    - Use cases: Problems with optimal substructure, where subproblems overlap.
    - Example:

      - Problem: Fibonacci series using dynamic programming.
      - Solution:

        ```python
        def fib(n):
            dp = [0] * (n + 1)
            dp[1] = 1
            for i in range(2, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]
            return dp[n]
        ```

9.  Topological Sorting (Graph)

    - Description: This pattern is used to find a linear ordering of vertices in a directed graph, such that for every directed edge u -> v, vertex u comes before vertex v in - the ordering.
    - Use cases: Task scheduling, dependencies, etc.
    - Example:

      - Problem: Topological sorting of a Directed Acyclic Graph (DAG).
      - Solution:

        ```python

        from collections import defaultdict, deque

        def topological_sort(vertices, edges):
        graph = defaultdict(list)
        in_degree = {v: 0 for v in vertices}

            for u, v in edges:
                graph[u].append(v)
                in_degree[v] += 1

            queue = deque([v for v in vertices if in_degree[v] == 0])
            sorted_order = []

            while queue:
                node = queue.popleft()
                sorted_order.append(node)

                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

            return sorted_order if len(sorted_order) == len(vertices) else []

        vertices = ['A', 'B', 'C', 'D', 'E', 'F']
        edges = [('A', 'C'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F')]
        print(topological_sort(vertices, edges))
        ```

10. Binary Search

    - Description: This pattern is used to search for a target value in a sorted array or similar data structure, halving the search space at each step.
    - Use cases: Searching in sorted arrays, binary search tree operations, etc.
    - Example:

      - Problem: Find the position of a target value in a sorted array.
      - Solution:

        ```python

        def binary_search(arr, target):
            left, right = 0, len(arr) - 1

            while left <= right:
                mid = left + (right - left) // 2
                    if arr[mid] == target:
                        return mid
                    elif arr[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
            return -1
        ```
