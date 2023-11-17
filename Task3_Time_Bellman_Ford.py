"""
Diana Nykonenko
Task 3 - the minimum time taken
Using Bellman Ford
"""

from bellman_ford import bellman_ford                                          # importing the class and the functiong from mst.py
from Graph import UndergroundMap                                               # importing the class UndergroundMap from Graph.py


if __name__ == "__main__":                                                     # testing whether sscript is being run directly


    tube_map = UndergroundMap()                                                # creating an instance of the class     
    tube_map.create_data_base('London Underground data.xlsx')                  # loading the data from the file
    tube_graph = tube_map.get_graph()                                          # getting the graph of the Tube Map
    stations = tube_map.get_station_indexes()                                  # getting indexes

    start_station = 'Holborn'                                                  # the starting point for the algorithm
    end_station = 'Highgate'                                                   # the ending point for the alghorithm
    end_index = int(stations.get(end_station))                                 # storing the index of the start station
    d, pi, cycle = bellman_ford(tube_graph, stations[start_station])           # calling the algorithm 


    """
    Lines used for testing:

    print(stations)                                                                                                                    
    print(end_index)                                                           
    print(d, pi, cycle)                                                       
    """


    min_time = int(d[end_index])                                               # finding the minimum time
    print("The mininmum travel time is", min_time, "minutes.")                 # printing the answer