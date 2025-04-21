from collections import deque

class Graph:
    def __init__(self,vno:int):
        self.vertex_count = vno
        self.adj_list = {v:[] for v in range(vno)}

    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u].append((v,weight))
            self.adj_list[v].append((u,weight))
        else:
            print('Invalid vertices')

    def print_graph(self):
        for vertex,neighbor in self.adj_list.items():
            print(f' V {vertex} : {neighbor} ')

    def shortest_distance(self,start,end):
        visited = [False]*self.vertex_count
        distance = [float('inf')]*self.vertex_count
        queue=deque()
        visited[start]=True
        distance[start]=0
        queue.append(start)
        while queue:
            current = queue.popleft()
            for neighbor,_ in self.adj_list[current]:
                if not visited[neighbor]:
                    visited[neighbor]=True
                    distance[neighbor]=distance[current]+1
                    queue.append(neighbor)
        return distance[end] if distance[end]!=float('inf') else -1
    

    """eccentricity of a graph"""
    """The eccentricity of a Vertex: Maximum distance from a vertex to all other vertices is considered as the Eccentricity of that vertex.
    Note here we are talking about max distance of shortest path , in other words maximum shortest path / max(shortestpath)
    """
    def eccentricity(self,v):
        # validity of vertex
        if v<0 or v>=self.vertex_count:
            return -1
        
        visited = [False]*self.vertex_count
        distance = [float('inf')]*self.vertex_count
        queue=deque()
        visited[v]=True
        distance[v]=0
        queue.append(v)
        while queue:
            current = queue.popleft()
            for neighbor,_ in self.adj_list[current]:
                if not visited[neighbor]:
                    visited[neighbor]=True
                    distance[neighbor]=distance[current]+1
                    queue.append(neighbor)
        
        max_distance = max(d for d in distance if d!=float('inf'))
        return max_distance




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
    distance1=graph.shortest_distance(0,1)
    distance2=graph.shortest_distance(0,2)
    distance3=graph.shortest_distance(0,3)
    distance4=graph.shortest_distance(0,4)
    distance5=graph.shortest_distance(0,5)
    distance6=graph.shortest_distance(0,6)
    ecc = graph.eccentricity(0)
    print(distance1,distance2,distance3,distance4,distance5,distance6)
    print(ecc)



    # 0-1 min(1)
    # 0-2 min(3,1)
    # 0-3 min(3,1)
    # 0-4 min(6,4)
    # 0-5 min(5,3)
    # 0-6 min(4,2)