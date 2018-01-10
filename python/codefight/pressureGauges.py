def pressureGauges(morning, evening):
    return map(lambda t: list(t), zip(*map(lambda x: (x[0], x[1]) if x[0] < x[1] else  (x[1], x[0]), zip(morning, evening))))
