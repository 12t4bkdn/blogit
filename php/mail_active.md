<p>Mailgun and Mandrill that are api based drivers are mostly faster and simpler rather than SMTP servers.</p>

<p>Guzzle HTTP library should be installed in your application if don&#39;t have installed then run this command after adding in&nbsp;<code>composer.json</code>&nbsp;file.</p>

<pre>
&quot;guzzlehttp/guzzle&quot;: &quot;~5.3|~6.0&quot;</pre>

<p>To use all api based driver you need to set the driver option in your&nbsp;<strong>config/mail.php</strong>&nbsp;and set credentials in&nbsp;<strong>config/services.php</strong></p>

<p><strong>Mailgun Driver</strong></p>

<ol>
	<li>&#39;mailgun&#39; =&gt; [</li>
	<li>&#39;domain&#39; =&gt; &#39;your-mailgun-domain&#39;,</li>
	<li>&#39;secret&#39; =&gt; &#39;your-mailgun-key&#39;,</li>
	<li>],</li>
</ol>

<p><strong>Mandrill Driver</strong></p>

<ol>
	<li>&#39;mandrill&#39; =&gt; [</li>
	<li>&#39;secret&#39; =&gt; &#39;your-mandrill-key&#39;,</li>
	<li>],</li>
</ol>

<p><strong>Laravel Mail Send Example</strong></p>

<p>Use&nbsp;<code>Mail</code>&nbsp;facade to send mail via&nbsp;<code>send</code>&nbsp;method. The&nbsp;<code>send</code>&nbsp;method contain three parameters. First parameter is your view blade file where you write your messages, second parameter is for passing array data to view and last one is closure callback that receives a message instance through which you can customize the subjects, recipients and other features of mail messages.</p>

<ol>
	<li>Mail::send(&#39;email.welcome&#39;, [&#39;name&#39; =&gt; $name], function ($message) use($data)</li>
	<li>{</li>
	<li>$message-&gt;to($data[&#39;email&#39;], $data[&#39;name&#39;])-&gt;subject(&#39;Welcome to Expertphp.in!&#39;);</li>
	<li>&nbsp;</li>
	<li>});</li>
</ol>

<p>Now you can see we are passing $data in view&nbsp;<code>welcome.blade.php</code>&nbsp;in&nbsp;<code>email</code>&nbsp;directory</p>

<p>Access&nbsp;<code>$data</code>&nbsp;in view :</p>

<ol>
	<li>echo $data[&#39;name&#39;]; ?&gt;</li>
</ol>

<p><strong>Add Attachments</strong></p>

<ol>
	<li>Mail::send(&#39;users.file&#39;, $data, function ($message) {</li>
	<li>$message-&gt;attach($pathToFile);</li>
	<li>});</li>
</ol>

<p>You can easily sent mail in laravel with files, you have to put your file path only in attachment method.</p>

<h3>Send emails with activation link after successful Register</h3>

<ol>
	<li>&nbsp;&nbsp;&nbsp;&nbsp;$this-&gt;validate($request, [</li>
	<li>&#39;name&#39; =&gt; &#39;required&#39;,</li>
	<li>&#39;email&#39; =&gt; &#39;required|email&#39;,</li>
	<li>&#39;password&#39;=&gt;&#39;required&#39;</li>
	<li>]);</li>
	<li>&nbsp;&nbsp;&nbsp;&nbsp;$user = new User;</li>
	<li>&nbsp;&nbsp;&nbsp;&nbsp;$user-&gt;name=$request-&gt;get(&#39;name&#39;);</li>
	<li>&nbsp;&nbsp;&nbsp;&nbsp;$user-&gt;email=$request-&gt;get(&#39;email&#39;);</li>
	<li>&nbsp;&nbsp;&nbsp;&nbsp;$user-&gt;password=$request-&gt;get(&#39;password&#39;);</li>
	<li>&nbsp;&nbsp;&nbsp;$user-&gt;verification_token = md5(uniqid(&#39;KP&#39;));</li>
	<li>&nbsp;&nbsp;&nbsp;$user-&gt;save();</li>
	<li>$activation_link = route(&#39;user.activate&#39;, [&#39;email&#39; =&gt; $user-&gt;email, &#39;verification_token&#39; =&gt; urlencode($user-&gt;verification_token)]);</li>
	<li>Mail::send(&#39;users.email.welcome&#39;, [&#39;name&#39; =&gt; $user-&gt;name, &#39;activation_link&#39; =&gt; $activation_link], function ($message) use($user,$activation_link)</li>
	<li>{</li>
	<li>$message-&gt;to($user-&gt;email, $user-&gt;name)-&gt;subject(&#39;Welcome to Expertphp.in!&#39;);</li>
	<li>});</li>
</ol>
