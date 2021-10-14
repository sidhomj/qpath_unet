
# function to flatten nested list/tuple/numpy whatever it is 
flatten = lambda *n: (e for a in n
    for e in (flatten(*a) if isinstance(a, (tuple, list)) else (a,)))