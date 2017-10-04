class MyGraph:
    def __init__(self):
        self.graph = {
            'A': ['B', 'C'],
            'B': ['C', 'D'],
            'C': ['D'],
            'D': ['C'],
            'E': ['F'],
            'F': ['C']
            }
    def arrayOfArcs(self):
        arcs = []
        for vertex, neighbors in self.graph.iteritems():
            for n in neighbors:
                arcs.append((vertex, n))
        return arcs


gr = MyGraph()
print gr.arrayOfArcs()
