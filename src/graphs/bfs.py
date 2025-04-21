""" implementation of BFS """
from collections import deque
class Graph:
    def __init__(self,vno):
        self.vertex_count = vno
        self.adj_list = {v:[]  for v in range(vno)}
    
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u].append((v,weight))
            self.adj_list[v].append((u,weight))
    
    def print_graph(self):
        for vertex,neighbor in self.adj_list.items():
            print(f'V {vertex} : {neighbor} ')

    def bfs(self,start):
        visited = [False]*self.vertex_count
        queue=deque()
        visited[start]=True
        queue.append(start)
        print(f'BFS Traversal ',end=' ')
        while queue:
            current = queue.popleft()
            print(current,end=' ')
            for neighbor,_ in self.adj_list[current]:
                if not visited[neighbor]:
                    visited[neighbor]=True
                    queue.append(neighbor)


if __name__=="__main__":
    graph = Graph(7)
    graph.add_edge(0,1)
    graph.add_edge(0,3)
    graph.add_edge(1,2)
    graph.add_edge(2,3)
    graph.add_edge(3,6)
    graph.add_edge(4,5)
    graph.add_edge(5,6)
    graph.print_graph()
    graph.bfs(0)