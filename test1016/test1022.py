
"""
>>> multiply1(4, 3)
12
>>> multiply1(5, 3)
15
>>> multiply2(2, 3)
12
>>> multiply2(3,4)
36
"""
def multiply1(a, b):
    """
    >>> multiply1(4, 3)
    12
    >>> multiply1(5, 3)
    15
    >>> multiply2(2, 3)
    12
    >>> multiply2(3,4)
    36
    """
    return a * b
def multiply2(a, b):
    return a * a * b

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)