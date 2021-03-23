import itertools

def propose_in_route(distance_matrix, cycle):
    for i1, i2 in itertools.combinations(range(len(cycle)), 2):
        cost = 0
        cost -= distance_matrix[cycle[i1]][cycle[(i1-1)%len(cycle)]] + \
                distance_matrix[cycle[i1]][cycle[(i1+1)%len(cycle)]] + \
                distance_matrix[cycle[i2]][cycle[(i2-1)%len(cycle)]] + \
                distance_matrix[cycle[i2]][cycle[(i2+1)%len(cycle)]]

        cost += distance_matrix[cycle[i1]][cycle[(i2-1)%len(cycle)]] + \
                distance_matrix[cycle[i1]][cycle[(i2+1)%len(cycle)]] + \
                distance_matrix[cycle[i2]][cycle[(i1-1)%len(cycle)]] + \
                distance_matrix[cycle[i2]][cycle[(i1+1)%len(cycle)]]
        # returning cycle indexes to swap
        yield i1, i2, cost

def propose_between_routes(distance_matrix, cycle1, cycle2):
    for i1, i2 in itertools.product(range(len(cycle1)), range(len(cycle2))):
        cost = 0
        cost -= distance_matrix[cycle1[i1]][cycle1[(i1-1)%len(cycle1)]] + \
                distance_matrix[cycle1[i1]][cycle1[(i1+1)%len(cycle1)]] + \
                distance_matrix[cycle2[i2]][cycle2[(i2-1)%len(cycle2)]] + \
                distance_matrix[cycle2[i2]][cycle2[(i2+1)%len(cycle2)]]

        cost += distance_matrix[cycle1[i1]][cycle2[(i2-1)%len(cycle2)]] + \
                distance_matrix[cycle1[i1]][cycle2[(i2+1)%len(cycle2)]] + \
                distance_matrix[cycle2[i2]][cycle1[(i1-1)%len(cycle1)]] + \
                distance_matrix[cycle2[i2]][cycle1[(i1+1)%len(cycle1)]]
        # returning cycle1 index and cycle2 index to swap
        yield i1, i2, cost
