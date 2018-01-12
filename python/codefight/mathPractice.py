def mathPractice(numbers):
    return reduce(lambda x, (i,y): x+y if i%2 else x*y, enumerate(numbers), 1)
