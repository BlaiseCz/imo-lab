from copy import deepcopy
from propose import change_edges, edges, change_edges_
from random import randint

def perturbateSmall_(cycle1, cycle2, num_of_perturbations=5):
    """
    (In-place) zamienia wierzchołki/krawędzie wewnątrz podanych cykli.
    """
    for _ in range(num_of_perturbations):
        move_type = randint(0, 2)
        i1 = randint(0, len(cycle1)-1)
        i2 = i1
        while move_type != 2 and i2 == i1:
            i2 = randint(0, len(cycle1)-1)
        change_edges_(move_type, i1, i2, cycle1, cycle2)


def perturbateSmall(cyclea, cycleb, num_of_perturbations=5):
    """
    (Zwraca kopię) zamienia wierzchołki/krawędzie wewnątrz podanych cykli.
    """
    cycle1 = deepcopy(cyclea)
    cycle2 = deepcopy(cycleb)
    for _ in range(num_of_perturbations):
        move_type = randint(0, 2)
        i1 = randint(0, len(cycle1)-1)
        i2 = i1
        while move_type != 2 and i2 == i1:
            i2 = randint(0, len(cycle1)-1)
        change_edges_(move_type, i1, i2, cycle1, cycle2)
    return cycle1, cycle2


def perturbateBig_(cycle1: list, cycle2: list, num_of_deletes=20):
    """
    (In-place) Usuwa losowe wierzchołki z podanych cykli.
    """
    for _ in range(num_of_deletes):
        i = randint(0,len(cycle1)-1)
        cycle1.pop(i)
        i = randint(0,len(cycle2)-1)
        cycle2.pop(i)


def perturbateBig(cyclea: list, cycleb: list, num_of_deletes=20):
    """
    (In-place) Usuwa losowe wierzchołki z podanych cykli.
    """
    cycle1 = deepcopy(cyclea)
    cycle2 = deepcopy(cycleb)
    for _ in range(num_of_deletes):
        i = randint(0,len(cycle1)-1)
        cycle1.pop(i)
        i = randint(0,len(cycle2)-1)
        cycle2.pop(i)
    return cycle1, cycle2

if __name__ == '__main__':
    a = list(range(1, 50))
    b = list(range(50, 100))
    print(perturbateSmall(a, b))
    print(perturbateBig(a, b))
