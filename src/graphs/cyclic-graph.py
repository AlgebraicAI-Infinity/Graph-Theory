"""Connected Graph"""

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
            print(f' v {vertex} : {neighbor} ')


if __name__=="__main__":
    graph = Graph(3)
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(1,2)
    graph.print_graph()