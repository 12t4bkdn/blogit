def primesSum(a, b):
    return reduce(lambda x, y: x+y, filter(lambda x: x >= 2 and not bool(filter(lambda i: x%i==0, range(2,int(x**0.5) + 1))), range(a, b+1)), 0)
