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
    if move_type == 2: #zamiana krawędzi
        cycle1[i1], cycle2[i2] = cycle2[i2], cycle1[i1]


def change_edges(move_type: int, i1, i2, cycle1, cycle2):
    """
    (Zwraca rezultat operacji) Wykonaj ruch zaproponowany przez funkcję edges.
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

def compute_gain(distance_matrix: list, move_type: int, i1: int, i2: int, cycle1: list, cycle2: list):
    """
    Oblicza gaina jakiego uzyskamy ze zrobienia ruchu zaproponowanego przez
    edges.
    """

    gain = 0
    # Poprzedniki i następniki
    i1l = (i1-1)%len(cycle1)
    i1r = (i1+1)%len(cycle1)
    i2l = (i2-1)%len(cycle1)
    i2r = (i2+1)%len(cycle1)

    # Wymiana cykli
    if move_type == 2:
        # usunięcie połączenia z cyklu 1
        gain += distance_matrix[cycle1[i1l]][cycle1[i1]]
        gain += distance_matrix[cycle1[i1r]][cycle1[i1]]
        # dodanie połączenia w cyklu 1
        gain -= distance_matrix[cycle1[i1l]][cycle2[i2]]
        gain -= distance_matrix[cycle1[i1r]][cycle2[i2]]

        # usunięcie połączenia z cyklu 2
        gain += distance_matrix[cycle2[i2l]][cycle2[i2]]
        gain += distance_matrix[cycle2[i2r]][cycle2[i2]]
        # dodanie połączenia w cyklu 2
        gain -= distance_matrix[cycle2[i2l]][cycle1[i1]]
        gain -= distance_matrix[cycle2[i2r]][cycle1[i1]]

        return gain

    # Wymiana krawędzi
    if move_type == 0: cycle = cycle1
    else: cycle = cycle2

    return gain

