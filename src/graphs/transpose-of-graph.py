

class Graph:
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_list = {v:[] for v in range(vno)}
    
    def add_edge(self,u,v,weight=1):
        self.adj_list[u].append((v,weight))

    def print_graph(self):
        for vertex,neighbor in self.adj_list.items():
            print(f'v :{vertex} : {neighbor}')

    def get_transpose(self):
        transpose = Graph(self.vertex_count)
        for u in self.adj_list:
            for v,weight in self.adj_list[u]:
                transpose.add_edge(v,u,weight)
        return transpose
    

if __name__=="__main__":
    g=Graph(4)
    g.add_edge(0,1)
    g.add_edge(1,2)
    g.add_edge(2,3)
    g.print_graph()
    transpose=g.get_transpose()
    transpose.print_graph()