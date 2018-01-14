def tryFunctions(x, functions):
    return map(lambda func: eval(func)(x), functions)
