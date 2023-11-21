from single_source_shortest_paths import initialize_single_source
from Grapth import UndergroundMap
from dijkstra import dijkstra
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # Create the UndergroundMap and read the station data
    map = UndergroundMap()
    map.create_data_base('../London Underground data.xlsx')
    graph = map.get_graph()
    stations = map.get_station_indexes()

    start_station_name = input('Introduce the stationA: ').strip()
    end_station_name = input('Introduce the stationB: ').strip()

    # Find the shortest duration between the start and end stations
    shortest_durations, pi = dijkstra(graph, stations[start_station_name])

    # Display the shortest duration
    print(f"Shortest Duration: {shortest_durations[stations[end_station_name]]} minutes")

    # Calculate and plot the histogram of journey times between station pairs
    all_durations = []
    for start_station in stations.values():
        durations, pi = dijkstra(graph, start_station)
        for duration in durations:
            all_durations.append(duration)

    plt.figure(figsize=(8, 6))
    plt.hist(all_durations, bins=20, color='skyblue')
    plt.xlabel('Journey Durations (minutes)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Journey Times between Station Pairs')
    plt.grid(True)
    plt.show()
