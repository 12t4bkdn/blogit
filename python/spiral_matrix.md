<p>A&nbsp;<em>spiral matrix</em>&nbsp;is a square matrix of size&nbsp;<code>n &times; n</code>. It contains all the integers in range from&nbsp;<code>1</code>&nbsp;to&nbsp;<code>n * n</code>&nbsp;so that number&nbsp;<code>1</code>&nbsp;is written in the bottom right corner, and all other numbers are written in increasing order spirally in the counterclockwise direction.</p>

<p>Given the size of the matrix&nbsp;<code>n</code>, your task is to create a&nbsp;<em>spiral matrix</em>.</p>

<p><strong>Example</strong></p>

<p>For&nbsp;<code>n = 3</code>, the output should be</p>

<pre>
<code>createSpiralMatrix(n) = [[5, 4, 3],
                         [6, 9, 2],
                         [7, 8, 1]]</code></pre>

<pre>
<code class="language-python">def createSpiralMatrix(n):
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    curDir = 0
    curPos = (n - 1, n - 1)
    res = [[0 for x in range(n)] for y in range(n)]

    for i in range(1, n * n + 1):
        res[curPos[0]][curPos[1]] = i
        nextPos = curPos[0] + dirs[curDir][0], curPos[1] + dirs[curDir][1]
        if not (0 &lt;= nextPos[0] &lt; n and
                0 &lt;= nextPos[1] &lt; n and
                res[nextPos[0]][nextPos[1]] == 0):
            curDir = (curDir + 1) % 4
            nextPos = curPos[0] + dirs[curDir][0], curPos[1] + dirs[curDir][1]
        curPos = nextPos

    return res
</code></pre>

<p>&nbsp;</p>
