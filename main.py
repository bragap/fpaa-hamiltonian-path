from typing import List

class Graph:
    def __init__(self, vertices: int):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, source: int, destination: int):
        self.graph[source][destination] = 1
        self.graph[destination][source] = 1  # For undirected graph. Remove this line for directed graph.

    def _is_safe(self, v: int, pos: int, path: List[int]) -> bool:
        if self.graph[path[pos - 1]][v] == 0:
            return False
        if v in path:
            return False
        return True

    def _hamiltonian_path_util(self, path: List[int], pos: int) -> bool:
        if pos == self.V:
            return self.graph[path[pos - 1]][path[0]] == 1

        for v in range(1, self.V):
            if self._is_safe(v, pos, path):
                path[pos] = v
                if self._hamiltonian_path_util(path, pos + 1):
                    return True
                path[pos] = -1
        return False

    def find_hamiltonian_path(self) -> List[int]:
        path = [-1] * self.V
        path[0] = 0
        if not self._hamiltonian_path_util(path, 1):
            return []
        return path


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 4)
    g.add_edge(3, 4)

    result = g.find_hamiltonian_path()

    if result:
        print("Hamiltonian Path found:")
        print(result)
    else:
        print("No Hamiltonian Path exists.")
