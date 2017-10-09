<h1>Multiple SSH Keys settings for different github account</h1>

<h2>create different public key</h2>

<p>create different ssh key according the article&nbsp;<a href="http://help.github.com/mac-set-up-git/">Mac Set-Up Git</a></p>

<pre>
<code>$ ssh-keygen -t rsa -C "your_email@youremail.com"
</code></pre>

<p>Please refer to&nbsp;<a href="http://help.github.com/ssh-issues/">github ssh issues</a>&nbsp;for common problems.</p>

<p>for example, 2 keys created at:</p>

<pre>
<code>~/.ssh/id_rsa_activehacker
~/.ssh/id_rsa_jexchan
</code></pre>

<p>then, add these two keys as following</p>

<pre>
<code>$ ssh-add ~/.ssh/id_rsa_activehacker
$ ssh-add ~/.ssh/id_rsa_jexchan
</code></pre>

<p>you can delete all cached keys before</p>

<pre>
<code>$ ssh-add -D
</code></pre>

<p>finally, you can check your saved keys</p>

<pre>
<code>$ ssh-add -l
</code></pre>

<h2>Modify the ssh config</h2>

<pre>
<code>$ cd ~/.ssh/
$ touch config
$ subl -a config
</code></pre>

<p>Then added</p>

<pre>
<code>#activehacker account
Host github.com-activehacker
	HostName github.com
	User git
	IdentityFile ~/.ssh/id_rsa_activehacker

#jexchan account
Host github.com-jexchan
	HostName github.com
	User git
	IdentityFile ~/.ssh/id_rsa_jexchan
</code></pre>

<h2>Clone you repo and modify your Git config</h2>

<p>clone your repo git clone&nbsp;<a href="mailto:git@github.com">git@github.com</a>:activehacker/gfs.git gfs_jexchan</p>

<p>cd gfs_jexchan and modify git config</p>

<pre>
<code>$ git config user.name "jexchan"
$ git config user.email "jexchan@gmail.com" 

$ git config user.name "activehacker"
$ git config user.email "jexlab@gmail.com" 
</code></pre>

<p>or you can have global git config $ git config --global user.name &quot;jexchan&quot; $ git config --global user.email &quot;<a href="mailto:jexchan@gmail.com">jexchan@gmail.com</a>&quot;</p>

<p>then use normal flow to push your code</p>

<pre>
<code>$ git add .
$ git commit -m "your comments"
$ git push</code></pre>
