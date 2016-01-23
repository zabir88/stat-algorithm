import numpy as np
#To write each data file as a 128 by 199 matrix
def individual_datfile(x): 
    try:
        t,y= np.loadtxt(x, skiprows=1, unpack= True,dtype=np.float64)
    except:
        return False
    y= np.row_stack(y[:,])
    yfin= y.reshape(199,128).T
    return yfin

#To average the plus and minus m
def array_avg(a,b): 
    mean= np.mean(([a,b]), axis =0,dtype= np.float64)
    return mean

#To calculate arithmetic mean
def arithmetic_mean(a,b,c): 
    sum= np.sum((a,b), axis=0, dtype=np.float64)
    arith_mean= np.divide(sum,(2*c), dtype= np.float64)
    return arith_mean

#To calculate geometric mean
def geometric_mean(a,b,c): 
    product= np.multiply(a,b,dtype= np.float64)
    root= np.sqrt(product,dtype=np.float64)
    geo_mean= np.divide(root, c, dtype=np.float64)
    return geo_mean

#To calculate log of arithmetic and geometric mean (Effective Mass)
def log_values(a):
    log= np.empty(shape=(127,199), dtype=np.float64)
    for i in range(127):
        ratio_log[i]= (-1)*np.log(np.divide(a[i+1],a[i]), dtype=np.float64)
    return ratio_log

#To calculate the mean of arithmetic and geometric mean, then take ratio and then take the log (Average Effective Mass)
def mean_log_values(a): 
    up = np.empty(shape= (127,199), dtype= np.float64)
    down= np.empty(shape= (127,199), dtype= np.float64)
    for i in range(127):
        up[i] =a[i+1]
        down[i]= a[i]    
    meanup= np.mean(up, axis=1, dtype=np.float64)
    meandown= np.mean(down, axis=1, dtype=np.float64)
    log_mean= (-1)*np.log(np.divide(np.row_stack(meanup), np.row_stack(meandown), dtype=np.float64))
    return log_mean

#To calculate standard deviation 
def standard_dev(a,b): 
    std= np.sqrt(np.sum(np.square(np.subtract(a,b)), axis=1))
    std= std/np.sqrt([199*198])
    return np.row_stack(std)

#To bootstrap arithmetic and geometric mean 
def bootstrap(data, numsampling, blocked=False): 
    if blocked:
        x= np.asarray([[[np.random.choice(row)for elements in row]for row in data]for numresample in range(numsampling)])
    else:
        flat = np.asarray([x for row in data for x in row])
        x= np.asarray([[[np.random.choice(flat) for elements in row] for row in data]for numresample in range(numsampling)])
    avg= np.array([np.column_stack(np.mean(row, axis=1))for row in x]).T    
    return avg.reshape(128,numsampling)

#To calculate log of bootstrapped arithmetic and geometric mean 
def bootstrap_log_values(a):
    log= np.empty(shape=(127,796), dtype=np.float64)
    for i in range(127):
        log[i]= (-1)*np.log(np.divide(a[i+1],a[i]), dtype=np.float64)
    return log

#To calculate the mean of bootstrapped arithmetic and geometric mean, then take ratio and then take the log
def bootstrap_mean_log_values(a): 
    up= np.empty(shape= (127,796), dtype= np.float64)
    down= np.empty(shape= (127,796), dtype= np.float64)
    for i in range(127):
        up[i] =a[i+1]
        down[i]= a[i]    
    meanup= np.mean(up, axis=1, dtype=np.float64)
    meandown= np.mean(down, axis=1, dtype=np.float64)
    log_mean= (-1)*np.log(np.divide(np.row_stack(meanup), np.row_stack(meandown), dtype=np.float64))
    return log_mean

#To calculate standard deviation
def bootstrap_standard_dev(a,b): 
    std= np.sqrt(np.sum(np.square(np.subtract(a,b)), axis=1))
    std= std/np.sqrt([796*795])
    return np.row_stack(std)

#Block Method for Arithmetic and Geometric Mean
def block_method(x, blocksize):
    a=np.divide(len(x[0]),blocksize, dtype=np.float64)
    if type(blocksize)==int and type(a)==int:
        x1= np.mean(x.reshape(len(x), a, blocksize),axis=2)
        return x1
    else:
        return 'Both block size and ratio of column dimension to block size must be integers'

#Correlated Chisquare test:
def chisquaretest(Meff,AvgMeff):
    #Finding the covariance matrix
    covar= np.empty(shape=(len(Meff),len(AvgMeff),len(Meff[0])))
    for i in range(len(Meff)):
        for row in zip(Meff,AvgMeff):
            covar[i]=(Meff[i]-AvgMeff[i])*(Meff-AvgMeff)
    covar= np.sum(covar, axis=2)
    #Finding the correlation matrix
    corr= np.linalg.inv(covar)
    #Finding Chisquare 
    chisquare= np.empty(shape=(len(AvgMeff),len(AvgMeff)))
    for i in range(len(AvgMeff)) :
        for row in AvgMeff:
            chisquare[i]= np.column_stack(0.25*(AvgMeff[i]-AvgMeff)*(AvgMeff-AvgMeff[i]))
    return chisquare*corr
    

