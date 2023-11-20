from single_source_shortest_paths import initialize_single_source
from Grapth import UndergroundMap
import matplotlib.pyplot as plt

def dijkstra(G, start_station, end_station):
    # Initialize distances and predecessors
    d, _ = initialize_single_source(G, start_station)

    # Create a simple list as a priority queue and a set to track visited stations
    queue = []
    visited = set()

    # Extract station with minimum distance from the queue
    def extract_min(queue, d):
        min_station = None
        min_distance = float('inf')
        for station in queue:
            if d[station] < min_distance:
                min_distance = d[station]
                min_station = station
        queue.remove(min_station)
        return min_station

    # Add the start station to the queue
    queue.append(start_station)

    # Loop until the queue is not empty
    while queue:
        # Extract station with minimum distance
        u = extract_min(queue, d)
        # Check if the end station is reached
        if u == end_station:
            break
        # Skip if the station has already been visited
        if u in visited:
            continue
        # Mark the station as visited
        visited.add(u)

        # Iterate through adjacent stations
        for edge in G.get_adj_list(u):
            v = edge.get_v()
            weight = edge.get_weight()
            # Relax the edges to find the shortest distance
            if d[v] > d[u] + weight:
                d[v] = d[u] + weight
                queue.append(v)  # Add station to the queue

    shortest_time = d[end_station]

    return shortest_time

if __name__ == "__main__":
    # Create the UndergroundMap and read the station data
    map = UndergroundMap()
    map.create_data_base('London Underground data.xlsx')
    london_underground_graph = map.get_graph()
    stations = map.get_station_indexes()

    start_station_name = 'Holborn'
    end_station_name = 'Moor Park'

    # Find the shortest duration between the start and end stations
    shortest_duration = dijkstra(london_underground_graph, stations[start_station_name],
                                 stations[end_station_name])

    # Display the shortest duration
    print(f"Shortest Duration: {shortest_duration} minutes")

    # Calculate and plot the histogram of journey times between station pairs
    all_durations = []
    for start_station in stations.values():
        for end_station in stations.values():
            duration = dijkstra(london_underground_graph, start_station, end_station)
            all_durations.append(duration)

    plt.figure(figsize=(8, 6))
    plt.hist(all_durations, bins=20, color='skyblue')
    plt.xlabel('Journey Durations (minutes)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Journey Times between Station Pairs')
    plt.grid(True)
    plt.show()
