"""
Diana Nykonenko
Task 3 - the minimum time taken
Using Bellman-Ford
"""

from Graph import UndergroundMap
from bellman_ford import bellman_ford
import matplotlib.pyplot as plt
import time

def task3(stationA, stationB):
    tube_map = UndergroundMap()  # creating an instance of the class
    tube_map.create_data_base('London Underground data.xlsx')  # loading the data from the file
    tube_graph = tube_map.get_graph()  # getting the graph of the Tube Map
    stations = tube_map.get_station_indexes()  # getting indexes

    end_index = stations[stationB]                                        # storing the index of the start station
    d, pi, cycle = bellman_ford(tube_graph, stations[stationA])           # calling the algorithm


    start = time.time()                                                        # record time point
    min_time = int(d[end_index])                                               # finding the minimum time
    end = time.time()                                                          # record time point
    timer = end - start                                                        # getting the final time
    print("The mininmum travel time: ", min_time, " minutes.")                 # printing the answer
    print("Time taken by the algorithm - ", timer)                             # total time

    # Calculate and plot the histogram of journey times between station pairs
    all_durations = []
    for start_station in stations.values():
        durations, pi, no_negative_cycle = bellman_ford(tube_graph, start_station)
        for duration in durations:
            all_durations.append(duration)

    # draw_histogram(all_durations)


def draw_histogram(all_durations):
    plt.figure(figsize=(8, 6))
    plt.hist(all_durations, bins=20, color='skyblue')
    plt.xlabel('Journey Durations (minutes)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Journey Times between Station Pairs')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    stationA = input('Introduce the stationA: ').strip()
    stationB = input('Introduce the stationB: ').strip()
    task3(stationA, stationB)

