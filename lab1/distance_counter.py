import math


def count_dist(coordinates):
    distance_matrix = []
    # node_id = 0

    for p in coordinates:
        distances = []
        for q in coordinates:
            dist = math.sqrt(math.pow(q[0] - p[0], 2) + math.pow(q[1] - p[1], 2))
            distances.append(round(dist, 0))
        distance_matrix.append(distances)
        # node_id += 1

    return distance_matrix

def calculate_distance(distance_matrix, cycle):
    res = 0
    for i in range(1, len(cycle)):
        res += distance_matrix[cycle[i-1]][cycle[i]]
    return res


