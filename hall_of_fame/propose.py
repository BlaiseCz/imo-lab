from itertools import combinations, product
from copy import deepcopy

def edges(cycle1: list, cycle2: list):
    """
    Zaproponuj ruch zamiany krawędzi (lub wierzchołków jeśli między cyklami).
    Zakłada że cykle są tej samej długości.

    Używa yielda:

    proposer = edges(cycle1, cycle2)

    # jedna propozycja ruchu
    move = next(proposer)

    # wszystkie możliwe ruchy
    move = list(proposer)
    """
    proposer = product([0,1,2], combinations(range(len(cycle1)), 2))
    for move_type, (i1, i2) in proposer:
        yield move_type, i1, i2

def change_edges_(move_type: int, i1, i2, cycle1, cycle2):
    """
    (In-place) Wykonaj ruch zaproponowany przez funkcję edges.
    """
    if move_type == 0:
        cycle1[i1:i2+1] = reversed(cycle1[i1:i2+1])
    elif move_type == 1:
        cycle2[i1:i2+1] = reversed(cycle2[i1:i2+1])
    if move_type == 2:
        cycle1[i1], cycle2[i2] = cycle2[i2], cycle1[i1]

def change_edges(move_type: int, i1, i2, cycle1, cycle2):
    """
    (Zwraca kopię) Wykonaj ruch zaproponowany przez funkcję edges.
    """
    cyclea = deepcopy(cycle1)
    cycleb = deepcopy(cycle2)

    if move_type == 0:
        cyclea[i1:i2+1] = reversed(cyclea[i1:i2+1])
    elif move_type == 1:
        cycleb[i1:i2+1] = reversed(cycleb[i1:i2+1])
    if move_type == 2:
        cyclea[i1], cycleb[i2] = cycleb[i2], cyclea[i1]
    return cyclea, cycleb
