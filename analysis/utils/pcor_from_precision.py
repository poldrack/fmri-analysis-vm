"""
compute partial correlation
"""

import numpy

def pcor_from_precision(P,zero_diagonal=1):
    # given a precision matrix, compute the partial correlation matrix
    # based on wikipedia page: http://en.wikipedia.org/wiki/Partial_correlat
    #Using_matrix_inversion
    pcor=numpy.zeros(P.shape)
    for i in range(P.shape[0]):
        for j in range(P.shape[1]):
            pcor[i,j]=P[i,j]/numpy.sqrt(P[i,i]*P[j,j])
            if zero_diagonal==1 and i==j:
                pcor[i,j]=0
    return pcor


