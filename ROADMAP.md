# Algorithms & Data Structures — Study Checklist (~60–70 hours)

Format for each topic: theory → implement the data structure in this repo → solve problems as files in this repo → verify on LeetCode. Blocks must be completed strictly in order (they are arranged by dependency). The plan is language-agnostic — use whatever language you're interviewing in.

## Ground Rules

- [ ] **The 30-minute rule:** stuck with no progress — watch an explanation (NeetCode), mark the problem, and re-solve it from scratch 3–4 days later
- [ ] Implementing a structure should take 1–2 evenings max: core operations only, no API polishing. Roughly 30% of time on implementations, 70% on problems
- [ ] Solve each problem as a file in the repo first (with a sample call at the bottom so the file runs directly), then submit on LeetCode to verify
- [ ] File names in the trees below have no extensions — add your language's extension
- [ ] Keep a log: problem / solved on my own or with help / re-solve date

---

## Block 1. Warm-up: Two Pointers, Sliding Window, Prefix Sums (~5–6 h)

No data structures here — pure techniques.

**Theory:** when each pattern applies (sorted input → two pointers; subarray/substring → sliding window; range sums → prefix sums).

**Repo output:**
```
src/algorithms/two-pointers/
├── two-sum-sorted
├── three-sum
├── container-with-most-water
└── move-zeroes
src/algorithms/sliding-window/
├── best-time-to-buy-sell-stock
├── longest-substring-no-repeat
└── permutation-in-string
src/algorithms/prefix-sum/
├── range-sum-query
├── subarray-sum-equals-k
└── product-of-array-except-self
```

**LeetCode to verify:** submit the problems solved in the repo — Move Zeroes (easy), Two Sum II — Input Array Is Sorted (medium), 3Sum (medium), Container With Most Water (medium); Best Time to Buy and Sell Stock (easy), Longest Substring Without Repeating Characters (medium), Permutation in String (medium); Range Sum Query — Immutable (easy), Subarray Sum Equals K (medium), Product of Array Except Self (medium).

**Block is done when:** you recognize the pattern from the problem statement before writing any code.

---

## Block 2. Stack (~3–4 h)

**Theory:** LIFO, operation complexities, the call stack as a stack, monotonic stack.

**Implementation:** a `Stack` class backed by a dynamic array: `push`, `pop`, `peek`, `is_empty`, `size`.

**Repo output:**
```
src/data-structures/stack/
├── stack                      # implementation
└── problems/
    ├── valid-parentheses
    ├── min-stack
    ├── evaluate-rpn
    └── daily-temperatures     # monotonic stack
```

**LeetCode to verify:** submit the problems solved in the repo — Valid Parentheses (easy), Min Stack (medium), Evaluate Reverse Polish Notation (medium), Daily Temperatures (medium). If it felt easy — additionally Car Fleet (medium).

**Block is done when:** you solved daily-temperatures and can explain why a monotonic stack gives O(n).

---

## Block 3. Queue (~2–3 h)

**Theory:** FIFO; why a naive array-based queue (removing from the front) costs O(n) and how to avoid it: circular buffer, two stacks, or linked nodes; deque. Also check what ready-made queue/deque your language's standard library offers.

**Implementation:** a `Queue` class on linked nodes or two stacks: `enqueue`, `dequeue`, `peek`, `is_empty`, `size`.

**Repo output:**
```
src/data-structures/queue/
├── queue                      # implementation
└── problems/
    ├── queue-using-stacks
    ├── recent-counter
    └── sliding-window-maximum # deque, medium/hard — OK to solve with help
```

**Block is done when:** you can explain why BFS needs a queue (you'll use this in Blocks 10 and 13).

---

## Block 4. Singly Linked List (~4–5 h)

**Theory:** nodes and references; complexity comparison with arrays; fast/slow pointer technique; dummy head node.

**Implementation:** a `SinglyLinkedList` class: `push_front`, `push_back`, `pop_front`, `insert_at`, `remove_at`, `find`, `to_array`.

**Repo output:**
```
src/data-structures/linked-list-singly/
├── singly-linked-list         # implementation
└── problems/
    ├── reverse-list           # iterative AND recursive, two functions
    ├── find-middle            # fast/slow
    ├── merge-two-sorted-lists
    ├── has-cycle              # Floyd's algorithm
    ├── remove-nth-from-end
    └── reorder-list           # medium, combines middle + reverse + merge
```

**Block is done when:** you write reverse-list in 5 minutes with no mistakes; you solved reorder-list by spotting the three previous problems inside it.

---

## Block 5. Doubly Linked List (~2–3 h)

**Theory:** why the backward reference matters; real-world uses (browser history, LRU cache).

**Implementation:** a `DoublyLinkedList` class: `push_front`, `push_back`, `pop_front`, `pop_back`, `remove(node)` in O(1).

**Repo output:**
```
src/data-structures/linked-list-doubly/
├── doubly-linked-list         # implementation
└── problems/
    ├── browser-history
    └── lru-cache              # medium, the key problem: DLL + hash map
```

**Block is done when:** you implemented an LRU cache and can explain why a doubly linked list is exactly what makes every operation O(1).

---

## Block 6. Hash Table (~3–4 h)

**Theory:** hash functions, collisions, chaining vs open addressing, why average O(1); how your language's built-in hash map (dict/Map) works under the hood.

**Implementation:** a `HashTable` class with chaining: `set`, `get`, `delete`, `has`. Resizing is optional.

**Repo output:**
```
src/data-structures/hash-table/
├── hash-table                 # implementation
└── problems/
    ├── first-unique-char
    ├── group-anagrams         # re-solve using your own HashTable, for fun
    └── longest-consecutive-sequence   # medium
```

**Block is done when:** you can narrate what happens when a key is inserted into the built-in hash map — all the way down to a collision.

---

## Block 7. Recursion (~3–4 h)

The gateway to trees, graphs, backtracking, and DP. "Grokking Algorithms", ch. 3.

**Theory:** base case + recursive case; the call stack; your language's recursion depth limit and what happens when it's exceeded; memoization.

**Repo output:**
```
src/algorithms/recursion/
├── fibonacci                  # naive and memoized versions side by side, with a comment on the difference
├── pow                        # fast exponentiation
└── sum-nested                 # sum of an arbitrarily nested array
```

**Block is done when:** for any recursive function you can immediately name the base case and the stack depth.

---

## Block 8. Searching (~3–4 h)

**Theory:** "Grokking Algorithms", ch. 1; boundary handling (`left <= right`), midpoint overflow (relevant in some languages, not in others — know it either way), the "binary search on the answer" pattern.

**Repo output:**
```
src/algorithms/searching/
├── linear-search
├── binary-search              # reference implementation, know it by heart
└── problems/
    ├── search-insert-position
    ├── find-min-rotated
    ├── search-rotated
    └── koko-bananas           # binary search on the answer
```

**Block is done when:** you understand why koko-bananas is binary search even though nothing is sorted.

---

## Block 9. Sorting (~4–5 h)

**Theory:** "Grokking Algorithms", ch. 2 and 4. Complexities of each, stability, when quicksort degrades to O(n²), which algorithm your language's built-in sort uses.

**Repo output:**
```
src/algorithms/sorting/
├── bubble-sort
├── selection-sort
├── insertion-sort
├── merge-sort                 # the main one: implement carefully
├── quick-sort
└── problems/
    ├── sort-colors            # Dutch national flag
    └── merge-intervals
```

**Block is done when:** you can trace merge sort on paper for an 8-element array and name the complexity of every sort you wrote without looking.

---

## Block 10. Binary Tree (~5–6 h)

**Theory:** terminology (root, leaf, height, depth); the four traversals; the recursive mindset of "answer = f(left subtree, right subtree)".

**Implementation:** a `TreeNode` class + traversal functions (a tree is easier to keep as nodes + functions rather than a wrapper class).

**Repo output:**
```
src/data-structures/binary-tree/
├── tree-node                  # node implementation
├── traversals                 # preorder, inorder, postorder (recursive), level-order (with a queue)
└── problems/
    ├── max-depth
    ├── invert-tree
    ├── same-tree
    ├── subtree-of-another
    ├── level-order-traversal
    └── diameter-of-tree
```

**Block is done when:** you write any traversal without thinking; level-order uses your own queue from Block 3.

---

## Block 11. Binary Search Tree (~4–5 h)

**Theory:** the BST property; why in-order traversal yields sorted order; degeneration into a list and why balanced trees exist (AVL / red-black — concept only, no implementation).

**Implementation:** a `BST` class: `insert`, `find`, `min`, `max`. `delete` is optional (understand how it works; writing it is not required).

**Repo output:**
```
src/data-structures/bst/
├── bst                        # implementation
└── problems/
    ├── validate-bst
    ├── kth-smallest
    └── lowest-common-ancestor
```

**Block is done when:** you solved validate-bst with the min/max bounds approach, not just via in-order, and understand both.

---

## Block 12. Heap (~3–4 h)

**Theory:** min/max-heap, array storage (parent/child index formulas), siftUp/siftDown, complexities. When a heap beats sorting: you only need the top K.

**Implementation:** a `MinHeap` class: `insert`, `extract_min`, `peek`, `size`. Even if your language's standard library ships a heap — write your own for understanding, then learn the built-in one too (real tests will call for both).

**Repo output:**
```
src/data-structures/heap/
├── min-heap                   # implementation
└── problems/
    ├── last-stone-weight
    ├── kth-largest-element
    ├── k-closest-points
    └── top-k-frequent         # re-solve using your own heap
```

**Block is done when:** you can derive the index formulas unaided and explain why insertion is O(log n).

---

## Block 13. Graphs (~7–9 h)

The biggest topic — don't rush it. "Grokking Algorithms", ch. 6.

**Theory:** adjacency list vs matrix; directed/weighted; a grid as a graph; BFS vs DFS — when to use which; topological sort (Kahn's algorithm); Dijkstra — idea only, implementation optional.

**Implementation:** a `Graph` class on an adjacency list: `add_vertex`, `add_edge`, plus standalone `bfs` and `dfs` files as reference templates.

**Repo output:**
```
src/data-structures/graph/
├── graph                      # implementation
├── bfs                        # reference template, memorize
├── dfs                        # reference template, memorize
├── topological-sort
└── problems/
    ├── number-of-islands      # the key problem of the block
    ├── max-area-of-island
    ├── rotting-oranges        # level-by-level BFS
    ├── clone-graph
    ├── course-schedule        # topological sort
    └── pacific-atlantic
```

**Block is done when:** number-of-islands and course-schedule are solved on your own; you can justify the BFS vs DFS choice for every problem in the block.

---

## Block 14. Greedy + Backtracking (~4–5 h)

**Theory:** the greedy choice and why it isn't always correct; Kadane's algorithm; the backtracking template (choose → recurse → undo).

**Repo output:**
```
src/algorithms/greedy/
├── max-subarray               # Kadane
└── jump-game
src/algorithms/backtracking/
├── subsets
├── permutations
├── combination-sum
└── word-search
```

**Block is done when:** you write the backtracking template from memory and understand why the undo step exists.

---

## Block 15. Dynamic Programming (~7–9 h)

The hardest part — going slowly is normal. "Grokking Algorithms", ch. 9 + NeetCode videos (1-D DP section).

**Theory:** state → transition → base case; top-down with memo → rewrite bottom-up; the link back to recursion from Block 7.

**Repo output:**
```
src/algorithms/dynamic-programming/
├── climbing-stairs
├── min-cost-climbing-stairs
├── house-robber
├── house-robber-2
├── coin-change
├── longest-increasing-subsequence
├── unique-paths               # 2-D
└── longest-common-subsequence # 2-D
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
