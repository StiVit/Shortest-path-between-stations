from bfs import bfs
from Graph import UndergroundMap
import matplotlib.pyplot as plt
from datetime import datetime


def min_edges_between_nodes(g, start, end):
    distances, _ = bfs(g, start)
    if distances[end] == float('inf'):
        # If end is not reachable from start_node
        return None
    # it adds in the list itself, because of that -1
    return distances[end]-1


def Task2():
    # Reading Excel file and creating the graph
    map = UndergroundMap()
    map.create_data_base('../London Underground data.xlsx')
    grapth = map.get_graph()
    # stations - dictionary with key: value as 'station name': in's numeral index
    stations = map.get_station_indexes()

    stationA = input('Introduce the stationA: ').strip()
    stationB = input('Introduce the stationB: ').strip()

    start = datetime.now()
    # calculating min number of vertices between two stations using bfs
    min_edges = min_edges_between_nodes(grapth, stations[stationA], stations[stationB])
    if min_edges is not None:
        print(f"Minimum number of edges between {stationA} and {stationB}: {min_edges}")
    else:
        print(f"There is no path from {stationA} to {stationB}")
    print(f'execution time: {(datetime.now()-start)}')

    start = datetime.now()
    all_durations = []
    for start_station in stations.values():
        for end_station in stations.values():
            min_edges = min_edges_between_nodes(grapth, start_station, end_station)
            if min_edges is not None:
                all_durations.append(min_edges)
    print(f'execution time of all station pairs: {(datetime.now() - start)}')

    plot_histogram(all_durations)


def plot_histogram(all_durations):
    plt.figure(figsize=(8, 6))
    plt.hist(all_durations, bins=20, color='skyblue')
    plt.xlabel('Station Numbers')
    plt.ylabel('Frequency')
    plt.title('Distribution of Number of Stations between Station Pairs')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    Task2()