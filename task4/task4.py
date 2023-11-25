from mst import kruskal
from Graph import UndergroundMap
from task1.Dijkstra import dijkstra
from datetime import datetime
import matplotlib.pyplot as plt

def task4(G, stations):
    start = datetime.now()
    optimised_graph = kruskal(G)
    print(f'MST made in: {datetime.now() - start}')
    edges_optimised = optimised_graph.get_edge_list()
    edges_main = G.get_edge_list()
    keys = list(stations.keys())

    for edge in edges_main:
        if edge not in edges_optimised:
            print(f'{keys[edge[0]]} -- {keys[edge[1]]}')

    all_durations = []
    for start_station in range(optimised_graph.get_card_V()):
        durations, _ = dijkstra(optimised_graph, start_station)
        for duration in durations:
            all_durations.append(duration)

    draw_histogram(all_durations)

def draw_histogram(all_durations):
    plt.figure(figsize=(8, 6))
    plt.hist(all_durations, bins=20, color='skyblue')
    plt.xlabel('Journey Durations (minutes)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Journey Times between Station Pairs After Optimising')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    graph = UndergroundMap()
    graph.create_data_base('../London Underground data.xlsx')
    stations = graph.get_station_indexes()
    graph = graph.get_graph()

    task4(graph, stations)