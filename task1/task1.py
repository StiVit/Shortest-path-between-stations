from Graph import UndergroundMap
from Dijkstra import dijkstra
import matplotlib.pyplot as plt
from datetime import datetime

def task1():
    # Create the UndergroundMap and read the station data
    map = UndergroundMap()
    map.create_data_base('../London Underground data.xlsx')
    graph = map.get_graph()
    # stations - dictionary with key: value as 'station name': in's numeral index
    stations = map.get_station_indexes()

    start_station_name = input('Introduce the stationA: ').strip()
    end_station_name = input('Introduce the stationB: ').strip()

    start = datetime.now()
    # Find the shortest duration between the start and end stations
    shortest_durations, _ = dijkstra(graph, stations[start_station_name])

    # Display the shortest duration
    print(f"Shortest Duration: {shortest_durations[stations[end_station_name]]} minutes")
    print(f'execution time: {(datetime.now()-start)}')

    start = datetime.now()
    # Calculate and plot the histogram of journey times between station pairs
    all_durations = []
    for start_station in stations.values():
        durations, _ = dijkstra(graph, start_station)
        for duration in durations:
            all_durations.append(duration)
    print(f'execution time of all station pairs: {(datetime.now() - start)}')

    plot_histogram(all_durations)

def plot_histogram(all_durations):
    plt.figure(figsize=(8, 6))
    plt.hist(all_durations, bins=20, color='skyblue')
    plt.xlabel('Journey Durations (minutes)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Journey Times between Station Pairs')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    task1()