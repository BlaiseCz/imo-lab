from copy import deepcopy
from lab2.local_search import make_change
import numpy as np


def lm_algorithm(distance_matrix,
                 path1, path2,
                 propose_method,
                 history):
    gain, i1, i2, num = propose_method(distance_matrix, path1, path2)
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
