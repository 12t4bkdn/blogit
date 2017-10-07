<h2>Basic File Handling in PHP</h2>

<p>PHP has different different method or functions for creating, reading, uploading, writing, closing, deleting files.</p>

<h3>What is file handling in PHP</h3>

<p>Before going to understand about file handling, you should first know what is file ?File is nothing but a sequence of bytes stored in a group.File are used to store your information and if you can make changes in your file whenever you want like:</p>

<ol>
	<li><strong>Opening &amp; Closing File</strong></li>
	<li><strong>Creating File</strong></li>
	<li><strong>Reading File</strong></li>
	<li><strong>Writing File</strong></li>
	<li><strong>Editing File</strong></li>
</ol>

<h3>Opening &amp; Closing a File</h3>

<p>Before doing any activity with files you need to open the file, also when you are going to open file then you can set mode, in which you want to open. Mode will be like read, write etc.</p>

<table border="1" cellpadding="0" cellspacing="0" style="width:100%">
	<tbody>
		<tr>
			<th>Modes</th>
			<th>Description</th>
		</tr>
		<tr>
			<td>r</td>
			<td>Read only. Pointers at the beginning of the file</td>
		</tr>
		<tr>
			<td>r+</td>
			<td>Read and Write both.&nbsp;Pointers&nbsp;at the beginning of the file</td>
		</tr>
		<tr>
			<td>w</td>
			<td>Write only. Opens and clears the contents of file; or creates a new file if it doesn&rsquo;t exist</td>
		</tr>
		<tr>
			<td>w+</td>
			<td>Read and Write both. Opens and clears the contents of file or creates a new file if it doesn&rsquo;t exist</td>
		</tr>
		<tr>
			<td>a</td>
			<td>Append. Opens and writes to the end of the file or creates a new file if it doesn&rsquo;t exist</td>
		</tr>
		<tr>
			<td>a+</td>
			<td>Read and Append both. Preserves file content by writing to the end of the file</td>
		</tr>
		<tr>
			<td>x</td>
			<td>Write only. Creates a new file. Returns FALSE and an error if file already exists</td>
		</tr>
		<tr>
			<td>x+</td>
			<td>Read and Write both. Creates a new file. Returns FALSE and an error if file already exists</td>
		</tr>
	</tbody>
</table>

<p>Open a File :</p>

<p>You can use fopen() function to open a file in PHP. fopen() function takes two arguments, first contains the name of the file and second contains the mode of file.</p>

<p>Have a look at given example :</p>

<ol>
	<li>$my_file = &#39;myfile.txt&#39;;</li>
	<li>$handle = fopen($my_file, &#39;w&#39;) or die(&#39;Cannot open file: &#39;.$my_file);</li>
</ol>

<p>Read a File :</p>

<p>You can use fread() function to read a file in PHP.</p>

<p>Have a look at given example :</p>

<ol>
	<li>$my_file = &#39;myfile.txt&#39;;</li>
	<li>$handle = fopen($my_file, &#39;r&#39;);</li>
	<li>$data = fread($handle,filesize($my_file));</li>
</ol>

<p>Write to a File :</p>

<p>You can use fwrite() function to write to a file in PHP.</p>

<p>Have a look at given example :</p>

<ol>
	<li>$my_file = &#39;myfile.txt&#39;;</li>
	<li>$handle = fopen($my_file, &#39;w&#39;) or die(&#39;Cannot open file: &#39;.$my_file);</li>
	<li>$data = &#39;This is the data which you have to write in your file&#39;;</li>
	<li>fwrite($handle, $data);</li>
</ol>

<p>Close a File :</p>

<p>You can use fclose() function to close a file in PHP.</p>

<p>Have a look at given example :</p>

<ol>
	<li>$my_file = &#39;myfile.txt&#39;;</li>
	<li>$handle = fopen($my_file, &#39;w&#39;) or die(&#39;Cannot open file: &#39;.$my_file);</li>
	<li>//write some data here</li>
	<li>fclose($handle);</li>
</ol>

<p>Delete a File :</p>

<p>You can use unlink() function to delete a file in PHP.</p>

<p>Have a look at given example :</p>

<ol>
	<li>$my_file = &#39;myfile.txt&#39;;</li>
	<li>unlink($my_file);</li>
</ol>

<p>Reading a File Line by Line :</p>

<p>The fgets() function is used to read a single line from a file and then file pointer is pointing to the next line in the file. so by this way we can read file line by line.</p>

<p>Have a look at given example :</p>

<ol>
	<li>$file = fopen(&quot;myfile.txt&quot;, &quot;r&quot;) or exit(&quot;Unable to open the file!&quot;);</li>
	<li>while(!feof($file))</li>
	<li>{</li>
	<li>echo fgets($file). &quot;&lt;br&gt;&quot;;</li>
	<li>}</li>
	<li>fclose($file);</li>
</ol>
