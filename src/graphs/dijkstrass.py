""" implementation of BFS and Dijkstra's """
from collections import deque
import heapq

class Graph:
    def __init__(self, vno):
        self.vertex_count = vno
        self.adj_list = {v: [] for v in range(vno)}
    
    def add_edge(self, u, v, weight=1):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_list[u].append((v, weight))
            self.adj_list[v].append((u, weight))
    
    def print_graph(self):
        for vertex, neighbor in self.adj_list.items():
            print(f'V {vertex} : {neighbor}')
    
    def bfs(self, start):
        visited = [False] * self.vertex_count
        queue = deque()
        visited[start] = True
        queue.append(start)
        print('BFS Traversal ', end=' ')
        while queue:
            current = queue.popleft()
            print(current, end=' ')
            for neighbor, _ in self.adj_list[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

    def dijkstra(self, start):
        distances = [float('inf')] * self.vertex_count
        distances[start] = 0
        pq = [(0, start)]  # priority queue with (distance, vertex)
        
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            # If we find a longer distance in queue, we skip
            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.adj_list[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        print("\nDijkstra's shortest paths from vertex", start)
        for vertex, dist in enumerate(distances):
            print(f"Vertex {vertex} : Distance {dist}")

if __name__ == "__main__":
    graph = Graph(7)
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 6)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.print_graph()
    graph.bfs(0)
    graph.dijkstra(0)
