from copy import deepcopy
from lab2.local_search import make_change

def steepest(distance_matrix, c1, c2, propose_method, history):
    pass
#   mamy cykl i robimy tylko zamianę wierzchołków
#   jako sąsiedztwo bierzemy wierzchołki
#   generujemy liste możliwych ruchow
#   wyrzucamy ruchy, które nie przynoszą poprawy
#   sortowanie listy od najlepszego do najgorszego
#   while LM not empty:
#       aplikujemy nasz najlepszy ruch
#       wyrzucamy wykoanny ruch z listy
#       do listy dodajemy wszystkie ruchy które brały udział w zamianie
# local search