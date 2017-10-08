<pre>
<code class="language-php">function getDirContents($dir, &amp;$results = array()){
    $files = scandir($dir);
    foreach($files as $key =&gt; $value){
        $path = realpath($dir.DIRECTORY_SEPARATOR.$value);
        if(!is_dir($path)) {
            $results[] = ['path'=&gt;$path,'size'=&gt;filesize($path)];
        } else if($value != "." &amp;&amp; $value != "..") {
            getDirContents($path, $results);
            $results[] = ['path'=&gt;$path,'size'=&gt;filesize($path)];
        }
    }
    return $results;
}</code></pre>

<p>&nbsp;</p>
