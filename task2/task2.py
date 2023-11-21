from bfs import bfs
from Graph import UndergroundMap
import matplotlib.pyplot as plt


def min_edges_between_nodes(g, start, end):
    distances, _ = bfs(g, start)
    if distances[end] == float('inf'):
        # If end is not reachable from start_node
        return None
    return distances[end]


if __name__ == '__main__':
    map = UndergroundMap()
    map.create_data_base('../London Underground data.xlsx')
    grapth = map.get_graph()
    stations = map.get_station_indexes()
    stationA = input('Introduce the stationA: ').strip()
    stationB = input('Introduce the stationB: ').strip()

    min_edges = min_edges_between_nodes(grapth, stations[stationA] ,stations[stationB])

    if min_edges is not None:
        print(f"Minimum number of edges between {stationA} and {stationB}: {min_edges}")
    else:
        print(f"There is no path from {stationA} to {stationB}")

    all_durations = []
    for start_station in stations.values():
        for end_station in stations.values():
            min_edges = min_edges_between_nodes(grapth, start_station, end_station)
            if min_edges is not None:
                all_durations.append(min_edges)


    plt.figure(figsize=(8, 6))
    plt.hist(all_durations, bins=20, color='skyblue')
    plt.xlabel('Number of Stations')
    plt.ylabel('Frequency')
    plt.title('Distribution of Station Numbers between Station Pairs')
    plt.grid(True)
    plt.show()