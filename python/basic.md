<p>1. A simple array sort method:</p>

<pre>
<code class="language-python">def simpleSort(arr):

    n = len(arr)

    for i in range(n):
        j = 0
        stop = n - i
        while j &lt; stop - 1:
            if arr[j] &gt; arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
    return arr
</code></pre>

<p>2. Given a number&nbsp;<code>n</code>&nbsp;and a base&nbsp;<code>x</code>, converts the number from base&nbsp;<code>x</code>&nbsp;to base&nbsp;<code>16</code></p>

<pre>
<code class="language-python">def baseConversion(n, x):
    return hex(int(str(n),x))[2:]</code></pre>

<p>3. A&nbsp;list&nbsp;<em>beautiful</em>&nbsp;if its first element is equal to its last element, or if a list is empty. Given a list&nbsp;<code>a</code>, your task is to chop off its first and its last element until it becomes&nbsp;<em>beautiful</em>.&nbsp;</p>

<pre>
<code class="language-python">def listBeautifier(a):
    res = a[:]
    while res and res[0] != res[-1]:
        a, *res, c = res
    return res</code></pre>

<p>4. Here&#39;s how&nbsp;<em>permutation cipher</em>&nbsp;works: the&nbsp;<code>key</code>&nbsp;to it consists of all the letters of the alphabet written up in some order. All occurrences of letter&nbsp;<code>&#39;a&#39;</code>&nbsp;in the encrypted text are substituted with the first letter of the&nbsp;<code>key</code>, all occurrences of letter&nbsp;<code>&#39;b&#39;</code>&nbsp;are replaced with the second letter from the&nbsp;<code>key</code>, and so on, up to letter&nbsp;<code>&#39;z&#39;</code>&nbsp;replaced with the last symbol of the&nbsp;<code>key</code>.</p>

<p>Given the&nbsp;<code>password</code>&nbsp;you always use, your task is to encrypt it using the&nbsp;<em>permutation cipher</em>&nbsp;with the given&nbsp;<code>key</code>.</p>

<pre>
<code class="language-python">def permutationCipher(password, key):
    table = string.maketrans('abcdefghijklmnopqrstuvwxyz', key)
    return str(password).translate(table)</code></pre>

<p>5.&nbsp;The track of time will be kept by a float number. It will be displayed on the board with the set precision&nbsp;<code>precision</code>&nbsp;with center alignment, and it is guaranteed that it will fit in the screen. Your task is to test the billboard. Given the time&nbsp;<code>t</code>, the&nbsp;<code>width</code>&nbsp;of the screen and the&nbsp;<code>precision</code>&nbsp;with which the time should be displayed, return a string that should be shown on the billboard.</p>

<p><strong>Example</strong></p>

<p>For&nbsp;<code>t = 3.1415</code>,&nbsp;<code>width = 10</code>&nbsp;and&nbsp;<code>precision = 2</code>,<br />
the output should be<br />
<code>competitiveEating(t, width, precision) = &quot;&nbsp;&nbsp;&nbsp;3.14&nbsp;&nbsp;&nbsp;&quot;</code>.</p>

<pre>
<code class="language-python">def competitiveEating(t, width, precision):
    return '{0:.{1}f}'.format(t, precision).center(width, ' ')</code></pre>

<p>&nbsp;</p>
