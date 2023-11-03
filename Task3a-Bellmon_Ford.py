from Graph import UndergroundMap
from bellman_ford import bellman_ford
import matplotlib.pyplot as plt


def get_user_input():
    user_start_station = input("Enter the start station")
    user_end_station = input("Enter the end station")
    return user_start_station, user_end_station


def get_number_of_stations():
    # This part is to trace back on itself to find the number of stations between the start and end stations
    # It basically uses the predecessors returned by the bellman ford algorithm.
    # it starts by getting the position of the end station's predecessor
    # it then uses a do while loop to get the predecessor of the next station.
    # This keeps looping until the start station is reached.
    new_pos = pi[pos_of_station[end_station]]
    list_of_previous = []
    while True:  # using a do while loop

        if new_pos != pos_of_station[start_station]:  # check if the trace back as reached the starting station
            # list out keys and values separately
            key_list = list(pos_of_station.keys())
            val_list = list(pos_of_station.values())

            position = val_list.index(new_pos)
            list_of_previous.append((key_list[position]))  # create a list of previous stations

            new_pos = pi[pos_of_station[key_list[position]]]
            continue
        else:
            break
    print(f'Number of stations between {start_station} and {end_station} is {len(list_of_previous) + 1}')


if __name__ == "__main__":
    map = UndergroundMap()  # Creating an instance of the UndergroundMap class from Graph.py
    map.create_data_base('London Underground data.xlsx')  # Load data into the graph from the provided Excel file
    london_underground_graph = map.get_graph()  # Get the graph representing the London Underground
    pos_of_station = map.get_station_indexes()  # get the dict of stations positions within the index

    start_station, end_station = get_user_input()  # get the start station and end station from user

    d, pi, cycle = bellman_ford(london_underground_graph, pos_of_station[start_station])  # use the bellman ford
    # search algorithm to find the shortest path to every single station

    print(f'Time taken from {start_station} to {end_station} is {d[pos_of_station[end_station]]} minutes')  # Print the
    # time taken from start station to end

    get_number_of_stations()
