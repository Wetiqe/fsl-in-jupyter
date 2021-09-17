from scipy import stats
import numpy  as np
import pandas as pd
import math


# Definate partial correlation function
def partial_corr(x, y, partial = []):
    """
    partial correlation test
    input:
        x,y: series, contains the data
        partial: list, contains the covarate
    returns:
        r: partial correlation coefficient
        prob: p value
    """
    xy, xyp = stats.pearsonr(x, y)
    xp, xpp = stats.pearsonr(x, partial)
    yp, ypp = stats.pearsonr(y, partial)
    n = len(x)
    df = n - 3
    r = (xy - xp*yp)/(np.sqrt(1 - xp*xp)*np.sqrt(1 - yp*yp))
    if abs(r) == 1.0:
        prob = 0.0
    else:
        t = (r*np.sqrt(df))/np.sqrt(1 - r*r)
        prob = (1 - stats.t.cdf(abs(t),df))**2
        
    return r,prob

# chi squre test
def chi2(g1,g2,factor):
    """
    chi squre test and fisher exact test for 2 X 2 matrix
    input:
        g1,g2: raw dataframe
        factor: str, the the column which needs compare
    returns:
        a tuple contains the matrix, stats, p value in order
    """
    def get_min(ls):
        num = ls[0]
        for item in ls[1:]:
            if item < num :
                num = item 
        return num    
    g1_a = g1[factor].sum()
    g2_a = g2[factor].sum()
    g1_b = g1.shape[0] - g1_a
    g2_b = g2.shape[0] - g2_a
    matrix = [[g2_a, g1_a],
             [g2_b, g1_b]]
    total = g1_a + g1_b + g2_a +g2_b
    MIN = get_min([g1_a, g1_b, g2_a, g2_b])
    print(matrix, total, MIN)
    if total < 40 or MIN < 5:
        # Fisher Exact
        oddsratio, p = stats.fisher_exact(matrix)
        return matrix, oddsratio, p 
    else:
        # chi2 
        chi2, chi2_p = stats.chi2_contingency(matrix)[0:2]
        return matrix, chi2, chi2_p

