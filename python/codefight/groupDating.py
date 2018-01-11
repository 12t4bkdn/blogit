def groupDating(male, female):
    return zip(*[(i,j) for i, j in zip(male,female) if i != j]) or [[], []]
