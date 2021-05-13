import math

def create_distance_matrix(coordinates: list):
    """
    Wykorzystuje zmienną coordinates i zwraca macierz odległości
    """
    distance_matrix = []

    for p in coordinates:
        distances = []
        for q in coordinates:
            dist = math.sqrt(math.pow(q[0] - p[0], 2) + math.pow(q[1] - p[1], 2))
            distances.append(round(dist, 0))
        distance_matrix.append(distances)

    return distance_matrix

def calculate_distance(distance_matrix, cycles) -> float:
    """
    Oblicza dystans na podstawie macierzy odległości i podanych cykli/ cyklu
    """
    if type(cycles[0]) is not list:
        cycles = [cycles]
    res = 0
    for cycle in cycles:
        for i in range(len(cycle)):
            res += distance_matrix[cycle[i-1]][cycle[i]]
    return res

