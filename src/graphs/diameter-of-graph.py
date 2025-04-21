""" Finding diameter of the graph """
from collections import deque

class Graph:
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_list = {v:[] for v in range(vno)}
    
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u].append((v,weight))
            self.adj_list[v].append((u,weight))
    
    def print_graph(self):
        for vertex,neighbor in self.adj_list.items():
            print(f'v {vertex} : {neighbor} ')



    def eccentricity(self,v):
        if v<0 or v>=self.vertex_count:
            return -1
        
        visited=[False]*self.vertex_count
        distance = [float('inf')]*self.vertex_count
        queue=deque()
        visited[v]=True
        distance[v]=0
        queue.append(v)
        while queue:
            current = queue.popleft()
            for neighbor, _ in self.adj_list[current]:
                if not visited[neighbor]:
                    visited[neighbor]=True
                    distance[neighbor]=distance[current]+1
                    queue.append(neighbor)
        max_distance = max(d for d in distance if d!=float('inf'))
        return max_distance
    
    def get_diameter(self):
        max_eccentricity = 0
        for v in range(self.vertex_count):
            ecc = self.eccentricity(v)
            max_eccentricity=max(max_eccentricity,ecc)
        return max_eccentricity


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
    diameter = graph.get_diameter()
    print(diameter)