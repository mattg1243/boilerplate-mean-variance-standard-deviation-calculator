import numpy as np

def calculate(list):

    # create np array from arg list
    arrOG = np.array(list)
    if arrOG.size != 9:
        raise ValueError
    arr = np.reshape(arrOG, (3, 3))
    print(arr)
    # each value in the dictionary should be formatted like:
    # [ axis1, axis2, flattened ]
    calculations = {
        'mean': [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arrOG)], 
        'variance': [], 
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }

    return calculations