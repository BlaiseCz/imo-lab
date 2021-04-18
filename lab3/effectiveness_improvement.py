from copy import deepcopy

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


def candidate_moves():
    pass


def set_ids_order(i1, i2):
    if i1 < i2:
        first_node = i1
        second_node = i2
    else:
        first_node = i2
        second_node = i1
    return first_node, second_node


def swap_edges(cycle, distance_matrix, i1, i2):
    first_node, second_node = set_ids_order(i1, i2)
    first_node = first_node.astype(int)
    second_node = second_node.astype(int)
    updated_path = deepcopy(cycle)
    updated_path[first_node:second_node] = updated_path[first_node:second_node][::-1]

    gain = 0
    if (second_node - 1) % len(cycle) != first_node:
        gain += distance_matrix[cycle[first_node]][cycle[(first_node - 1) % len(cycle)]] + \
                distance_matrix[cycle[second_node - 1]][cycle[(second_node) % len(cycle)]]

        gain -= distance_matrix[updated_path[first_node]][updated_path[(first_node - 1) % len(cycle)]] + \
                distance_matrix[updated_path[second_node - 1]][updated_path[(second_node) % len(cycle)]]

    return gain


def lm_algorithm_ver2(distance_matrix, path1, path2, propose_method):
    history = [(path1, path2)]
    # gain, i1, i2, num
    propositions = np.array(list(propose_method(distance_matrix, path1, path2)))
    lm_indexes = np.where(propositions[..., 0] > 0)
    LM_ = np.take(propositions, lm_indexes, axis=0)
    # LM = LM_[LM_[..., 0].argsort(kind='mergesort')][::-1]

    while propositions.size != 0:
        # only changes with positive gain
        propositions = propositions[propositions[..., 0] > 0]
        # sorted from best to worst
        propositions = np.sort(propositions, axis=0)
        propositions = np.flip(propositions, axis=0)
        gain, i1, i2, num = propositions[0]

        i1 = i1.astype(int)
        i2 = i2.astype(int)
        # two different cycles
        if num == 2:
            path1[i1], path2[i2] = path2[i2], path1[i1]
            affected_nodes = {path1[i1 - 1], path1[i1], path1[i1 + 1], path2[i2 - 1], path2[i2], path2[i2 + 1]}
        # both from cycle1
        elif num == 0:
            swap_edges(path1, distance_matrix, i1, i2)
            affected_nodes = set([path1[i1 - 1], path1[i1], path1[i1 + 1],
                                  path1[i2 - 1], path1[i2], path1[i2 + 1]])
        elif num == 1:
            swap_edges(path2, distance_matrix, i1, i2)
            affected_nodes = set([path2[i1 - 1], path2[i1], path2[i1 + 1],
                                  path2[i2 - 1], path2[i2], path2[i2 + 1]])
        else:
            print(num)

        history.append((path1, path2))
        propositions = propositions[propositions[..., 1] not in affected_nodes]
        propositions = propositions[propositions[..., 2] not in affected_nodes]
        new_propositions = np.array(list(propose_method(distance_matrix, path1,
                                                        path2, fresh=affected_nodes)))
        propositions = np.concatenate([propositions, new_propositions], axis=0)
    return history
