import pandas as pd
from adjacency_list_graph import AdjacencyListGraph

class UndergroundMap():

    def __init__(self):
        # initialise the grapth
        self.graph = AdjacencyListGraph(270, directed=False, weighted=True)
        # initialise the station_index dictionary
        self.stations = {}

    def create_data_base(self, path):
        #read the data from excel
        self.data_set = pd.read_excel(path)

        # initialise the dict for indexes as well as it's place in the dict
        indexes = {}
        place = 0
        # iterate thorugh each of the rows in the data set
        for index, row in self.data_set.iterrows():
            station1 = row[1].strip()
            # check if the stations already have an index
            if station1 not in indexes:
                indexes[station1] = place
                place += 1

            station2 = row[2].strip()
            if station2 not in indexes:
                indexes[station2] = place
                place += 1
            weight = row[3]

            # chech if the edge between two stations already exists, if not, create
            if not self.graph.has_edge(indexes[station1], indexes[station2]):
                self.graph.insert_edge(indexes[station1], indexes[station2], weight=weight)
        self.stations = indexes

    def get_graph(self):
        return self.graph

    def get_station_indexes(self):
        return self.stations

if __name__ == '__main__':
    map = UndergroundMap()
    map.create_data_base('London Underground data.xlsx')
    graph = map.get_graph()
    stations = map.get_station_indexes()


    print(graph)
    print('Morden' in stations)
