import numpy as np

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



