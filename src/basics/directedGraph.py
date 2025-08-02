"""Building Basic Directed Graph"""
# Blog content Link : https://uchiha-vivek.github.io/Vivek-s-Blog/blogs/academia/Graphs/undirectedGraph.html

class Graph:
    def __init__(self,vno):
        self.vertex_count = vno
        self.adj_list  = {v:[] for v in range(vno)}
    
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u].append((v,weight))

    def print_graph(self):
        for vertex,neighbor in self.adj_list.items():
            print(f'Vertex {vertex} : {neighbor}')



if __name__=="__main__":
    graph=Graph(4)
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(2,3)
    graph.print_graph()