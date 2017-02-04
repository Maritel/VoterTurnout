# Utility functions specific to NN

import numpy as np


# The labels are '1' and '2'
# This changes all '2' labels to '-1'
def standardize_labels(array):
    for y in np.nditer(array, op_flags=['readwrite']):
        if y == 2:
            y[...] = -1


# Performs the reverse of standardize_labels
def unstandardize_labels(array):
    for y in np.nditer(array, op_flags=['readwrite']):
        if y == -1:
            y[...] = 2

