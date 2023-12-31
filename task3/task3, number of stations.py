from bellman_ford import bellman_ford
import time
import pandas as pd
from adjacency_list_graph import AdjacencyListGraph

class UndergroundMap:

    def __init__(self):
        # initialise the graph
        self.graph = AdjacencyListGraph(270, directed=False, weighted=True)
        # initialise the station_index dictionary
        self.stations = {}

    def create_data_base(self, path):
        # read the data from excel
        self.data_set = pd.read_excel(path)

        # initialise the dict for indexes as well as it's place in the dict
        indexes = {}
        place = 0
        # iterate through each of the rows in the data set
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
            weight = 1 # Change weight to 1
            # This allows for the Bellman ford algorithm to prioritise the smallest number of stations traversed. So
            # for example say Station A to B is 10 stops long but originally 15 in total weight and another route via
            # station C is 6 stops long but 20 in total weight. Bellman ford will find a route from A to B via the
            # normal route. However, when changing all weights to 1, the Bellman Ford Algorithm will now find Station
            # A to B via C as the 6 stops have less weight (6 < 10) and thus should output this.

            # check if the edge between two stations already exists, if not, create
            if not self.graph.has_edge(indexes[station1], indexes[station2]):
                self.graph.insert_edge(indexes[station1], indexes[station2], weight=weight)
        self.stations = indexes

    def get_graph(self):
        return self.graph

    def get_station_indexes(self):
        return self.stations


def get_user_input():
    user_start_station = input("Enter the start station").strip()  # check for whitespace and the beginning or end
    user_end_station = input("Enter the end station").strip()
    return user_start_station, user_end_station


def get_number_of_stations(n_start, n_end):
    list_of_previous = get_list_previous(n_start, n_end)
    return len(list_of_previous)


def get_list_previous(f_start, f_end):
    # This part is to trace back on itself to find the number of stations between the start and end stations
    # It basically uses the predecessors returned by the bellman ford algorithm.
    # it starts by getting the position of the end station's predecessor
    # it then uses a do while loop to get the predecessor of the next station.
    # This keeps looping until the start station is reached.
    new_pos = pi[pos_of_station[f_end]]
    list_of_previous = []
    # list out keys and values separately
    key_list = list(pos_of_station.keys())
    val_list = list(pos_of_station.values())
    while True:  # using a do while loop

        if new_pos != pos_of_station[f_start]:  # check if the trace back as reached the starting station

            position = val_list.index(new_pos)
            list_of_previous.append((key_list[position]))  # create a list of previous stations

            new_pos = pi[pos_of_station[key_list[position]]]
            continue
        else:
            break
    return list_of_previous


if __name__ == "__main__":
    start_station, end_station = get_user_input()  # get the start station and end station from user

    start = time.time() # check time taken

    underground_map = UndergroundMap()  # Creating an instance of the UndergroundMap class from Graph.py

    underground_map.create_data_base('London Underground data.xlsx')  # Load data into the graph from the
    # provided. Weights all set to one.

    london_underground_graph = underground_map.get_graph()  # Get the graph representing the London Underground
    pos_of_station = underground_map.get_station_indexes()  # get the dict of stations positions within the index
    graph = underground_map.get_graph()

    d, pi, cycle = bellman_ford(london_underground_graph, pos_of_station[start_station])  # use the bellman ford
    # search algorithm to find the shortest path to every single station

    user_number_stops = get_number_of_stations(start_station, end_station)
    list_of_stations_to_end = get_list_previous(start_station, end_station)
    print(f'The stations between {start_station} and {end_station} is {list_of_stations_to_end}')
    print(f'Number of stops between {start_station} and {end_station} is {user_number_stops} ')

    end = time.time()
    print(f'The time taken is {end - start}')