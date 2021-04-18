from copy import deepcopy
from lab2.local_search import make_change
import numpy as np


def lm_algorithm(distance_matrix,
                 path1, path2,
                 propose_method,
                 history):
    gain, i1, i2, num = next(propose_method(distance_matrix, path1, path2))
    stacked_values = np.vstack((gain, i1, i2))
    lm_indexes = np.where(stacked_values[0, ...] > 0)
    LM_ = np.take(stacked_values, lm_indexes, axis=1).reshape(3, len(lm_indexes[0])).T
    LM = LM_[LM_[:, 0].argsort(kind='mergesort')][::-1]

    change = False

    applied_i1 = -1
    applied_i2 = -1

    while LM.size != 0:

        if change:
            LM = apply_new_(applied_i1, applied_i2)
        for i, (gain, i1, i2) in enumerate(LM):
            if i1 in path1 and i2 in path2:
                path1, path2 = apply_move(i1, i2)
                applied_i1, applied_i2 = i1, i2
                change = True
            elif i2 in path1 and i1 in path2:
                path1, path2 = apply_move(i2, i1)
                applied_i1, applied_i2 = i2, i1
                change = True
            else:
                np.delete(LM, i, axis=1)
                change = False

    return history

def lm_algorithm_ver2(distance_matrix, path1, path2, propose_method):
    history = [(path1, path2)]
    # gain, i1, i2, num
    propositions = np.array(list(propose_method(distance_matrix, path1, path2)),
                            dtype=np.int64)
    while propositions.size != 0:
        # only changes with positive gain
        propositions = propositions[propositions[..., 0] > 0]
        # sorted from best to worst
        propositions = np.sort(propositions, axis=0)
        propositions = np.flip(propositions, axis=0)
        gain, i1, i2, num = propositions[-1]

        # two different cycles
        if num == 2:
            path1[i1], path2[i2] = path2[i2], path1[i1]
            affected_nodes = {path1[i1 - 1], path1[i1], path1[i1 + 1], path2[i2 - 1], path2[i2], path2[i2 + 1]}
        # both from cycle1
        elif num == 0:
            swap_edges(path1, i1, i2)
            affected_nodes = {path1[i1 - 1], path1[i1], path1[i1 + 1], path1[i2 - 1], path1[i2], path1[i2 + 1]}
        elif num == 1:
            swap_edges(path2, i1, i2)
            affected_nodes = {path2[i1 - 1], path2[i1], path2[i1 + 1], path2[i2 - 1], path2[i2], path2[i2 + 1]}
        else:
            print('Coś poszło nie tak bo num jest równe:', end='')
            print(num)
            affected_nodes = set([])
        np.delete(propositions, 0, axis=0)

        history.append((path1, path2))

        #TODO: Zrób pętlę która usuwa jak i1 albo i2 jest w affected_nodes
        # teraz nie działa bo jak usuwa to indeks i się nie zgadza
        for i in range(len(propositions)):
            if propositions[i][1] in affected_nodes or \
               propositions[i][2] in affected_nodes:
                propositions = np.delete(propositions, i, axis=0)

        new_propositions = np.array(list(propose_method(distance_matrix, path1,
                                                        path2,
                                                        fresh=affected_nodes)),
                                    dtype=np.int64)
        propositions = np.concatenate([propositions, new_propositions], axis=0)
    return history

def swap_edges(cycle, i1, i2):
    if i1 > i2:
        i1, i2 = i2, i1
    cycle[i1:i2+1] = np.flip(cycle[i1:i2+1])

