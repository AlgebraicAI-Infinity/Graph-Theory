# https://www.geeksforgeeks.org/find-the-level-of-given-node-in-an-undirected-graph/

from collections import deque
class Graph:
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_list = {v:[] for v in range(vno)}
    
    # undirected graph
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u].append((v,weight))
            self.adj_list[v].append((u,weight))

    # printing graph
    def print_graph(self):
        for vertex,neighbor in self.adj_list.items():
            print(f'v {vertex} : {neighbor} ')

    # Level of graph
    def level(self, start, target) -> int:
        visited = [False] * self.vertex_count
        level = [-1] * self.vertex_count  # Default: -1 (not reachable)
        queue = deque()

        visited[start] = True
        level[start] = 0
        queue.append(start)

        while queue:
            current = queue.popleft()

            for neighbor, _ in self.adj_list[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    level[neighbor] = level[current] + 1
                    queue.append(neighbor)

                    if neighbor == target:
                        return level[neighbor]  # Return immediately when found

        return level[target]  # -1 if not reachable




if __name__=="__main__":
    graph = Graph(5)
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(1,3)
    graph.add_edge(2,4)
    graph.print_graph()
    ans=graph.level(0,4)
    print(ans)