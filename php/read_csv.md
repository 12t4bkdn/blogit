<pre>
<code class="language-php"> $fileD = fopen('expertphp-product.csv',"r");
 $column=fgetcsv($fileD);
 while(!feof($fileD)){
     $rowData[]=fgetcsv($fileD);
 }
 foreach ($rowData as $key =&gt; $value) {
            
     $inserted_data=array('name'=&gt;$value[0],
         'details'=&gt;$value[1],
     );
            
     Product::create($inserted_data);
 }
 print_r($rowData);</code></pre>

<p>&nbsp;</p>
