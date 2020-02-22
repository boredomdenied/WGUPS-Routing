import math

from controller import Interface


# Big-O time complexity of O(n^2)
# Nearest neighbor [A]takes the initial position and [B]a list of nodes, then [C]calculates the lowest value for
# distance between the current node and the remaining within the list. Once it finds this value, it [D]adds the node to
# the path list and [E]marks the current node as this lowest value node. [F]The process repeats until there is no more
# nodes left to visit. The [G]final path is returned


# [B] takes in our list
def run(arr, location_list, departure_time, max_distance=math.inf):
    # the final path to be returned after calculation is performed
    final_path = []
    # [A] sets initial node as HUB
    current_node = 0
    distance = 0
    # [F] iterate through all nodes until we have none left to visit
    while len(location_list) != 0:
        lowest_value = math.inf
        lowest_node = math.inf
        for n in location_list:
            # check if node greater than current, if so set value
            if current_node < n:
                value = arr[n][current_node]
            # check node less than current, if so set value
            elif n < current_node:
                value = arr[current_node][n]
            # [C] check if found value is lowest of all in list, if so it's set as lowest
            if value < lowest_value:
                # if lower than lowest value, set as lowest value and node
                lowest_value = value
                lowest_node = n
        # add distance of nearest neighbor for reporting
        distance += lowest_value
        # reset our remaining distance
        max_distance -= lowest_value
        # [D] add node to path
        final_path.append(lowest_node)
        # [E] reset current node
        current_node = lowest_node
        # remove node from starting list
        location_list.remove(lowest_node)
        # update package statuses of packages arriving on time
        if max_distance > 0:
            Interface.update(departure_time, distance, current_node)
    # travel back to HUB
    distance += [current_node][0]
    # [G]final path and distance are returned
    return final_path, distance
