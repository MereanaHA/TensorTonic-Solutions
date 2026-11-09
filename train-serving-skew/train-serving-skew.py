import numpy as np
import math

def detect_skew(train_dist: dict, serving_dist: dict, threshold: float = 0.2, eps: float = 1e-10) -> dict:
    """
    Returns a dictionary of feature PSI scores and skew flags.
    """
    # Write code here
    dic_psi = {}
    for key,value in train_dist.items() :
        sum=0
        diff = [a-b for a,b in zip(serving_dist[key],value)]
        ratio = [(a+eps)/(b+eps) for a,b in zip(serving_dist[key],value)]
        for i in range (len(value)):
            sum+=diff[i]*math.log(ratio[i])
        dic_psi[key]={"psi":sum,"skewed":sum>=threshold}
    return dic_psi
    pass