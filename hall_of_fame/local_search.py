from .propose import change_edges, change_edges_, edges
from .distance import calculate_distance
from copy import deepcopy

def steepest(distance_matrix, cycle1, cycle2):
    c1 = deepcopy(cycle1)
    c2 = deepcopy(cycle2)
    history = []
    while True:
        distance_before = calculate_distance(distance_matrix, (c1, c2))
        propositions: list = list(edges(c1, c2))

        options = []
        for p in propositions:
            dist = calculate_distance(distance_matrix, change_edges(p[0], p[1], p[2], c1, c2))
            options.append((dist, p[0], p[1], p[2]))

        distance_after, num, i1, i2 = min(options)
        if distance_before <= distance_after:
            break

        change_edges_(num, i1, i2, c1, c2)

        history.append([c1, c2])
        print(distance_after)

    return history

# powinien brać wszystkie propozycje i wybierać najlepszą spośród edges i nodes
