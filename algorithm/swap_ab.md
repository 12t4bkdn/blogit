
<pre>
<code class="language-java">public static void swap(int a, int b) {
    //b = 9, a = 5
    a = b - a; // 9 - 5 = 4
    b = b - a; // 9 - 4 = 5
    a = a + b; // 4 + 5 = 9
    //b = 5, a = 9
}

</code></pre>

<p><code>//Một c&aacute;ch kh&aacute;c optimize v&agrave; nhanh hơn, sử dụng to&aacute;n tử XOR</code></p>

<pre>
<code class="language-java">public static void swap_opt(int a, int b) {
   a = a^b;
   b = a^b;
   a = a^b;
}</code></pre>

<p>&nbsp;</p>
