import pandas as pd
import networkx as nx

class UndergroundMap():
    def __init__(self):
        self.graph = nx.Graph()

    def create_data_base(self, path):
        self.data_set = pd.read_excel(path)
        for index, row in self.data_set.iterrows():
            station1 = row[1]
            station2 = row[2]
            weight = row[3]
            self.graph.add_edge(station1, station2, weight=weight)

    def get_graph(self):
        return self.graph

map = UndergroundMap()
map.create_data_base('London Underground data.xlsx')
graph = map.get_graph()


# Task 2, e.g. Holdorn-Mile End
shortest_path = nx.shortest_path_length(graph, source='Holborn', target='Mile End', weight='weight')
print("Shortest travel time:", shortest_path)
# Task 1, same example
shortest_path = nx.shortest_path(graph, source='Holborn', target='Mile End', weight='weight')
print("Shortest path:", shortest_path)