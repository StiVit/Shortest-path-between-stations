from Grapth import UndergroundMap
from bellman_ford import bellman_ford
import matplotlib.pyplot as plt

def task3(stationA, stationB):
    grapth = UndergroundMap()
    grapth.create_data_base('../London Underground data.xlsx')
    stations = grapth.get_station_indexes()
    grapth = grapth.get_graph()

    durations, predecessors, no_negative_cycle = bellman_ford(grapth, stations[stationA])

    print(durations[stations[stationB]])

    # Calculate and plot the histogram of journey times between station pairs
    all_durations = []
    for start_station in stations.values():
        durations, pi, no_negative_cycle = bellman_ford(grapth, start_station)
        for duration in durations:
            all_durations.append(duration)

    plt.figure(figsize=(8, 6))
    plt.hist(all_durations, bins=20, color='skyblue')
    plt.xlabel('Journey Durations (minutes)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Journey Times between Station Pairs')
    plt.grid(True)
    plt.show()



if __name__ == '__main__':
    task3('Tottenham Court Road', 'Barking')

