def calkinWilfSequence(number):
    def fractions():
        last =[1,1]
        while True:
            yield last
            a = 2 * (last[0] // last[1]) + 1
            denominator = a * last[1]-last[0]
            numerator = last[1]
            last = [numerator, denominator]

    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res
