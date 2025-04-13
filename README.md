# Project: Hamiltonian Path in Python

##  Project Description
This project aims to implement an algorithm to find a Hamiltonian Path in a graph (directed or undirected). A Hamiltonian Path is a path that visits each vertex exactly once.

The algorithm was implemented using **backtracking** and is available in the `main.py` file. The graph is represented by an adjacency matrix.

---

##  Algorithm Explanation (line by line)

### Class `Graph`
```python
class Graph:
    def __init__(self, vertices: int):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
```
Initializes a graph with `V` vertices, represented by an adjacency matrix.

```python
    def add_edge(self, source: int, destination: int):
        self.graph[source][destination] = 1
        self.graph[destination][source] = 1  # bidirectional (remove for directed graph)
```
Adds an edge between two vertices. In the undirected case, it adds in both directions.

```python
    def _is_safe(self, v: int, pos: int, path: List[int]) -> bool:
        if self.graph[path[pos - 1]][v] == 0:
            return False
        if v in path:
            return False
        return True
```
Checks whether it's safe to add vertex `v` at position `pos` in the path.

```python
    def _hamiltonian_path_util(self, path: List[int], pos: int) -> bool:
        if pos == self.V:
            return self.graph[path[pos - 1]][path[0]] == 1
```
Base case: if all vertices are included, check if the last connects to the first (cycle).

```python
        for v in range(1, self.V):
            if self._is_safe(v, pos, path):
                path[pos] = v
                if self._hamiltonian_path_util(path, pos + 1):
                    return True
                path[pos] = -1
        return False
```
Try vertices one by one. If it doesn't work, backtrack.

```python
    def find_hamiltonian_path(self) -> List[int]:
        path = [-1] * self.V
        path[0] = 0
        if not self._hamiltonian_path_util(path, 1):
            return []
        return path
```
Main function that initializes the path and starts the recursion.

---

##  How to Run the Project

1. **Clone the repository:**
```bash
git clone https://github.com/bragap/fpaa-hamiltonian-path
cd fpaa-hamiltonian-path
```

2. **Run the script:**
```bash
python main.py
```

The program will display the Hamiltonian Path found or indicate that none exists.

---

## Hamiltonian Path Visualization 

This project also includes a `view.py` file that uses **NetworkX** and **Matplotlib** to:
- Draw the **original graph**.
- **Highlight** the edges of the Hamiltonian Path (if found).
- Export the visual result as a PNG image to the `assets/` folder.

### Install required libraries:
```bash
pip install networkx matplotlib
```

### Run the visualizer:
```bash
python view.py
```

An image `assets/graph.png` will be generated showing the graph with the Hamiltonian Path highlighted in red.

---

## Technical Report

### 1. Complexity Classes (P, NP, NP-Complete, NP-Hard)
- The **Hamiltonian Path problem** belongs to the **NP-Complete** class.
- It is in **NP** because a solution can be verified in polynomial time.
- It is **NP-Complete** because it is as hard as any problem in NP, and no polynomial-time algorithm is known.
- Closely related to the **Traveling Salesman Problem (TSP)**, which is **NP-Hard**.

### 2. Asymptotic Time Complexity

#### Algorithm used: backtracking
- **Worst case**: the algorithm tries all possible permutations of vertices.
- Time complexity is **O(n!)**, where n is the number of vertices.

### 3. Application of the Master Theorem

The Master Theorem is used for solving recurrences of the form:
```
T(n) = aT(n/b) + f(n)
```
In this case, the algorithm does not follow this pattern, as it is **combinatorial** and based on **permutations**. Therefore:
- **Master Theorem is not applicable**.
- Complexity was determined through **operation counting** and **combinatorial analysis**.

### 4. Complexity Case Analysis

- **Best case:** Hamiltonian Path is found quickly. Still O(n!), but fast in practice.
- **Average case:** Depends on the graph structure and attempt order. Usually slow for large graphs.
- **Worst case:** Explores **all possible permutations** and **finds no path**. Complexity: O(n!).

**Impact:** The algorithm works well for small graphs but does **not scale** due to factorial growth.

---

## Conclusion
This project demonstrates the practical complexity of solving NP-Complete problems. Through backtracking, it is possible to find exact solutions, but with performance limitations on large instances. Ideal for academic studies and understanding computational limits in graph problems.

