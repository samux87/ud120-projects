#!/usr/bin/python
# Modified by Samuele Buosi
import numpy as np

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    # Start from 90 emelement and release 81 (-10%)
    '''import operator

    errors = [a-b for a, b in zip(predictions, net_worths)]
    data = list(zip(ages, net_worths, errors))
    sorted(data, key=operator.itemgetter(2))
    cleaned_data = data[:int(len(predictions)*0.9)]
'''

    ### your code goes here
    num_samples = len(ages)
    errors = np.empty((num_samples))
    for ind in range(num_samples):
        errors[ind] = abs(predictions[ind] - net_worths[ind])

    # sort and get a pivot value
    sorted_errors = errors.copy()
    sorted_errors.sort()
    pivot_ind = int(0.9 * num_samples)
    pivot_value = sorted_errors[pivot_ind]
    
    keep = errors < pivot_value
    for ind in range(num_samples):
        if keep[ind]:
            cleaned_data.append((ages[ind], net_worths[ind], errors[ind]))

    return cleaned_data
