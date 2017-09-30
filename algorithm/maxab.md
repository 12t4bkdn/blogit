<pre>
<code>int getMax(int a, int b) {
   int c = a - b;
   int k = (c &lt;&lt; 31) &amp; 0x1;
   int max = a - k * c;
   return max;
}</code></pre>

<p>&nbsp;</p>
