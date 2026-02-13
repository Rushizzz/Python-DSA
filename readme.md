# 🛠️ 2026 DSA Progress Tracker (Private)

**Goal:** 2 Hours Daily | **Status:** 2-Month Sprint
**Focus:** Identify patterns, don't just "get it to pass."

---

## 🟦 PHASE 1: ARRAYS & POINTERS (WEEK 1)
*Focus: Avoiding O(n²) and managing memory.*

- [ ] **Two Sum** 
    - *Logic:* Use a Map to store `(target - current)`. Trade space for speed.
- [ ] **3Sum** 
    - *Logic:* Sort first. Fix one pointer, use Two Pointers for the rest. Watch for duplicates!
- [ ] **Sliding Window: Longest Substring** 
    - *Logic:* Use a "Shrinking/Expanding" window. Use a Set to track seen chars.
- [ ] **Maximum Subarray (Kadane's)** 
    - *Logic:* "Local Max vs Global Max." If current sum < 0, reset it.

## 🟩 PHASE 2: LINKED LISTS (WEEK 2)
*Focus: Pointers & the 'Dummy Node' trick.*

- [ ] **Reverse Linked List** 
    - *Logic:* `next = curr.next`, `curr.next = prev`, `prev = curr`, `curr = next`.
- [ ] **Cycle Detection (Tortoise & Hare)** 
    - *Logic:* Fast moves 2x, Slow moves 1x. If they meet, there's a loop.
- [ ] **Remove Nth Node From End** 
    - *Logic:* Use two pointers `n` distance apart. When fast hits end, slow is at the target.

## 🟨 PHASE 3: RECURSION & BACKTRACKING (WEEK 3-4)
*Focus: The State Tree. Remember to "Undo" your move.*

- [ ] **Subsets** 
    - *Logic:* The "Include/Exclude" choice at every element.
- [ ] **Permutations** 
    - *Logic:* Swap elements to fix positions. Don't forget to swap back (backtrack).
- [ ] **Combination Sum** 
    - *Logic:* DFS with a target. Subtract from target; if 0, you found a path.

---

## 🟥 PHASE 4: THE DP DEEP DIVE (2 WEEKS)
*Focus: State → Recurrence → Memoize → Tabulate.*

### Week 1: 1D & Grids
- [ ] **Climbing Stairs** 
    - *Insight:* It's just Fibonacci. `dp[i] = dp[i-1] + dp[i-2]`.
- [ ] **House Robber** 
    - *Insight:* Decision: `rob current + rob i-2` OR `skip current and take i-1`.
- [ ] **Unique Paths (Grid)** 
    - *Insight:* `dp[r][c] = dp[r-1][c] + dp[r][c-1]`. Boundary checks are key.

### Week 2: Classical Patterns
- [ ] **0/1 Knapsack** 
    - *Insight:* Weight vs Value. Use a 2D array (or optimized 1D) for "Take/Don't Take".
- [ ] **Coin Change** 
    - *Insight:* Unbounded DP. Use `min(dp[current_amount], 1 + dp[amount - coin])`.
- [ ] **Longest Common Subsequence (LCS)** 
    - *Insight:* If chars match: `1 + diagonal`. If not: `max(top, left)`.
- [ ] **Edit Distance** 
    - *Insight:* The 3-way choice: Insert, Delete, Replace. 

---

## 📔 LOG BOOK
| Date | Problem | Time Taken | Struggle Point / Note |
| :--- | :--- | :--- | :--- |
| | | | |


