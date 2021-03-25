from copy import deepcopy
import time

def make_change(cycle1, cycle2, num, i1, i2):
    if num == 0:
        cycle1[i1], cycle1[i2] = cycle1[i2], cycle1[i1]
    elif num == 1:
        cycle2[i1], cycle2[i2] = cycle2[i2], cycle2[i1]
    elif num == 2:
        cycle1[i1], cycle2[i2] = cycle2[i2], cycle1[i1]
    else:
        print('Wrong num value:', num)


def greedy(distance_matrix, c1, c2, propose_method):
    cycle1 = deepcopy(c1)
    cycle2 = deepcopy(c2)
    while True:
        for gain, i1, i2, num in propose_method(distance_matrix, cycle1, cycle2):
            if gain > 0:
                make_change(cycle1, cycle2, num, i1, i2)
                break
        else:
            break
    return cycle1, cycle2


def steepest(distance_matrix, c1, c2, propose_method):
    cycle1 = deepcopy(c1)
    cycle2 = deepcopy(c2)
    while True:
        gain, i1, i2, num = max(list(propose_method(distance_matrix, cycle1, cycle2)))
        if gain <= 0:
            break
        make_change(cycle1, cycle2, num, i1, i2)
    return cycle1, cycle2


def random_walk(distance_matrix, c1, c2, propose_method, time_allowed=1):
    cycle1 = deepcopy(c1)
    cycle2 = deepcopy(c2)
    best_cycle1, best_cycle2 = [], []
    best_gain = 0
    current_gain = 0
    start = time.time()
    while True:
        gain, i1, i2, num = next(propose_method(distance_matrix, cycle1, cycle2))
        make_change(cycle1, cycle2, num, i1, i2)
        current_gain += gain
        if best_gain < current_gain:
            best_gain = current_gain
            best_cycle1 = deepcopy(cycle1)
            best_cycle2 = deepcopy(cycle2)
        checkpoint = time.time()
        if checkpoint - start > time_allowed:
            break
    return best_cycle1, best_cycle2
