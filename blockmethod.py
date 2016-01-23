import numpy as np

def block_method(x, blocksize):
    a=np.divide(len(x[0]),blocksize, dtype=np.float64)
    if type(a)==int and type(blocksize)==int:
        x1= np.sum(x.reshape(len(x), a, blocksize),axis=2)
        return x1
    else:
        return 'Both block size and ratio of column dimension to block size must be integers' 


