# Algorithms & Data Structures in TypeScript — Study Checklist (~60–70 hours)

Format for each topic: theory → implement the data structure in this repo → solve problems as files in this repo → verify on LeetCode. Blocks must be completed strictly in order (they are arranged by dependency).

## Ground Rules

- [ ] **The 30-minute rule:** stuck with no progress — watch an explanation (NeetCode), mark the problem, and re-solve it from scratch 3–4 days later
- [ ] Implementing a structure should take 1–2 evenings max: core operations only, no API polishing. Roughly 30% of time on implementations, 70% on problems
- [ ] Solve each problem as a file in the repo first (with a sample call at the bottom, run via `npx tsx src/...`), then submit on LeetCode to verify
- [ ] Keep a log: problem / solved on my own or with help / re-solve date

---

## Block 1. Warm-up: Two Pointers, Sliding Window, Prefix Sums (~5–6 h)

No data structures here — pure techniques.

**Theory:** when each pattern applies (sorted input → two pointers; subarray/substring → sliding window; range sums → prefix sums).

**Repo output:**
```
src/algorithms/two-pointers/
├── two-sum-sorted.ts
├── three-sum.ts
├── container-with-most-water.ts
└── move-zeroes.ts
src/algorithms/sliding-window/
├── best-time-to-buy-sell-stock.ts
├── longest-substring-no-repeat.ts
└── permutation-in-string.ts
src/algorithms/prefix-sum/
├── range-sum-query.ts
├── subarray-sum-equals-k.ts
└── product-of-array-except-self.ts
```

**LeetCode to verify:** submit the problems solved in the repo — Move Zeroes (easy), Two Sum II — Input Array Is Sorted (medium), 3Sum (medium), Container With Most Water (medium); Best Time to Buy and Sell Stock (easy), Longest Substring Without Repeating Characters (medium), Permutation in String (medium); Range Sum Query — Immutable (easy), Subarray Sum Equals K (medium), Product of Array Except Self (medium).

**Block is done when:** you recognize the pattern from the problem statement before writing any code.

---

## Block 2. Stack (~3–4 h)

**Theory:** LIFO, operation complexities, the call stack as a stack, monotonic stack.

**Implementation:** `Stack<T>` backed by an array: `push`, `pop`, `peek`, `isEmpty`, `size`.

**Repo output:**
```
src/data-structures/stack/
├── Stack.ts
└── problems/
    ├── valid-parentheses.ts
    ├── min-stack.ts
    ├── evaluate-rpn.ts
    └── daily-temperatures.ts      # monotonic stack
```

**LeetCode to verify:** submit the problems solved in the repo — Valid Parentheses (easy), Min Stack (medium), Evaluate Reverse Polish Notation (medium), Daily Temperatures (medium). If it felt easy — additionally Car Fleet (medium).

**Block is done when:** you solved daily-temperatures and can explain why a monotonic stack gives O(n).

---

## Block 3. Queue (~2–3 h)

**Theory:** FIFO; why `Array.prototype.shift()` is O(n) and how to avoid it (circular buffer or two stacks); deque.

**Implementation:** `Queue<T>` on linked nodes or two stacks: `enqueue`, `dequeue`, `peek`, `isEmpty`, `size`.

**Repo output:**
```
src/data-structures/queue/
├── Queue.ts
└── problems/
    ├── queue-using-stacks.ts
    ├── recent-counter.ts
    └── sliding-window-maximum.ts   # deque, medium/hard — OK to solve with help
```

**Block is done when:** you can explain why BFS needs a queue (you'll use this in Blocks 10 and 13).

---

## Block 4. Singly Linked List (~4–5 h)

**Theory:** nodes and references; complexity comparison with arrays; fast/slow pointer technique; dummy head node.

**Implementation:** `SinglyLinkedList<T>`: `pushFront`, `pushBack`, `popFront`, `insertAt`, `removeAt`, `find`, `toArray`.

**Repo output:**
```
src/data-structures/linked-list-singly/
├── SinglyLinkedList.ts
└── problems/
    ├── reverse-list.ts             # iterative AND recursive, two functions
    ├── find-middle.ts              # fast/slow
    ├── merge-two-sorted-lists.ts
    ├── has-cycle.ts                # Floyd's algorithm
    ├── remove-nth-from-end.ts
    └── reorder-list.ts             # medium, combines middle + reverse + merge
```

**Block is done when:** you write reverse-list in 5 minutes with no mistakes; you solved reorder-list by spotting the three previous problems inside it.

---

## Block 5. Doubly Linked List (~2–3 h)

**Theory:** why the backward reference matters; real-world uses (browser history, LRU cache).

**Implementation:** `DoublyLinkedList<T>`: `pushFront`, `pushBack`, `popFront`, `popBack`, `remove(node)` in O(1).

**Repo output:**
```
src/data-structures/linked-list-doubly/
├── DoublyLinkedList.ts
└── problems/
    ├── browser-history.ts
    └── lru-cache.ts                # medium, the key problem: DLL + Map
```

**Block is done when:** you implemented an LRU cache and can explain why a doubly linked list is exactly what makes every operation O(1).

---

## Block 6. Hash Table (~3–4 h)

**Theory:** hash functions, collisions, chaining vs open addressing, why average O(1); what's under the hood of Map/Set in JS.

**Implementation:** `HashTable<K, V>` with chaining: `set`, `get`, `delete`, `has`. Resizing is optional.

**Repo output:**
```
src/data-structures/hash-table/
├── HashTable.ts
└── problems/
    ├── first-unique-char.ts
    ├── group-anagrams.ts           # re-solve using your own HashTable, for fun
    └── longest-consecutive-sequence.ts   # medium
```

**Block is done when:** you can narrate what happens on `map.set(key, value)` all the way down to a collision.

---

## Block 7. Recursion (~3–4 h)

The gateway to trees, graphs, backtracking, and DP. "Grokking Algorithms", ch. 3.

**Theory:** base case + recursive case; the call stack; memoization.

**Repo output:**
```
src/algorithms/recursion/
├── fibonacci.ts                    # naive and memoized versions side by side, with a comment on the difference
├── pow.ts                          # fast exponentiation
└── sum-nested.ts                   # sum of an arbitrarily nested array
```

**Block is done when:** for any recursive function you can immediately name the base case and the stack depth.

---

## Block 8. Searching (~3–4 h)

**Theory:** "Grokking Algorithms", ch. 1; boundary handling (`left <= right`), midpoint overflow (not an issue in JS, but know it), the "binary search on the answer" pattern.

**Repo output:**
```
src/algorithms/searching/
├── linear-search.ts
├── binary-search.ts                # reference implementation, know it by heart
└── problems/
    ├── search-insert-position.ts
    ├── find-min-rotated.ts
    ├── search-rotated.ts
    └── koko-bananas.ts             # binary search on the answer
```

**Block is done when:** you understand why koko-bananas is binary search even though nothing is sorted.

---

## Block 9. Sorting (~4–5 h)

**Theory:** "Grokking Algorithms", ch. 2 and 4. Complexities of each, stability, when quicksort degrades to O(n²), what V8 uses in `Array.prototype.sort`.

**Repo output:**
```
src/algorithms/sorting/
├── bubble-sort.ts
├── selection-sort.ts
├── insertion-sort.ts
├── merge-sort.ts                   # the main one: implement carefully
├── quick-sort.ts
└── problems/
    ├── sort-colors.ts              # Dutch national flag
    └── merge-intervals.ts
```

**Block is done when:** you can trace merge sort on paper for an 8-element array and name the complexity of every sort you wrote without looking.

---

## Block 10. Binary Tree (~5–6 h)

**Theory:** terminology (root, leaf, height, depth); the four traversals; the recursive mindset of "answer = f(left subtree, right subtree)".

**Implementation:** `TreeNode<T>` + traversal functions (a tree is easier to keep as nodes + functions rather than a wrapper class).

**Repo output:**
```
src/data-structures/binary-tree/
├── TreeNode.ts
├── traversals.ts                   # preorder, inorder, postorder (recursive), levelOrder (with a queue)
└── problems/
    ├── max-depth.ts
    ├── invert-tree.ts
    ├── same-tree.ts
    ├── subtree-of-another.ts
    ├── level-order-traversal.ts
    └── diameter-of-tree.ts
```

**Block is done when:** you write any traversal without thinking; level-order uses your own queue from Block 3.

---

## Block 11. Binary Search Tree (~4–5 h)

**Theory:** the BST property; why in-order traversal yields sorted order; degeneration into a list and why balanced trees exist (AVL / red-black — concept only, no implementation).

**Implementation:** `BST`: `insert`, `find`, `min`, `max`. `delete` is optional (understand how it works; writing it is not required).

**Repo output:**
```
src/data-structures/bst/
├── BST.ts
└── problems/
    ├── validate-bst.ts
    ├── kth-smallest.ts
    └── lowest-common-ancestor.ts
```

**Block is done when:** you solved validate-bst with the min/max bounds approach, not just via in-order, and understand both.

---

## Block 12. Heap (~3–4 h)

**Theory:** min/max-heap, array storage (parent/child index formulas), siftUp/siftDown, complexities. When a heap beats sorting: you only need the top K.

**Implementation:** `MinHeap`: `insert`, `extractMin`, `peek`, `size`. One of the most useful implementations — JS has no built-in heap, so your own class will serve you in real tests too.

**Repo output:**
```
src/data-structures/heap/
├── MinHeap.ts
└── problems/
    ├── last-stone-weight.ts
    ├── kth-largest-element.ts
    ├── k-closest-points.ts
    └── top-k-frequent.ts           # re-solve using your own heap
```

**Block is done when:** you can derive the index formulas unaided and explain why insertion is O(log n).

---

## Block 13. Graphs (~7–9 h)

The biggest topic — don't rush it. "Grokking Algorithms", ch. 6.

**Theory:** adjacency list vs matrix; directed/weighted; a grid as a graph; BFS vs DFS — when to use which; topological sort (Kahn's algorithm); Dijkstra — idea only, implementation optional.

**Implementation:** `Graph` on an adjacency list: `addVertex`, `addEdge`, plus standalone `bfs.ts` and `dfs.ts` as reference templates.

**Repo output:**
```
src/data-structures/graph/
├── Graph.ts
├── bfs.ts                          # reference template, memorize
├── dfs.ts                          # reference template, memorize
├── topological-sort.ts
└── problems/
    ├── number-of-islands.ts        # the key problem of the block
    ├── max-area-of-island.ts
    ├── rotting-oranges.ts          # level-by-level BFS
    ├── clone-graph.ts
    ├── course-schedule.ts          # topological sort
    └── pacific-atlantic.ts
```

**Block is done when:** number-of-islands and course-schedule are solved on your own; you can justify the BFS vs DFS choice for every problem in the block.

---

## Block 14. Greedy + Backtracking (~4–5 h)

**Theory:** the greedy choice and why it isn't always correct; Kadane's algorithm; the backtracking template (choose → recurse → undo).

**Repo output:**
```
src/algorithms/greedy/
├── max-subarray.ts                 # Kadane
└── jump-game.ts
src/algorithms/backtracking/
├── subsets.ts
├── permutations.ts
├── combination-sum.ts
└── word-search.ts
```

**Block is done when:** you write the backtracking template from memory and understand why the undo step exists.

---

## Block 15. Dynamic Programming (~7–9 h)

The hardest part — going slowly is normal. "Grokking Algorithms", ch. 9 + NeetCode videos (1-D DP section).

**Theory:** state → transition → base case; top-down with memo → rewrite bottom-up; the link back to recursion from Block 7.

**Repo output:**
```
src/algorithms/dynamic-programming/
├── climbing-stairs.ts
├── min-cost-climbing-stairs.ts
├── house-robber.ts
├── house-robber-2.ts
├── coin-change.ts
├── longest-increasing-subsequence.ts
├── unique-paths.ts                 # 2-D
└── longest-common-subsequence.ts   # 2-D
```

**Block is done when:** for coin-change and LCS you can state the DP state and transition in words without looking at a solution.

---

## Block 16. Final: Review & Simulation (~5–7 h)

- [ ] Re-solve from scratch every problem marked "solved with help"
- [ ] 3–4 mixed sets of 4–5 random problems from NeetCode 150 — without knowing the topic
- [ ] 2–3 timed simulations: 3–4 problems in 90 minutes, no googling
- [ ] Finish the README: one line per structure — "what it is and when to use it" — with links to the files

**The checklist is done when:** you solve 3 out of 4 in a 90-minute simulation, and the README reads like your personal cheat sheet.

---

## Totals

| Part | Hours |
|---|---|
| Blocks 1–6 (techniques + linear structures) | ~20–25 |
| Blocks 7–12 (recursion, searching, sorting, trees, heap) | ~22–28 |
| Blocks 13–15 (graphs, greedy/backtracking, DP) | ~18–23 |
| Block 16 (final) | ~5–7 |
| **Total** | **~65–83** |

If you're running out of time: the mandatory core is Blocks 1, 2, 4, 6, 7, 8, 10, 13, 15. Compress first: Block 5 (doubly linked list — keep only LRU cache), Block 9 (implement merge sort only), Block 11 (BST without delete), Block 14 (2 problems each instead of 4).
