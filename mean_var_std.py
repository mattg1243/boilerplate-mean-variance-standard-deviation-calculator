import numpy as np

def calculate(list):

    # create np array from arg list and make sure its valid
    arrOG = np.array(list)
    if arrOG.size != 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.reshape(arrOG, (3, 3))
    # each value in the dictionary should be formatted like:
    # [ axis1, axis2, flattened ]
    calculations = {
        'mean': [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arrOG)], 
        'variance': [np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), np.var(arrOG)], 
        'standard deviation': [np.std(arr, axis=0).tolist(), np.std(arr, axis=1).tolist(), np.std(arrOG)],
        'max': [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), arrOG.max()],
        'min': [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), arrOG.min()],
        'sum': [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), arrOG.sum()]
    }

    return calculations