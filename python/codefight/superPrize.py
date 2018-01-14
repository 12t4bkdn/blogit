class Prizes(object):
    def __init__(self, purchases, n, d):
        self.purchases = purchases
        self.i = n
        self.step = n
        self.d = d
    def __iter__(self):
        return self
    
    def next(self):
        while self.i <= len(self.purchases) and self.purchases[self.i-1] % self.d != 0:
            self.i += self.step
        if self.i > len(self.purchases):
            raise StopIteration
        a = self.i
        self.i += self.step
        return a
            
        


def superPrize(purchases, n, d):
    return list(Prizes(purchases, n, d))
