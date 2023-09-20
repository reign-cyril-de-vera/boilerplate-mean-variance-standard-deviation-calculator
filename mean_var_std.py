import numpy as np

def calculate(lst):
    if len(lst) < 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.reshape(np.array(lst), (-1, 3))

    operations = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']
    np_operations = [np.mean, np.var, np.std, np.max, np.min, np.sum]

    calculations = {operation: [np_operation(arr, axis=0).tolist(), 
                           np_operation(arr, axis=1).tolist(), 
                           np_operation(arr).tolist()] 
               for operation, np_operation in zip(operations, np_operations)}

    return calculations