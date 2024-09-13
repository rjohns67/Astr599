
def Sumf(L, f=1):
    """ summation of a field in the asteroid data 
    
    parameters
    ---------
    L : list of tuples
        the list of asteroids and their sma, ecc and orbital class
    f : integer
        the field to be summed (in this case the semi-major axes)
        
    returns
    ------
    s : float
        the sum of the values in the field = f
    """
    s = 0.0
    for k in L:
        s += k[f]
    return s
