<pre>
<code>def wordPower(word):
    num = { x: ord(x)-96 for x in word}
    return sum([num[ch] for ch in word])</code></pre>

<pre>
<code>In [1]: a = b = c = range(20)

In [2]: zip(a, b, c)
Out[2]: 
[(0, 0, 0),
 (1, 1, 1),
 ...
 (17, 17, 17),
 (18, 18, 18),
 (19, 19, 19)]</code></pre>

<pre>
<code>def fixResult(result):
    def fix(x):
        return x / 10

    return map(fix, result)</code></pre>

<pre>
<code>def collegeCourses(x, courses):
    def shouldConsider(course):
        return len(course) != x

    return filter(shouldConsider, courses)</code></pre>

<pre>
<code>def createHistogram(ch, data):
    return map(lambda x: ch*x,data)</code></pre>

<pre>
<code>def gcd(m,n):
    return gcd(abs(m-n), min(m, n)) if (m-n) else n</code></pre>

<pre>
<code>from fractions import gcd

def leastCommonDenominator(denominators):
    return reduce(lambda x, y: x*y/gcd(x, y), denominators)</code></pre>

<pre>
<code>def uniqueCharacters(document):
    return sorted(list(set([x for x in document])))</code></pre>

<p>&nbsp;</p>

<pre>
<code>from itertools import *

def cyclicName(name, n):
    gen = iter(name)
    res = [next(gen) for _ in range(n)]
    return ''.join(res)</code></pre>

<p>&nbsp;</p>
