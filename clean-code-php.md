 <article class="markdown-body entry-content" itemprop="text"><h1><a href="#clean-code-php" aria-hidden="true" class="anchor" id="user-content-clean-code-php"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Clean Code PHP</h1>
<h2><a href="#table-of-contents" aria-hidden="true" class="anchor" id="user-content-table-of-contents"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Table of Contents</h2>
<ol>
<li><a href="#introduction">Introduction</a></li>
<li><a href="#variables">Variables</a>
<ul>
<li><a href="#use-meaningful-and-pronounceable-variable-names">Use meaningful and pronounceable variable names</a></li>
<li><a href="#use-the-same-vocabulary-for-the-same-type-of-variable">Use the same vocabulary for the same type of variable</a></li>
<li><a href="#use-searchable-names-part-1">Use searchable names (part 1)</a></li>
<li><a href="#use-searchable-names-part-2">Use searchable names (part 2)</a></li>
<li><a href="#use-explanatory-variables">Use explanatory variables</a></li>
<li><a href="#avoid-nesting-too-deeply-and-return-early-part-1">Avoid nesting too deeply and return early (part 1)</a></li>
<li><a href="#avoid-nesting-too-deeply-and-return-early-part-2">Avoid nesting too deeply and return early (part 2)</a></li>
<li><a href="#avoid-mental-mapping">Avoid Mental Mapping</a></li>
<li><a href="#dont-add-unneeded-context">Don't add unneeded context</a></li>
<li><a href="#use-default-arguments-instead-of-short-circuiting-or-conditionals">Use default arguments instead of short circuiting or conditionals</a></li>
</ul>
</li>
<li><a href="#functions">Functions</a>
<ul>
<li><a href="#function-arguments-2-or-fewer-ideally">Function arguments (2 or fewer ideally)</a></li>
<li><a href="#functions-should-do-one-thing">Functions should do one thing</a></li>
<li><a href="#function-names-should-say-what-they-do">Function names should say what they do</a></li>
<li><a href="#functions-should-only-be-one-level-of-abstraction">Functions should only be one level of abstraction</a></li>
<li><a href="#dont-use-flags-as-function-parameters">Don't use flags as function parameters</a></li>
<li><a href="#avoid-side-effects">Avoid Side Effects</a></li>
<li><a href="#dont-write-to-global-functions">Don't write to global functions</a></li>
<li><a href="#dont-use-a-singleton-pattern">Don't use a Singleton pattern</a></li>
<li><a href="#encapsulate-conditionals">Encapsulate conditionals</a></li>
<li><a href="#avoid-negative-conditionals">Avoid negative conditionals</a></li>
<li><a href="#avoid-conditionals">Avoid conditionals</a></li>
<li><a href="#avoid-type-checking-part-1">Avoid type-checking (part 1)</a></li>
<li><a href="#avoid-type-checking-part-2">Avoid type-checking (part 2)</a></li>
<li><a href="#remove-dead-code">Remove dead code</a></li>
</ul>
</li>
<li><a href="#objects-and-data-structures">Objects and Data Structures</a>
<ul>
<li><a href="#use-object-encapsulation">Use object encapsulation</a></li>
<li><a href="#make-objects-have-privateprotected-members">Make objects have private/protected members</a></li>
</ul>
</li>
<li><a href="#classes">Classes</a>
<ul>
<li><a href="#prefer-composition-over-inheritance">Prefer composition over inheritance</a></li>
<li><a href="#avoid-fluent-interfaces">Avoid fluent interfaces</a></li>
</ul>
</li>
<li><a href="#solid">SOLID</a>
<ul>
<li><a href="#single-responsibility-principle-srp">Single Responsibility Principle (SRP)</a></li>
<li><a href="#openclosed-principle-ocp">Open/Closed Principle (OCP)</a></li>
<li><a href="#liskov-substitution-principle-lsp">Liskov Substitution Principle (LSP)</a></li>
<li><a href="#interface-segregation-principle-isp">Interface Segregation Principle (ISP)</a></li>
<li><a href="#dependency-inversion-principle-dip">Dependency Inversion Principle (DIP)</a></li>
</ul>
</li>
<li><a href="#dont-repeat-yourself-dry">Don’t repeat yourself (DRY)</a></li>
<li><a href="#translations">Translations</a></li>
</ol>
<h2><a href="#introduction" aria-hidden="true" class="anchor" id="user-content-introduction"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Introduction</h2>
<p>Software engineering principles, from Robert C. Martin's book
<a href="https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882"><em>Clean Code</em></a>,
adapted for PHP. This is not a style guide. It's a guide to producing
readable, reusable, and refactorable software in PHP.</p>
<p>Not every principle herein has to be strictly followed, and even fewer will be universally
agreed upon. These are guidelines and nothing more, but they are ones codified over many
years of collective experience by the authors of <em>Clean Code</em>.</p>
<p>Inspired from <a href="https://github.com/ryanmcdermott/clean-code-javascript">clean-code-javascript</a></p>
<p>Although many developers still use PHP 5, most of the examples in this article only work with PHP 7.1+.</p>
<h2><a href="#variables" aria-hidden="true" class="anchor" id="user-content-variables"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Variables</h2>
<h3><a href="#use-meaningful-and-pronounceable-variable-names" aria-hidden="true" class="anchor" id="user-content-use-meaningful-and-pronounceable-variable-names"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Use meaningful and pronounceable variable names</h3>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-smi">$ymdstr</span> <span class="pl-k">=</span> <span class="pl-smi">$moment</span><span class="pl-k">-&gt;</span>format(<span class="pl-s"><span class="pl-pds">'</span>y-m-d<span class="pl-pds">'</span></span>);</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-smi">$currentDate</span> <span class="pl-k">=</span> <span class="pl-smi">$moment</span><span class="pl-k">-&gt;</span>format(<span class="pl-s"><span class="pl-pds">'</span>y-m-d<span class="pl-pds">'</span></span>);</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#use-the-same-vocabulary-for-the-same-type-of-variable" aria-hidden="true" class="anchor" id="user-content-use-the-same-vocabulary-for-the-same-type-of-variable"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Use the same vocabulary for the same type of variable</h3>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1">getUserInfo();</span>
<span class="pl-s1">getUserData();</span>
<span class="pl-s1">getUserRecord();</span>
<span class="pl-s1">getUserProfile();</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1">getUser();</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#use-searchable-names-part-1" aria-hidden="true" class="anchor" id="user-content-use-searchable-names-part-1"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Use searchable names (part 1)</h3>
<p>We will read more code than we will ever write. It's important that the code we do write is
readable and searchable. By <em>not</em> naming variables that end up being meaningful for
understanding our program, we hurt our readers.
Make your names searchable.</p>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-c"><span class="pl-c">//</span> What the heck is 448 for?</span></span>
<span class="pl-s1"><span class="pl-smi">$result</span> <span class="pl-k">=</span> <span class="pl-smi">$serializer</span><span class="pl-k">-&gt;</span>serialize(<span class="pl-smi">$data</span>, <span class="pl-c1">448</span>);</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-smi">$json</span> <span class="pl-k">=</span> <span class="pl-smi">$serializer</span><span class="pl-k">-&gt;</span>serialize(<span class="pl-smi">$data</span>, <span class="pl-c1">JSON_UNESCAPED_SLASHES</span> <span class="pl-k">|</span> <span class="pl-c1">JSON_PRETTY_PRINT</span> <span class="pl-k">|</span> <span class="pl-c1">JSON_UNESCAPED_UNICODE</span>);</span></pre></div>
<h3><a href="#use-searchable-names-part-2" aria-hidden="true" class="anchor" id="user-content-use-searchable-names-part-2"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Use searchable names (part 2)</h3>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-c"><span class="pl-c">//</span> What the heck is 4 for?</span></span>
<span class="pl-s1"><span class="pl-k">if</span> (<span class="pl-smi">$user</span><span class="pl-k">-&gt;</span><span class="pl-smi">access</span> <span class="pl-k">&amp;</span> <span class="pl-c1">4</span>) {</span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">}</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">User</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">const</span> <span class="pl-c1">ACCESS_READ</span> <span class="pl-k">=</span> <span class="pl-c1">1</span>;</span>
<span class="pl-s1">    <span class="pl-k">const</span> <span class="pl-c1">ACCESS_CREATE</span> <span class="pl-k">=</span> <span class="pl-c1">2</span>;</span>
<span class="pl-s1"> <span class="pl-c1"> </span> <span class="pl-c1"> const</span> <span class="pl-c1">ACCESS_UPDATE</span> <span class="pl-k">=</span> <span class="pl-c1">4</span>;</span>
<span class="pl-s1">    <span class="pl-k">const</span> <span class="pl-c1">ACCESS_DELETE</span> <span class="pl-k">=</span> <span class="pl-c1">8</span>;</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">if</span> (<span class="pl-smi">$user</span><span class="pl-k">-&gt;</span><span class="pl-smi">access</span> <span class="pl-k">&amp;</span> <span class="pl-c1">User</span><span class="pl-k">::</span><span class="pl-c1">ACCESS_UPDATE</span>) {</span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> do edit ...</span></span>
<span class="pl-s1">}</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#use-explanatory-variables" aria-hidden="true" class="anchor" id="user-content-use-explanatory-variables"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Use explanatory variables</h3>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-smi">$address</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>One Infinite Loop, Cupertino 95014<span class="pl-pds">'</span></span>;</span>
<span class="pl-s1"><span class="pl-smi">$cityZipCodeRegex</span> <span class="pl-k">=</span> <span class="pl-sr"><span class="pl-pds">'/</span><span class="pl-k">^</span><span class="pl-pds">[^,<span class="pl-cce">\\]</span>+[,<span class="pl-cce">\\\</span>s]</span><span class="pl-k">+</span>(.<span class="pl-k">+</span>?)<span class="pl-cce">\s</span><span class="pl-k">*</span>(<span class="pl-cce">\d</span><span class="pl-sra">{5}</span>)?<span class="pl-k">$</span><span class="pl-pds">/'</span></span>;</span>
<span class="pl-s1"><span class="pl-c1">preg_match</span>(<span class="pl-smi">$cityZipCodeRegex</span>, <span class="pl-smi">$address</span>, <span class="pl-smi">$matches</span>);</span>
<span class="pl-s1"></span>
<span class="pl-s1">saveCityZipCode(<span class="pl-smi">$matches</span>[<span class="pl-c1">1</span>], <span class="pl-smi">$matches</span>[<span class="pl-c1">2</span>]);</span></pre></div>
<p><strong>Not bad:</strong></p>
<p>It's better, but we are still heavily dependent on regex.</p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-smi">$address</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>One Infinite Loop, Cupertino 95014<span class="pl-pds">'</span></span>;</span>
<span class="pl-s1"><span class="pl-smi">$cityZipCodeRegex</span> <span class="pl-k">=</span> <span class="pl-sr"><span class="pl-pds">'/</span><span class="pl-k">^</span><span class="pl-pds">[^,<span class="pl-cce">\\]</span>+[,<span class="pl-cce">\\\</span>s]</span><span class="pl-k">+</span>(.<span class="pl-k">+</span>?)<span class="pl-cce">\s</span><span class="pl-k">*</span>(<span class="pl-cce">\d</span><span class="pl-sra">{5}</span>)?<span class="pl-k">$</span><span class="pl-pds">/'</span></span>;</span>
<span class="pl-s1"><span class="pl-c1">preg_match</span>(<span class="pl-smi">$cityZipCodeRegex</span>, <span class="pl-smi">$address</span>, <span class="pl-smi">$matches</span>);</span>
<span class="pl-s1"></span>
<span class="pl-s1">[, <span class="pl-smi">$city</span>, <span class="pl-smi">$zipCode</span>] <span class="pl-k">=</span> <span class="pl-smi">$matches</span>;</span>
<span class="pl-s1">saveCityZipCode(<span class="pl-smi">$city</span>, <span class="pl-smi">$zipCode</span>);</span></pre></div>
<p><strong>Good:</strong></p>
<p>Decrease dependence on regex by naming subpatterns.</p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-smi">$address</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>One Infinite Loop, Cupertino 95014<span class="pl-pds">'</span></span>;</span>
<span class="pl-s1"><span class="pl-smi">$cityZipCodeRegex</span> <span class="pl-k">=</span> <span class="pl-sr"><span class="pl-pds">'/</span><span class="pl-k">^</span><span class="pl-pds">[^,<span class="pl-cce">\\]</span>+[,<span class="pl-cce">\\\</span>s]</span><span class="pl-k">+</span>(?&lt;city&gt;.<span class="pl-k">+</span>?)<span class="pl-cce">\s</span><span class="pl-k">*</span>(?&lt;zipCode&gt;<span class="pl-cce">\d</span><span class="pl-sra">{5}</span>)?<span class="pl-k">$</span><span class="pl-pds">/'</span></span>;</span>
<span class="pl-s1"><span class="pl-c1">preg_match</span>(<span class="pl-smi">$cityZipCodeRegex</span>, <span class="pl-smi">$address</span>, <span class="pl-smi">$matches</span>);</span>
<span class="pl-s1"></span>
<span class="pl-s1">saveCityZipCode(<span class="pl-smi">$matches</span>[<span class="pl-s"><span class="pl-pds">'</span>city<span class="pl-pds">'</span></span>], <span class="pl-smi">$matches</span>[<span class="pl-s"><span class="pl-pds">'</span>zipCode<span class="pl-pds">'</span></span>]);</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#avoid-nesting-too-deeply-and-return-early-part-1" aria-hidden="true" class="anchor" id="user-content-avoid-nesting-too-deeply-and-return-early-part-1"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Avoid nesting too deeply and return early (part 1)</h3>
<p>Too many if else statements can make your code hard to follow. Explicit is better
than implicit.</p>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">isShopOpen</span>(<span class="pl-smi">$day</span>): <span class="pl-k">bool</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">if</span> (<span class="pl-smi">$day</span>) {</span>
<span class="pl-s1">        <span class="pl-k">if</span> (<span class="pl-c1">is_string</span>(<span class="pl-smi">$day</span>)) {</span>
<span class="pl-s1">            <span class="pl-smi">$day</span> <span class="pl-k">=</span> <span class="pl-c1">strtolower</span>(<span class="pl-smi">$day</span>);</span>
<span class="pl-s1">            <span class="pl-k">if</span> (<span class="pl-smi">$day</span> <span class="pl-k">===</span> <span class="pl-s"><span class="pl-pds">'</span>friday<span class="pl-pds">'</span></span>) {</span>
<span class="pl-s1">                <span class="pl-k">return</span> <span class="pl-c1">true</span>;</span>
<span class="pl-s1">            } <span class="pl-k">elseif</span> (<span class="pl-smi">$day</span> <span class="pl-k">===</span> <span class="pl-s"><span class="pl-pds">'</span>saturday<span class="pl-pds">'</span></span>) {</span>
<span class="pl-s1">                <span class="pl-k">return</span> <span class="pl-c1">true</span>;</span>
<span class="pl-s1">            } <span class="pl-k">elseif</span> (<span class="pl-smi">$day</span> <span class="pl-k">===</span> <span class="pl-s"><span class="pl-pds">'</span>sunday<span class="pl-pds">'</span></span>) {</span>
<span class="pl-s1">                <span class="pl-k">return</span> <span class="pl-c1">true</span>;</span>
<span class="pl-s1">            } <span class="pl-k">else</span> {</span>
<span class="pl-s1">                <span class="pl-k">return</span> <span class="pl-c1">false</span>;</span>
<span class="pl-s1">            }</span>
<span class="pl-s1">        } <span class="pl-k">else</span> {</span>
<span class="pl-s1">            <span class="pl-k">return</span> <span class="pl-c1">false</span>;</span>
<span class="pl-s1">        }</span>
<span class="pl-s1">    } <span class="pl-k">else</span> {</span>
<span class="pl-s1">        <span class="pl-k">return</span> <span class="pl-c1">false</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">isShopOpen</span>(<span class="pl-c1">string</span> <span class="pl-smi">$day</span>): <span class="pl-k">bool</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">if</span> (<span class="pl-c1">empty</span>(<span class="pl-smi">$day</span>)) {</span>
<span class="pl-s1">        <span class="pl-k">return</span> <span class="pl-c1">false</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-smi">$openingDays</span> <span class="pl-k">=</span> [</span>
<span class="pl-s1">        <span class="pl-s"><span class="pl-pds">'</span>friday<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>saturday<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>sunday<span class="pl-pds">'</span></span></span>
<span class="pl-s1">    ];</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">return</span> <span class="pl-c1">in_array</span>(<span class="pl-c1">strtolower</span>(<span class="pl-smi">$day</span>), <span class="pl-smi">$openingDays</span>, <span class="pl-c1">true</span>);</span>
<span class="pl-s1">}</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#avoid-nesting-too-deeply-and-return-early-part-2" aria-hidden="true" class="anchor" id="user-content-avoid-nesting-too-deeply-and-return-early-part-2"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Avoid nesting too deeply and return early (part 2)</h3>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">fibonacci</span>(<span class="pl-c1">int</span> <span class="pl-smi">$n</span>)</span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">if</span> (<span class="pl-smi">$n</span> <span class="pl-k">&lt;</span> <span class="pl-c1">50</span>) {</span>
<span class="pl-s1">        <span class="pl-k">if</span> (<span class="pl-smi">$n</span> <span class="pl-k">!</span><span class="pl-k">==</span> <span class="pl-c1">0</span>) {</span>
<span class="pl-s1">            <span class="pl-k">if</span> (<span class="pl-smi">$n</span> <span class="pl-k">!</span><span class="pl-k">==</span> <span class="pl-c1">1</span>) {</span>
<span class="pl-s1">                <span class="pl-k">return</span> fibonacci(<span class="pl-smi">$n</span> <span class="pl-k">-</span> <span class="pl-c1">1</span>) <span class="pl-k">+</span> fibonacci(<span class="pl-smi">$n</span> <span class="pl-k">-</span> <span class="pl-c1">2</span>);</span>
<span class="pl-s1">            } <span class="pl-k">else</span> {</span>
<span class="pl-s1">                <span class="pl-k">return</span> <span class="pl-c1">1</span>;</span>
<span class="pl-s1">            }</span>
<span class="pl-s1">        } <span class="pl-k">else</span> {</span>
<span class="pl-s1">            <span class="pl-k">return</span> <span class="pl-c1">0</span>;</span>
<span class="pl-s1">        }</span>
<span class="pl-s1">    } <span class="pl-k">else</span> {</span>
<span class="pl-s1">        <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">'</span>Not supported<span class="pl-pds">'</span></span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">fibonacci</span>(<span class="pl-c1">int</span> <span class="pl-smi">$n</span>): <span class="pl-k">int</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">if</span> (<span class="pl-smi">$n</span> <span class="pl-k">===</span> <span class="pl-c1">0</span> <span class="pl-k">||</span> <span class="pl-smi">$n</span> <span class="pl-k">===</span> <span class="pl-c1">1</span>) {</span>
<span class="pl-s1">        <span class="pl-k">return</span> <span class="pl-smi">$n</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">if</span> (<span class="pl-smi">$n</span> <span class="pl-k">&gt;</span> <span class="pl-c1">50</span>) {</span>
<span class="pl-s1">        <span class="pl-k">throw</span> <span class="pl-k">new</span> <span class="pl-c1">\Exception</span>(<span class="pl-s"><span class="pl-pds">'</span>Not supported<span class="pl-pds">'</span></span>);</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">return</span> fibonacci(<span class="pl-smi">$n</span> <span class="pl-k">-</span> <span class="pl-c1">1</span>) <span class="pl-k">+</span> fibonacci(<span class="pl-smi">$n</span> <span class="pl-k">-</span> <span class="pl-c1">2</span>);</span>
<span class="pl-s1">}</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#avoid-mental-mapping" aria-hidden="true" class="anchor" id="user-content-avoid-mental-mapping"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Avoid Mental Mapping</h3>
<p>Don’t force the reader of your code to translate what the variable means.
Explicit is better than implicit.</p>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-smi">$l</span> <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">'</span>Austin<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>New York<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>San Francisco<span class="pl-pds">'</span></span>];</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">for</span> (<span class="pl-smi">$i</span> <span class="pl-k">=</span> <span class="pl-c1">0</span>; <span class="pl-smi">$i</span> <span class="pl-k">&lt;</span> <span class="pl-c1">count</span>(<span class="pl-smi">$l</span>); <span class="pl-smi">$i</span><span class="pl-k">++</span>) {</span>
<span class="pl-s1">    <span class="pl-smi">$li</span> <span class="pl-k">=</span> <span class="pl-smi">$l</span>[<span class="pl-smi">$i</span>];</span>
<span class="pl-s1">    doStuff();</span>
<span class="pl-s1">    doSomeOtherStuff();</span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> Wait, what is `$li` for again?</span></span>
<span class="pl-s1">    dispatch(<span class="pl-smi">$li</span>);</span>
<span class="pl-s1">}</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-smi">$locations</span> <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">'</span>Austin<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>New York<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>San Francisco<span class="pl-pds">'</span></span>];</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">foreach</span> (<span class="pl-smi">$locations</span> <span class="pl-k">as</span> <span class="pl-smi">$location</span>) {</span>
<span class="pl-s1">    doStuff();</span>
<span class="pl-s1">    doSomeOtherStuff();</span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">    dispatch(<span class="pl-smi">$location</span>);</span>
<span class="pl-s1">}</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#dont-add-unneeded-context" aria-hidden="true" class="anchor" id="user-content-dont-add-unneeded-context"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Don't add unneeded context</h3>
<p>If your class/object name tells you something, don't repeat that in your
variable name.</p>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Car</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-smi">$carMake</span>;</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-smi">$carModel</span>;</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-smi">$carColor</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span>...</span></span>
<span class="pl-s1">}</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Car</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-smi">$make</span>;</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-smi">$model</span>;</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-smi">$color</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span>...</span></span>
<span class="pl-s1">}</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#use-default-arguments-instead-of-short-circuiting-or-conditionals" aria-hidden="true" class="anchor" id="user-content-use-default-arguments-instead-of-short-circuiting-or-conditionals"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Use default arguments instead of short circuiting or conditionals</h3>
<p><strong>Not good:</strong></p>
<p>This is not good because <code>$breweryName</code> can be <code>NULL</code>.</p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">createMicrobrewery</span>(<span class="pl-smi">$breweryName</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>Hipster Brew Co.<span class="pl-pds">'</span></span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1"> <span class="pl-c1"> </span> <span class="pl-c1"> </span><span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">}</span></pre></div>
<p><strong>Not bad:</strong></p>
<p>This opinion is more understandable than the previous version, but it better controls the value of the variable.</p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">createMicrobrewery</span>(<span class="pl-smi">$name</span> <span class="pl-k">=</span> <span class="pl-c1">null</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1"> <span class="pl-c1"> </span> <span class="pl-c1"> </span><span class="pl-smi">$breweryName</span> <span class="pl-k">=</span> <span class="pl-smi">$name</span> ?: <span class="pl-s"><span class="pl-pds">'</span>Hipster Brew Co.<span class="pl-pds">'</span></span>;</span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">}</span></pre></div>
<p><strong>Good:</strong></p>
<p>If you support only PHP 7+, then you can use <a href="http://php.net/manual/en/functions.arguments.php#functions.arguments.type-declaration">type hinting</a> and be sure that the <code>$breweryName</code> will not be <code>NULL</code>.</p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">createMicrobrewery</span>(<span class="pl-c1">string</span> $<span class="pl-c1">breweryName</span> = '<span class="pl-c1">Hipster</span> <span class="pl-c1">Brew</span> <span class="pl-c1">Co</span>.'): <span class="pl-c1">void</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1"> <span class="pl-c1"> </span> <span class="pl-c1"> </span><span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">}</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h2><a href="#functions" aria-hidden="true" class="anchor" id="user-content-functions"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Functions</h2>
<h3><a href="#function-arguments-2-or-fewer-ideally" aria-hidden="true" class="anchor" id="user-content-function-arguments-2-or-fewer-ideally"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Function arguments (2 or fewer ideally)</h3>
<p>Limiting the amount of function parameters is incredibly important because it makes
testing your function easier. Having more than three leads to a combinatorial explosion
where you have to test tons of different cases with each separate argument.</p>
<p>Zero arguments is the ideal case. One or two arguments is ok, and three should be avoided.
Anything more than that should be consolidated. Usually, if you have more than two
arguments then your function is trying to do too much. In cases where it's not, most
of the time a higher-level object will suffice as an argument.</p>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">createMenu</span>(<span class="pl-c1">string</span> <span class="pl-smi">$title</span>, <span class="pl-c1">string</span> <span class="pl-smi">$body</span>, <span class="pl-c1">string</span> <span class="pl-smi">$buttonText</span>, <span class="pl-c1">bool</span> <span class="pl-smi">$cancellable</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">}</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">MenuConfig</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-smi">$title</span>;</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-smi">$body</span>;</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-smi">$buttonText</span>;</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-smi">$cancellable</span> <span class="pl-k">=</span> <span class="pl-c1">false</span>;</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-smi">$config</span> <span class="pl-k">=</span> <span class="pl-k">new</span> <span class="pl-c1">MenuConfig</span>();</span>
<span class="pl-s1"><span class="pl-smi">$config</span><span class="pl-k">-&gt;</span><span class="pl-smi">title</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>Foo<span class="pl-pds">'</span></span>;</span>
<span class="pl-s1"><span class="pl-smi">$config</span><span class="pl-k">-&gt;</span><span class="pl-smi">body</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>Bar<span class="pl-pds">'</span></span>;</span>
<span class="pl-s1"><span class="pl-smi">$config</span><span class="pl-k">-&gt;</span><span class="pl-smi">buttonText</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>Baz<span class="pl-pds">'</span></span>;</span>
<span class="pl-s1"><span class="pl-smi">$config</span><span class="pl-k">-&gt;</span><span class="pl-smi">cancellable</span> <span class="pl-k">=</span> <span class="pl-c1">true</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">createMenu</span>(<span class="pl-c1">MenuConfig</span> <span class="pl-smi">$config</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">}</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#functions-should-do-one-thing" aria-hidden="true" class="anchor" id="user-content-functions-should-do-one-thing"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Functions should do one thing</h3>
<p>This is by far the most important rule in software engineering. When functions do more
than one thing, they are harder to compose, test, and reason about. When you can isolate
a function to just one action, they can be refactored easily and your code will read much
cleaner. If you take nothing else away from this guide other than this, you'll be ahead
of many developers.</p>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">emailClients</span>(<span class="pl-k">array</span> <span class="pl-smi">$clients</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">foreach</span> (<span class="pl-smi">$clients</span> <span class="pl-k">as</span> <span class="pl-smi">$client</span>) {</span>
<span class="pl-s1">        <span class="pl-smi">$clientRecord</span> <span class="pl-k">=</span> <span class="pl-smi">$db</span><span class="pl-k">-&gt;</span>find(<span class="pl-smi">$client</span>);</span>
<span class="pl-s1">        <span class="pl-k">if</span> (<span class="pl-smi">$clientRecord</span><span class="pl-k">-&gt;</span>isActive()) {</span>
<span class="pl-s1">            email(<span class="pl-smi">$client</span>);</span>
<span class="pl-s1">        }</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">emailClients</span>(<span class="pl-k">array</span> <span class="pl-smi">$clients</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-smi">$activeClients</span> <span class="pl-k">=</span> activeClients(<span class="pl-smi">$clients</span>);</span>
<span class="pl-s1">    <span class="pl-c1">array_walk</span>(<span class="pl-smi">$activeClients</span>, <span class="pl-s"><span class="pl-pds">'</span>email<span class="pl-pds">'</span></span>);</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">activeClients</span>(<span class="pl-k">array</span> <span class="pl-smi">$clients</span>): <span class="pl-k">array</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">return</span> <span class="pl-c1">array_filter</span>(<span class="pl-smi">$clients</span>, <span class="pl-s"><span class="pl-pds">'</span>isClientActive<span class="pl-pds">'</span></span>);</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">isClientActive</span>(<span class="pl-c1">int</span> <span class="pl-smi">$client</span>): <span class="pl-k">bool</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-smi">$clientRecord</span> <span class="pl-k">=</span> <span class="pl-smi">$db</span><span class="pl-k">-&gt;</span>find(<span class="pl-smi">$client</span>);</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">return</span> <span class="pl-smi">$clientRecord</span><span class="pl-k">-&gt;</span>isActive();</span>
<span class="pl-s1">}</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#function-names-should-say-what-they-do" aria-hidden="true" class="anchor" id="user-content-function-names-should-say-what-they-do"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Function names should say what they do</h3>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Email</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span>...</span></span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">handle</span>(): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-c1">mail</span>(<span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">to</span>, <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">subject</span>, <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">body</span>);</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-smi">$message</span> <span class="pl-k">=</span> <span class="pl-k">new</span> <span class="pl-c1">Email</span>(<span class="pl-k">...</span>);</span>
<span class="pl-s1"><span class="pl-c"><span class="pl-c">//</span> What is this? A handle for the message? Are we writing to a file now?</span></span>
<span class="pl-s1"><span class="pl-smi">$message</span><span class="pl-k">-&gt;</span>handle();</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Email</span> </span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span>...</span></span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">send</span>(): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-c1">mail</span>(<span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">to</span>, <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">subject</span>, <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">body</span>);</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-smi">$message</span> <span class="pl-k">=</span> <span class="pl-k">new</span> <span class="pl-c1">Email</span>(<span class="pl-k">...</span>);</span>
<span class="pl-s1"><span class="pl-c"><span class="pl-c">//</span> Clear and obvious</span></span>
<span class="pl-s1"><span class="pl-smi">$message</span><span class="pl-k">-&gt;</span>send();</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#functions-should-only-be-one-level-of-abstraction" aria-hidden="true" class="anchor" id="user-content-functions-should-only-be-one-level-of-abstraction"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Functions should only be one level of abstraction</h3>
<p>When you have more than one level of abstraction your function is usually
doing too much. Splitting up functions leads to reusability and easier
testing.</p>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">parseBetterJSAlternative</span>(<span class="pl-c1">string</span> <span class="pl-smi">$code</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-smi">$regexes</span> <span class="pl-k">=</span> [</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">    ];</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-smi">$statements</span> <span class="pl-k">=</span> <span class="pl-c1">explode</span>(<span class="pl-s"><span class="pl-pds">'</span> <span class="pl-pds">'</span></span>, <span class="pl-smi">$code</span>);</span>
<span class="pl-s1">    <span class="pl-smi">$tokens</span> <span class="pl-k">=</span> [];</span>
<span class="pl-s1">    <span class="pl-k">foreach</span> (<span class="pl-smi">$regexes</span> <span class="pl-k">as</span> <span class="pl-smi">$regex</span>) {</span>
<span class="pl-s1">        <span class="pl-k">foreach</span> (<span class="pl-smi">$statements</span> <span class="pl-k">as</span> <span class="pl-smi">$statement</span>) {</span>
<span class="pl-s1">            <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">        }</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-smi">$ast</span> <span class="pl-k">=</span> [];</span>
<span class="pl-s1">    <span class="pl-k">foreach</span> (<span class="pl-smi">$tokens</span> <span class="pl-k">as</span> <span class="pl-smi">$token</span>) {</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span> lex...</span></span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">foreach</span> (<span class="pl-smi">$ast</span> <span class="pl-k">as</span> <span class="pl-smi">$node</span>) {</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span> parse...</span></span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span></pre></div>
<p><strong>Bad too:</strong></p>
<p>We have carried out some of the functionality, but the <code>parseBetterJSAlternative()</code> function is still very complex and not testable.</p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">tokenize</span>(<span class="pl-c1">string</span> <span class="pl-smi">$code</span>): <span class="pl-k">array</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-smi">$regexes</span> <span class="pl-k">=</span> [</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">    ];</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-smi">$statements</span> <span class="pl-k">=</span> <span class="pl-c1">explode</span>(<span class="pl-s"><span class="pl-pds">'</span> <span class="pl-pds">'</span></span>, <span class="pl-smi">$code</span>);</span>
<span class="pl-s1">    <span class="pl-smi">$tokens</span> <span class="pl-k">=</span> [];</span>
<span class="pl-s1">    <span class="pl-k">foreach</span> (<span class="pl-smi">$regexes</span> <span class="pl-k">as</span> <span class="pl-smi">$regex</span>) {</span>
<span class="pl-s1">        <span class="pl-k">foreach</span> (<span class="pl-smi">$statements</span> <span class="pl-k">as</span> <span class="pl-smi">$statement</span>) {</span>
<span class="pl-s1">            <span class="pl-smi">$tokens</span>[] <span class="pl-k">=</span> <span class="pl-c"><span class="pl-c">/*</span> ... <span class="pl-c">*/</span></span>;</span>
<span class="pl-s1">        }</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">return</span> <span class="pl-smi">$tokens</span>;</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">lexer</span>(<span class="pl-k">array</span> <span class="pl-smi">$tokens</span>): <span class="pl-k">array</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-smi">$ast</span> <span class="pl-k">=</span> [];</span>
<span class="pl-s1">    <span class="pl-k">foreach</span> (<span class="pl-smi">$tokens</span> <span class="pl-k">as</span> <span class="pl-smi">$token</span>) {</span>
<span class="pl-s1">        <span class="pl-smi">$ast</span>[] <span class="pl-k">=</span> <span class="pl-c"><span class="pl-c">/*</span> ... <span class="pl-c">*/</span></span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">return</span> <span class="pl-smi">$ast</span>;</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">parseBetterJSAlternative</span>(<span class="pl-c1">string</span> <span class="pl-smi">$code</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-smi">$tokens</span> <span class="pl-k">=</span> tokenize(<span class="pl-smi">$code</span>);</span>
<span class="pl-s1">    <span class="pl-smi">$ast</span> <span class="pl-k">=</span> lexer(<span class="pl-smi">$tokens</span>);</span>
<span class="pl-s1">    <span class="pl-k">foreach</span> (<span class="pl-smi">$ast</span> <span class="pl-k">as</span> <span class="pl-smi">$node</span>) {</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span> parse...</span></span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span></pre></div>
<p><strong>Good:</strong></p>
<p>The best solution is move out the dependencies of <code>parseBetterJSAlternative()</code> function.</p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Tokenizer</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">tokenize</span>(<span class="pl-c1">string</span> <span class="pl-smi">$code</span>): <span class="pl-k">array</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$regexes</span> <span class="pl-k">=</span> [</span>
<span class="pl-s1">            <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">        ];</span>
<span class="pl-s1"></span>
<span class="pl-s1">        <span class="pl-smi">$statements</span> <span class="pl-k">=</span> <span class="pl-c1">explode</span>(<span class="pl-s"><span class="pl-pds">'</span> <span class="pl-pds">'</span></span>, <span class="pl-smi">$code</span>);</span>
<span class="pl-s1">        <span class="pl-smi">$tokens</span> <span class="pl-k">=</span> [];</span>
<span class="pl-s1">        <span class="pl-k">foreach</span> (<span class="pl-smi">$regexes</span> <span class="pl-k">as</span> <span class="pl-smi">$regex</span>) {</span>
<span class="pl-s1">            <span class="pl-k">foreach</span> (<span class="pl-smi">$statements</span> <span class="pl-k">as</span> <span class="pl-smi">$statement</span>) {</span>
<span class="pl-s1">                <span class="pl-smi">$tokens</span>[] <span class="pl-k">=</span> <span class="pl-c"><span class="pl-c">/*</span> ... <span class="pl-c">*/</span></span>;</span>
<span class="pl-s1">            }</span>
<span class="pl-s1">        }</span>
<span class="pl-s1"></span>
<span class="pl-s1">        <span class="pl-k">return</span> <span class="pl-smi">$tokens</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Lexer</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">lexify</span>(<span class="pl-k">array</span> <span class="pl-smi">$tokens</span>): <span class="pl-k">array</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$ast</span> <span class="pl-k">=</span> [];</span>
<span class="pl-s1">        <span class="pl-k">foreach</span> (<span class="pl-smi">$tokens</span> <span class="pl-k">as</span> <span class="pl-smi">$token</span>) {</span>
<span class="pl-s1">            <span class="pl-smi">$ast</span>[] <span class="pl-k">=</span> <span class="pl-c"><span class="pl-c">/*</span> ... <span class="pl-c">*/</span></span>;</span>
<span class="pl-s1">        }</span>
<span class="pl-s1"></span>
<span class="pl-s1">        <span class="pl-k">return</span> <span class="pl-smi">$ast</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">BetterJSAlternative</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$tokenizer</span>;</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$lexer</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-c1">__construct</span>(<span class="pl-c1">Tokenizer</span> <span class="pl-smi">$tokenizer</span>, <span class="pl-c1">Lexer</span> <span class="pl-smi">$lexer</span>)</span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">tokenizer</span> <span class="pl-k">=</span> <span class="pl-smi">$tokenizer</span>;</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">lexer</span> <span class="pl-k">=</span> <span class="pl-smi">$lexer</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">parse</span>(<span class="pl-c1">string</span> <span class="pl-smi">$code</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$tokens</span> <span class="pl-k">=</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">tokenizer</span><span class="pl-k">-&gt;</span>tokenize(<span class="pl-smi">$code</span>);</span>
<span class="pl-s1">        <span class="pl-smi">$ast</span> <span class="pl-k">=</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">lexer</span><span class="pl-k">-&gt;</span>lexify(<span class="pl-smi">$tokens</span>);</span>
<span class="pl-s1">        <span class="pl-k">foreach</span> (<span class="pl-smi">$ast</span> <span class="pl-k">as</span> <span class="pl-smi">$node</span>) {</span>
<span class="pl-s1">            <span class="pl-c"><span class="pl-c">//</span> parse...</span></span>
<span class="pl-s1">        }</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#dont-use-flags-as-function-parameters" aria-hidden="true" class="anchor" id="user-content-dont-use-flags-as-function-parameters"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Don't use flags as function parameters</h3>
<p>Flags tell your user that this function does more than one thing. Functions should
do one thing. Split out your functions if they are following different code paths
based on a boolean.</p>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">createFile</span>(<span class="pl-c1">string</span> <span class="pl-smi">$name</span>, <span class="pl-c1">bool</span> <span class="pl-smi">$temp</span> <span class="pl-k">=</span> <span class="pl-ii">false</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">if</span> (<span class="pl-smi">$temp</span>) {</span>
<span class="pl-s1">        <span class="pl-c1">touch</span>(<span class="pl-s"><span class="pl-pds">'</span>./temp/<span class="pl-pds">'</span></span><span class="pl-k">.</span><span class="pl-smi">$name</span>);</span>
<span class="pl-s1">    } <span class="pl-k">else</span> {</span>
<span class="pl-s1">        <span class="pl-c1">touch</span>(<span class="pl-smi">$name</span>);</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">createFile</span>(<span class="pl-c1">string</span> <span class="pl-smi">$name</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-c1">touch</span>(<span class="pl-smi">$name</span>);</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">createTempFile</span>(<span class="pl-c1">string</span> <span class="pl-smi">$name</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-c1">touch</span>(<span class="pl-s"><span class="pl-pds">'</span>./temp/<span class="pl-pds">'</span></span><span class="pl-k">.</span><span class="pl-smi">$name</span>);</span>
<span class="pl-s1">}</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#avoid-side-effects" aria-hidden="true" class="anchor" id="user-content-avoid-side-effects"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Avoid Side Effects</h3>
<p>A function produces a side effect if it does anything other than take a value in and
return another value or values. A side effect could be writing to a file, modifying
some global variable, or accidentally wiring all your money to a stranger.</p>
<p>Now, you do need to have side effects in a program on occasion. Like the previous
example, you might need to write to a file. What you want to do is to centralize where
you are doing this. Don't have several functions and classes that write to a particular
file. Have one service that does it. One and only one.</p>
<p>The main point is to avoid common pitfalls like sharing state between objects without
any structure, using mutable data types that can be written to by anything, and not
centralizing where your side effects occur. If you can do this, you will be happier
than the vast majority of other programmers.</p>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-c"><span class="pl-c">//</span> Global variable referenced by following function.</span></span>
<span class="pl-s1"><span class="pl-c"><span class="pl-c">//</span> If we had another function that used this name, now it'd be an array and it could break it.</span></span>
<span class="pl-s1"><span class="pl-smi">$name</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>Ryan McDermott<span class="pl-pds">'</span></span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">splitIntoFirstAndLastName</span>(): <span class="pl-c1">void</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">global</span> <span class="pl-smi">$name</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-smi">$name</span> <span class="pl-k">=</span> <span class="pl-c1">explode</span>(<span class="pl-s"><span class="pl-pds">'</span> <span class="pl-pds">'</span></span>, <span class="pl-smi">$name</span>);</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1">splitIntoFirstAndLastName();</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-c1">var_dump</span>(<span class="pl-smi">$name</span>); <span class="pl-c"><span class="pl-c">//</span> ['Ryan', 'McDermott'];</span></span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">splitIntoFirstAndLastName</span>(<span class="pl-c1">string</span> <span class="pl-smi">$name</span>): <span class="pl-k">array</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">return</span> <span class="pl-c1">explode</span>(<span class="pl-s"><span class="pl-pds">'</span> <span class="pl-pds">'</span></span>, <span class="pl-smi">$name</span>);</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-smi">$name</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>Ryan McDermott<span class="pl-pds">'</span></span>;</span>
<span class="pl-s1"><span class="pl-smi">$newName</span> <span class="pl-k">=</span> splitIntoFirstAndLastName(<span class="pl-smi">$name</span>);</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-c1">var_dump</span>(<span class="pl-smi">$name</span>); <span class="pl-c"><span class="pl-c">//</span> 'Ryan McDermott';</span></span>
<span class="pl-s1"><span class="pl-c1">var_dump</span>(<span class="pl-smi">$newName</span>); <span class="pl-c"><span class="pl-c">//</span> ['Ryan', 'McDermott'];</span></span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#dont-write-to-global-functions" aria-hidden="true" class="anchor" id="user-content-dont-write-to-global-functions"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Don't write to global functions</h3>
<p>Polluting globals is a bad practice in many languages because you could clash with another
library and the user of your API would be none-the-wiser until they get an exception in
production. Let's think about an example: what if you wanted to have configuration array.
You could write global function like <code>config()</code>, but it could clash with another library
that tried to do the same thing.</p>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">config</span>(): <span class="pl-k">array</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">return</span>  [</span>
<span class="pl-s1">        <span class="pl-s"><span class="pl-pds">'</span>foo<span class="pl-pds">'</span></span> <span class="pl-k">=&gt;</span> <span class="pl-s"><span class="pl-pds">'</span>bar<span class="pl-pds">'</span></span>,</span>
<span class="pl-s1">    ]</span>
<span class="pl-s1">}</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Configuration</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$configuration</span> <span class="pl-k">=</span> [];</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-c1">__construct</span>(<span class="pl-k">array</span> <span class="pl-smi">$configuration</span>)</span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">configuration</span> <span class="pl-k">=</span> <span class="pl-smi">$configuration</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">get</span>(<span class="pl-c1">string</span> <span class="pl-smi">$key</span>): ?<span class="pl-k">string</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-k">return</span> <span class="pl-c1">isset</span>(<span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">configuration</span>[<span class="pl-smi">$key</span>]) ? <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">configuration</span>[<span class="pl-smi">$key</span>] : <span class="pl-c1">null</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span></pre></div>
<p>Load configuration and create instance of <code>Configuration</code> class</p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-smi">$configuration</span> <span class="pl-k">=</span> <span class="pl-k">new</span> <span class="pl-c1">Configuration</span>([</span>
<span class="pl-s1">    <span class="pl-s"><span class="pl-pds">'</span>foo<span class="pl-pds">'</span></span> <span class="pl-k">=&gt;</span> <span class="pl-s"><span class="pl-pds">'</span>bar<span class="pl-pds">'</span></span>,</span>
<span class="pl-s1">]);</span></pre></div>
<p>And now you must use instance of <code>Configuration</code> in your application.</p>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#dont-use-a-singleton-pattern" aria-hidden="true" class="anchor" id="user-content-dont-use-a-singleton-pattern"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Don't use a Singleton pattern</h3>
<p>Singleton is an <a href="https://en.wikipedia.org/wiki/Singleton_pattern">anti-pattern</a>. Paraphrased from Brian Button:</p>
<ol>
<li>They are generally used as a <strong>global instance</strong>, why is that so bad? Because <strong>you hide the dependencies</strong> of your application in your code, instead of exposing them through the interfaces. Making something global to avoid passing it around is a <a href="https://en.wikipedia.org/wiki/Code_smell">code smell</a>.</li>
<li>They violate the <a href="#single-responsibility-principle-srp">single responsibility principle</a>: by virtue of the fact that <strong>they control their own creation and lifecycle</strong>.</li>
<li>They inherently cause code to be tightly <a href="https://en.wikipedia.org/wiki/Coupling_%28computer_programming%29">coupled</a>. This makes faking them out under <strong>test rather difficult</strong> in many cases.</li>
<li>They carry state around for the lifetime of the application. Another hit to testing since <strong>you can end up with a situation where tests need to be ordered</strong> which is a big no for unit tests. Why? Because each unit test should be independent from the other.</li>
</ol>
<p>There is also very good thoughts by <a href="http://misko.hevery.com/about/">Misko Hevery</a> about the <a href="http://misko.hevery.com/2008/08/25/root-cause-of-singletons/">root of problem</a>.</p>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">DBConnection</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-k">static</span> <span class="pl-smi">$instance</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-k">function</span> <span class="pl-c1">__construct</span>(<span class="pl-c1">string</span> <span class="pl-smi">$dsn</span>)</span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">static</span> <span class="pl-k">function</span> <span class="pl-en">getInstance</span>(): <span class="pl-c1">DBConnection</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-k">if</span> (<span class="pl-k">self</span><span class="pl-k">::</span><span class="pl-smi">$instance</span> <span class="pl-k">===</span> <span class="pl-c1">null</span>) {</span>
<span class="pl-s1">            <span class="pl-k">self</span><span class="pl-k">::</span><span class="pl-smi">$instance</span> <span class="pl-k">=</span> <span class="pl-k">new</span> <span class="pl-k">self</span>();</span>
<span class="pl-s1">        }</span>
<span class="pl-s1"></span>
<span class="pl-s1">        <span class="pl-k">return</span> <span class="pl-k">self</span><span class="pl-k">::</span><span class="pl-smi">$instance</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-smi">$singleton</span> <span class="pl-k">=</span> <span class="pl-c1">DBConnection</span><span class="pl-k">::</span>getInstance();</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">DBConnection</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-c1">__construct</span>(<span class="pl-c1">string</span> <span class="pl-smi">$dsn</span>)</span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">     <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">}</span></pre></div>
<p>Create instance of <code>DBConnection</code> class and configure it with <a href="http://php.net/manual/en/pdo.construct.php#refsect1-pdo.construct-parameters">DSN</a>.</p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-smi">$connection</span> <span class="pl-k">=</span> <span class="pl-k">new</span> <span class="pl-c1">DBConnection</span>(<span class="pl-smi">$dsn</span>);</span></pre></div>
<p>And now you must use instance of <code>DBConnection</code> in your application.</p>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#encapsulate-conditionals" aria-hidden="true" class="anchor" id="user-content-encapsulate-conditionals"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Encapsulate conditionals</h3>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">if</span> (<span class="pl-smi">$article</span><span class="pl-k">-&gt;</span><span class="pl-smi">state</span> <span class="pl-k">===</span> <span class="pl-s"><span class="pl-pds">'</span>published<span class="pl-pds">'</span></span>) {</span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">}</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">if</span> (<span class="pl-smi">$article</span><span class="pl-k">-&gt;</span>isPublished()) {</span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">}</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#avoid-negative-conditionals" aria-hidden="true" class="anchor" id="user-content-avoid-negative-conditionals"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Avoid negative conditionals</h3>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">isDOMNodeNotPresent</span>(<span class="pl-c1">\DOMNode</span> <span class="pl-smi">$node</span>): <span class="pl-k">bool</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">if</span> (<span class="pl-k">!</span>isDOMNodeNotPresent(<span class="pl-smi">$node</span>))</span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">}</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">isDOMNodePresent</span>(<span class="pl-c1">\DOMNode</span> <span class="pl-smi">$node</span>): <span class="pl-k">bool</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">if</span> (isDOMNodePresent(<span class="pl-smi">$node</span>)) {</span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">}</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#avoid-conditionals" aria-hidden="true" class="anchor" id="user-content-avoid-conditionals"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Avoid conditionals</h3>
<p>This seems like an impossible task. Upon first hearing this, most people say,
"how am I supposed to do anything without an <code>if</code> statement?" The answer is that
you can use polymorphism to achieve the same task in many cases. The second
question is usually, "well that's great but why would I want to do that?" The
answer is a previous clean code concept we learned: a function should only do
one thing. When you have classes and functions that have <code>if</code> statements, you
are telling your user that your function does more than one thing. Remember,
just do one thing.</p>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Airplane</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">getCruisingAltitude</span>(): <span class="pl-k">int</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-k">switch</span> (<span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">type</span>) {</span>
<span class="pl-s1">            <span class="pl-k">case</span> <span class="pl-s"><span class="pl-pds">'</span>777<span class="pl-pds">'</span></span>:</span>
<span class="pl-s1">                <span class="pl-k">return</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span>getMaxAltitude() <span class="pl-k">-</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span>getPassengerCount();</span>
<span class="pl-s1">            <span class="pl-k">case</span> <span class="pl-s"><span class="pl-pds">'</span>Air Force One<span class="pl-pds">'</span></span>:</span>
<span class="pl-s1">                <span class="pl-k">return</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span>getMaxAltitude();</span>
<span class="pl-s1">            <span class="pl-k">case</span> <span class="pl-s"><span class="pl-pds">'</span>Cessna<span class="pl-pds">'</span></span>:</span>
<span class="pl-s1">                <span class="pl-k">return</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span>getMaxAltitude() <span class="pl-k">-</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span>getFuelExpenditure();</span>
<span class="pl-s1">        }</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">interface</span> <span class="pl-en">Airplane</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">getCruisingAltitude</span>(): <span class="pl-k">int</span>;</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Boeing777</span> <span class="pl-k">implements</span> <span class="pl-e">Airplane</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">getCruisingAltitude</span>(): <span class="pl-k">int</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-k">return</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span>getMaxAltitude() <span class="pl-k">-</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span>getPassengerCount();</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">AirForceOne</span> <span class="pl-k">implements</span> <span class="pl-e">Airplane</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">getCruisingAltitude</span>(): <span class="pl-k">int</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-k">return</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span>getMaxAltitude();</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Cessna</span> <span class="pl-k">implements</span> <span class="pl-e">Airplane</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">getCruisingAltitude</span>(): <span class="pl-k">int</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-k">return</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span>getMaxAltitude() <span class="pl-k">-</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span>getFuelExpenditure();</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#avoid-type-checking-part-1" aria-hidden="true" class="anchor" id="user-content-avoid-type-checking-part-1"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Avoid type-checking (part 1)</h3>
<p>PHP is untyped, which means your functions can take any type of argument.
Sometimes you are bitten by this freedom and it becomes tempting to do
type-checking in your functions. There are many ways to avoid having to do this.
The first thing to consider is consistent APIs.</p>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">travelToTexas</span>(<span class="pl-smi">$vehicle</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">if</span> (<span class="pl-smi">$vehicle</span> <span class="pl-k">instanceof</span> <span class="pl-c1">Bicycle</span>) {</span>
<span class="pl-s1">        <span class="pl-smi">$vehicle</span><span class="pl-k">-&gt;</span>pedalTo(<span class="pl-k">new</span> <span class="pl-c1">Location</span>(<span class="pl-s"><span class="pl-pds">'</span>texas<span class="pl-pds">'</span></span>));</span>
<span class="pl-s1">    } <span class="pl-k">elseif</span> (<span class="pl-smi">$vehicle</span> <span class="pl-k">instanceof</span> <span class="pl-c1">Car</span>) {</span>
<span class="pl-s1">        <span class="pl-smi">$vehicle</span><span class="pl-k">-&gt;</span>driveTo(<span class="pl-k">new</span> <span class="pl-c1">Location</span>(<span class="pl-s"><span class="pl-pds">'</span>texas<span class="pl-pds">'</span></span>));</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">travelToTexas</span>(<span class="pl-c1">Traveler</span> <span class="pl-smi">$vehicle</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-smi">$vehicle</span><span class="pl-k">-&gt;</span>travelTo(<span class="pl-k">new</span> <span class="pl-c1">Location</span>(<span class="pl-s"><span class="pl-pds">'</span>texas<span class="pl-pds">'</span></span>));</span>
<span class="pl-s1">}</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#avoid-type-checking-part-2" aria-hidden="true" class="anchor" id="user-content-avoid-type-checking-part-2"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Avoid type-checking (part 2)</h3>
<p>If you are working with basic primitive values like strings, integers, and arrays,
and you use PHP 7+ and you can't use polymorphism but you still feel the need to
type-check, you should consider
<a href="http://php.net/manual/en/functions.arguments.php#functions.arguments.type-declaration">type declaration</a>
or strict mode. It provides you with static typing on top of standard PHP syntax.
The problem with manually type-checking is that doing it will require so much
extra verbiage that the faux "type-safety" you get doesn't make up for the lost
readability. Keep your PHP clean, write good tests, and have good code reviews.
Otherwise, do all of that but with PHP strict type declaration or strict mode.</p>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">combine</span>(<span class="pl-smi">$val1</span>, <span class="pl-smi">$val2</span>): <span class="pl-k">int</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">if</span> (<span class="pl-k">!</span><span class="pl-c1">is_numeric</span>(<span class="pl-smi">$val1</span>) <span class="pl-k">||</span> <span class="pl-k">!</span><span class="pl-c1">is_numeric</span>(<span class="pl-smi">$val2</span>)) {</span>
<span class="pl-s1">        <span class="pl-k">throw</span> <span class="pl-k">new</span> <span class="pl-c1">\Exception</span>(<span class="pl-s"><span class="pl-pds">'</span>Must be of type Number<span class="pl-pds">'</span></span>);</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">return</span> <span class="pl-smi">$val1</span> <span class="pl-k">+</span> <span class="pl-smi">$val2</span>;</span>
<span class="pl-s1">}</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">combine</span>(<span class="pl-c1">int</span> <span class="pl-smi">$val1</span>, <span class="pl-c1">int</span> <span class="pl-smi">$val2</span>): <span class="pl-k">int</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">return</span> <span class="pl-smi">$val1</span> <span class="pl-k">+</span> <span class="pl-smi">$val2</span>;</span>
<span class="pl-s1">}</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#remove-dead-code" aria-hidden="true" class="anchor" id="user-content-remove-dead-code"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Remove dead code</h3>
<p>Dead code is just as bad as duplicate code. There's no reason to keep it in
your codebase. If it's not being called, get rid of it! It will still be safe
in your version history if you still need it.</p>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">oldRequestModule</span>(<span class="pl-c1">string</span> <span class="pl-smi">$url</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">newRequestModule</span>(<span class="pl-c1">string</span> <span class="pl-smi">$url</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-smi">$request</span> <span class="pl-k">=</span> newRequestModule(<span class="pl-smi">$requestUrl</span>);</span>
<span class="pl-s1">inventoryTracker(<span class="pl-s"><span class="pl-pds">'</span>apples<span class="pl-pds">'</span></span>, <span class="pl-smi">$request</span>, <span class="pl-s"><span class="pl-pds">'</span>www.inventory-awesome.io<span class="pl-pds">'</span></span>);</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">requestModule</span>(<span class="pl-c1">string</span> <span class="pl-smi">$url</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-smi">$request</span> <span class="pl-k">=</span> requestModule(<span class="pl-smi">$requestUrl</span>);</span>
<span class="pl-s1">inventoryTracker(<span class="pl-s"><span class="pl-pds">'</span>apples<span class="pl-pds">'</span></span>, <span class="pl-smi">$request</span>, <span class="pl-s"><span class="pl-pds">'</span>www.inventory-awesome.io<span class="pl-pds">'</span></span>);</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h2><a href="#objects-and-data-structures" aria-hidden="true" class="anchor" id="user-content-objects-and-data-structures"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Objects and Data Structures</h2>
<h3><a href="#use-object-encapsulation" aria-hidden="true" class="anchor" id="user-content-use-object-encapsulation"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Use object encapsulation</h3>
<p>In PHP you can set <code>public</code>, <code>protected</code> and <code>private</code> keywords for methods.
Using it, you can control properties modification on an object.</p>
<ul>
<li>When you want to do more beyond getting an object property, you don't have
to look up and change every accessor in your codebase.</li>
<li>Makes adding validation simple when doing a <code>set</code>.</li>
<li>Encapsulates the internal representation.</li>
<li>Easy to add logging and error handling when getting and setting.</li>
<li>Inheriting this class, you can override default functionality.</li>
<li>You can lazy load your object's properties, let's say getting it from a
server.</li>
</ul>
<p>Additionally, this is part of <a href="#openclosed-principle-ocp">Open/Closed</a> principle.</p>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">BankAccount</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-smi">$balance</span> <span class="pl-k">=</span> <span class="pl-c1">1000</span>;</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-smi">$bankAccount</span> <span class="pl-k">=</span> <span class="pl-k">new</span> <span class="pl-c1">BankAccount</span>();</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-c"><span class="pl-c">//</span> Buy shoes...</span></span>
<span class="pl-s1"><span class="pl-smi">$bankAccount</span><span class="pl-k">-&gt;</span><span class="pl-smi">balance</span> <span class="pl-k">-</span><span class="pl-k">=</span> <span class="pl-c1">100</span>;</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">BankAccount</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$balance</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-c1">__construct</span>(<span class="pl-c1">int</span> <span class="pl-smi">$balance</span> <span class="pl-k">=</span> <span class="pl-ii">1000</span>)</span>
<span class="pl-s1">    {</span>
<span class="pl-s1">      <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">balance</span> <span class="pl-k">=</span> <span class="pl-smi">$balance</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">withdrawBalance</span>(<span class="pl-c1">int</span> <span class="pl-smi">$amount</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-k">if</span> (<span class="pl-smi">$amount</span> <span class="pl-k">&gt;</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">balance</span>) {</span>
<span class="pl-s1">            <span class="pl-k">throw</span> <span class="pl-k">new</span> <span class="pl-c1">\Exception</span>(<span class="pl-s"><span class="pl-pds">'</span>Amount greater than available balance.<span class="pl-pds">'</span></span>);</span>
<span class="pl-s1">        }</span>
<span class="pl-s1"></span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">balance</span> <span class="pl-k">-</span><span class="pl-k">=</span> <span class="pl-smi">$amount</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">depositBalance</span>(<span class="pl-c1">int</span> <span class="pl-smi">$amount</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">balance</span> <span class="pl-k">+</span><span class="pl-k">=</span> <span class="pl-smi">$amount</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">getBalance</span>(): <span class="pl-k">int</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-k">return</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">balance</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-smi">$bankAccount</span> <span class="pl-k">=</span> <span class="pl-k">new</span> <span class="pl-c1">BankAccount</span>();</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-c"><span class="pl-c">//</span> Buy shoes...</span></span>
<span class="pl-s1"><span class="pl-smi">$bankAccount</span><span class="pl-k">-&gt;</span>withdrawBalance(<span class="pl-smi">$shoesPrice</span>);</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-c"><span class="pl-c">//</span> Get balance</span></span>
<span class="pl-s1"><span class="pl-smi">$balance</span> <span class="pl-k">=</span> <span class="pl-smi">$bankAccount</span><span class="pl-k">-&gt;</span>getBalance();</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#make-objects-have-privateprotected-members" aria-hidden="true" class="anchor" id="user-content-make-objects-have-privateprotected-members"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Make objects have private/protected members</h3>
<ul>
<li><code>public</code> methods and properties are most dangerous for changes, because some outside code may easily rely on them and you can't control what code relies on them. <strong>Modifications in class are dangerous for all users of class.</strong></li>
<li><code>protected</code> modifier are as dangerous as public, because they are available in scope of any child class. This effectively means that difference between public and protected is only in access mechanism, but encapsulation guarantee remains the same. <strong>Modifications in class are dangerous for all descendant classes.</strong></li>
<li><code>private</code> modifier guarantees that code is <strong>dangerous to modify only in boundaries of single class</strong> (you are safe for modifications and you won't have <a href="http://www.urbandictionary.com/define.php?term=Jengaphobia&amp;defid=2494196">Jenga effect</a>).</li>
</ul>
<p>Therefore, use <code>private</code> by default and <code>public/protected</code> when you need to provide access for external classes.</p>
<p>For more informations you can read the <a href="http://fabien.potencier.org/pragmatism-over-theory-protected-vs-private.html">blog post</a> on this topic written by <a href="https://github.com/fabpot">Fabien Potencier</a>.</p>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Employee</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-smi">$name</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-c1">__construct</span>(<span class="pl-c1">string</span> <span class="pl-smi">$name</span>)</span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">name</span> <span class="pl-k">=</span> <span class="pl-smi">$name</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-smi">$employee</span> <span class="pl-k">=</span> <span class="pl-k">new</span> <span class="pl-c1">Employee</span>(<span class="pl-s"><span class="pl-pds">'</span>John Doe<span class="pl-pds">'</span></span>);</span>
<span class="pl-s1"><span class="pl-c1">echo</span> <span class="pl-s"><span class="pl-pds">'</span>Employee name: <span class="pl-pds">'</span></span><span class="pl-k">.</span><span class="pl-smi">$employee</span><span class="pl-k">-&gt;</span><span class="pl-smi">name</span>; <span class="pl-c"><span class="pl-c">//</span> Employee name: John Doe</span></span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Employee</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$name</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-c1">__construct</span>(<span class="pl-c1">string</span> <span class="pl-smi">$name</span>)</span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">name</span> <span class="pl-k">=</span> <span class="pl-smi">$name</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">getName</span>(): <span class="pl-k">string</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-k">return</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">name</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-smi">$employee</span> <span class="pl-k">=</span> <span class="pl-k">new</span> <span class="pl-c1">Employee</span>(<span class="pl-s"><span class="pl-pds">'</span>John Doe<span class="pl-pds">'</span></span>);</span>
<span class="pl-s1"><span class="pl-c1">echo</span> <span class="pl-s"><span class="pl-pds">'</span>Employee name: <span class="pl-pds">'</span></span><span class="pl-k">.</span><span class="pl-smi">$employee</span><span class="pl-k">-&gt;</span>getName(); <span class="pl-c"><span class="pl-c">//</span> Employee name: John Doe</span></span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h2><a href="#classes" aria-hidden="true" class="anchor" id="user-content-classes"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Classes</h2>
<h3><a href="#prefer-composition-over-inheritance" aria-hidden="true" class="anchor" id="user-content-prefer-composition-over-inheritance"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Prefer composition over inheritance</h3>
<p>As stated famously in <a href="https://en.wikipedia.org/wiki/Design_Patterns"><em>Design Patterns</em></a> by the Gang of Four,
you should prefer composition over inheritance where you can. There are lots of
good reasons to use inheritance and lots of good reasons to use composition.
The main point for this maxim is that if your mind instinctively goes for
inheritance, try to think if composition could model your problem better. In some
cases it can.</p>
<p>You might be wondering then, "when should I use inheritance?" It
depends on your problem at hand, but this is a decent list of when inheritance
makes more sense than composition:</p>
<ol>
<li>Your inheritance represents an "is-a" relationship and not a "has-a"
relationship (Human-&gt;Animal vs. User-&gt;UserDetails).</li>
<li>You can reuse code from the base classes (Humans can move like all animals).</li>
<li>You want to make global changes to derived classes by changing a base class.
(Change the caloric expenditure of all animals when they move).</li>
</ol>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Employee</span> </span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$name</span>;</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$email</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-c1">__construct</span>(<span class="pl-c1">string</span> <span class="pl-smi">$name</span>, <span class="pl-c1">string</span> <span class="pl-smi">$email</span>)</span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">name</span> <span class="pl-k">=</span> <span class="pl-smi">$name</span>;</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">email</span> <span class="pl-k">=</span> <span class="pl-smi">$email</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-c"><span class="pl-c">//</span> Bad because Employees "have" tax data. </span></span>
<span class="pl-s1"><span class="pl-c"><span class="pl-c">//</span> EmployeeTaxData is not a type of Employee</span></span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">EmployeeTaxData</span> <span class="pl-k">extends</span> <span class="pl-e">Employee</span> </span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$ssn</span>;</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$salary</span>;</span>
<span class="pl-s1">    </span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-c1">__construct</span>(<span class="pl-c1">string</span> <span class="pl-smi">$name</span>, <span class="pl-c1">string</span> <span class="pl-smi">$email</span>, <span class="pl-c1">string</span> <span class="pl-smi">$ssn</span>, <span class="pl-c1">string</span> <span class="pl-smi">$salary</span>)</span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-k">parent</span><span class="pl-k">::</span>__construct(<span class="pl-smi">$name</span>, <span class="pl-smi">$email</span>);</span>
<span class="pl-s1"></span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">ssn</span> <span class="pl-k">=</span> <span class="pl-smi">$ssn</span>;</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">salary</span> <span class="pl-k">=</span> <span class="pl-smi">$salary</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">}</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">EmployeeTaxData</span> </span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$ssn</span>;</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$salary</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-c1">__construct</span>(<span class="pl-c1">string</span> <span class="pl-smi">$ssn</span>, <span class="pl-c1">string</span> <span class="pl-smi">$salary</span>)</span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">ssn</span> <span class="pl-k">=</span> <span class="pl-smi">$ssn</span>;</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">salary</span> <span class="pl-k">=</span> <span class="pl-smi">$salary</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Employee</span> </span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$name</span>;</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$email</span>;</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$taxData</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-c1">__construct</span>(<span class="pl-c1">string</span> <span class="pl-smi">$name</span>, <span class="pl-c1">string</span> <span class="pl-smi">$email</span>)</span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">name</span> <span class="pl-k">=</span> <span class="pl-smi">$name</span>;</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">email</span> <span class="pl-k">=</span> <span class="pl-smi">$email</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">setTaxData</span>(<span class="pl-c1">string</span> <span class="pl-smi">$ssn</span>, <span class="pl-c1">string</span> <span class="pl-smi">$salary</span>)</span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">taxData</span> <span class="pl-k">=</span> <span class="pl-k">new</span> <span class="pl-c1">EmployeeTaxData</span>(<span class="pl-smi">$ssn</span>, <span class="pl-smi">$salary</span>);</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">}</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#avoid-fluent-interfaces" aria-hidden="true" class="anchor" id="user-content-avoid-fluent-interfaces"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Avoid fluent interfaces</h3>
<p>A <a href="https://en.wikipedia.org/wiki/Fluent_interface">Fluent interface</a> is an object
oriented API that aims to improve the readability of the source code by using
<a href="https://en.wikipedia.org/wiki/Method_chaining">Method chaining</a>.</p>
<p>While there can be some contexts, frequently builder objects, where this
pattern reduces the verbosity of the code (for example the <a href="https://phpunit.de/manual/current/en/test-doubles.html">PHPUnit Mock Builder</a>
or the <a href="http://docs.doctrine-project.org/projects/doctrine-dbal/en/latest/reference/query-builder.html">Doctrine Query Builder</a>),
more often it comes at some costs:</p>
<ol>
<li>Breaks <a href="https://en.wikipedia.org/wiki/Encapsulation_%28object-oriented_programming%29">Encapsulation</a></li>
<li>Breaks <a href="https://en.wikipedia.org/wiki/Decorator_pattern">Decorators</a></li>
<li>Is harder to <a href="https://en.wikipedia.org/wiki/Mock_object">mock</a> in a test suite</li>
<li>Makes diffs of commits harder to read</li>
</ol>
<p>For more informations you can read the full <a href="https://ocramius.github.io/blog/fluent-interfaces-are-evil/">blog post</a>
on this topic written by <a href="https://github.com/Ocramius">Marco Pivetta</a>.</p>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Car</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$make</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>Honda<span class="pl-pds">'</span></span>;</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$model</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>Accord<span class="pl-pds">'</span></span>;</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$color</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>white<span class="pl-pds">'</span></span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">setMake</span>(<span class="pl-c1">string</span> <span class="pl-smi">$make</span>): <span class="pl-k">self</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">make</span> <span class="pl-k">=</span> <span class="pl-smi">$make</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span> NOTE: Returning this for chaining</span></span>
<span class="pl-s1">        <span class="pl-k">return</span> <span class="pl-smi">$this</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">setModel</span>(<span class="pl-c1">string</span> <span class="pl-smi">$model</span>): <span class="pl-k">self</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">model</span> <span class="pl-k">=</span> <span class="pl-smi">$model</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span> NOTE: Returning this for chaining</span></span>
<span class="pl-s1">        <span class="pl-k">return</span> <span class="pl-smi">$this</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">setColor</span>(<span class="pl-c1">string</span> <span class="pl-smi">$color</span>): <span class="pl-k">self</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">color</span> <span class="pl-k">=</span> <span class="pl-smi">$color</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span> NOTE: Returning this for chaining</span></span>
<span class="pl-s1">        <span class="pl-k">return</span> <span class="pl-smi">$this</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">dump</span>(): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-c1">var_dump</span>(<span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">make</span>, <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">model</span>, <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">color</span>);</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-smi">$car</span> <span class="pl-k">=</span> (<span class="pl-k">new</span> <span class="pl-c1">Car</span>())</span>
<span class="pl-s1">  <span class="pl-k">-&gt;</span>setColor(<span class="pl-s"><span class="pl-pds">'</span>pink<span class="pl-pds">'</span></span>)</span>
<span class="pl-s1">  <span class="pl-k">-&gt;</span>setMake(<span class="pl-s"><span class="pl-pds">'</span>Ford<span class="pl-pds">'</span></span>)</span>
<span class="pl-s1">  <span class="pl-k">-&gt;</span>setModel(<span class="pl-s"><span class="pl-pds">'</span>F-150<span class="pl-pds">'</span></span>)</span>
<span class="pl-s1">  <span class="pl-k">-&gt;</span>dump();</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Car</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$make</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>Honda<span class="pl-pds">'</span></span>;</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$model</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>Accord<span class="pl-pds">'</span></span>;</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$color</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>white<span class="pl-pds">'</span></span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">setMake</span>(<span class="pl-c1">string</span> <span class="pl-smi">$make</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">make</span> <span class="pl-k">=</span> <span class="pl-smi">$make</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">setModel</span>(<span class="pl-c1">string</span> <span class="pl-smi">$model</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">model</span> <span class="pl-k">=</span> <span class="pl-smi">$model</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">setColor</span>(<span class="pl-c1">string</span> <span class="pl-smi">$color</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">color</span> <span class="pl-k">=</span> <span class="pl-smi">$color</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">dump</span>(): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-c1">var_dump</span>(<span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">make</span>, <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">model</span>, <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">color</span>);</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-smi">$car</span> <span class="pl-k">=</span> <span class="pl-k">new</span> <span class="pl-c1">Car</span>();</span>
<span class="pl-s1"><span class="pl-smi">$car</span><span class="pl-k">-&gt;</span>setColor(<span class="pl-s"><span class="pl-pds">'</span>pink<span class="pl-pds">'</span></span>);</span>
<span class="pl-s1"><span class="pl-smi">$car</span><span class="pl-k">-&gt;</span>setMake(<span class="pl-s"><span class="pl-pds">'</span>Ford<span class="pl-pds">'</span></span>);</span>
<span class="pl-s1"><span class="pl-smi">$car</span><span class="pl-k">-&gt;</span>setModel(<span class="pl-s"><span class="pl-pds">'</span>F-150<span class="pl-pds">'</span></span>);</span>
<span class="pl-s1"><span class="pl-smi">$car</span><span class="pl-k">-&gt;</span>dump();</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h2><a href="#solid" aria-hidden="true" class="anchor" id="user-content-solid"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>SOLID</h2>
<p><strong>SOLID</strong> is the mnemonic acronym introduced by Michael Feathers for the first five principles named by Robert Martin, which meant five basic principles of object-oriented programming and design.</p>
<ul>
<li><a href="#single-responsibility-principle-srp">S: Single Responsibility Principle (SRP)</a></li>
<li><a href="#openclosed-principle-ocp">O: Open/Closed Principle (OCP)</a></li>
<li><a href="#liskov-substitution-principle-lsp">L: Liskov Substitution Principle (LSP)</a></li>
<li><a href="#interface-segregation-principle-isp">I: Interface Segregation Principle (ISP)</a></li>
<li><a href="#dependency-inversion-principle-dip">D: Dependency Inversion Principle (DIP)</a></li>
</ul>
<h3><a href="#single-responsibility-principle-srp" aria-hidden="true" class="anchor" id="user-content-single-responsibility-principle-srp"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Single Responsibility Principle (SRP)</h3>
<p>As stated in Clean Code, "There should never be more than one reason for a class
to change". It's tempting to jam-pack a class with a lot of functionality, like
when you can only take one suitcase on your flight. The issue with this is
that your class won't be conceptually cohesive and it will give it many reasons
to change. Minimizing the amount of times you need to change a class is important.
It's important because if too much functionality is in one class and you modify a piece of it,
it can be difficult to understand how that will affect other dependent modules in
your codebase.</p>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">UserSettings</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$user</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-c1">__construct</span>(<span class="pl-c1">User</span> <span class="pl-smi">$user</span>)</span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">user</span> <span class="pl-k">=</span> <span class="pl-smi">$user</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">changeSettings</span>(<span class="pl-k">array</span> <span class="pl-smi">$settings</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-k">if</span> (<span class="pl-smi">$this</span><span class="pl-k">-&gt;</span>verifyCredentials()) {</span>
<span class="pl-s1">            <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">        }</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-k">function</span> <span class="pl-en">verifyCredentials</span>(): <span class="pl-k">bool</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">UserAuth</span> </span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$user</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-c1">__construct</span>(<span class="pl-c1">User</span> <span class="pl-smi">$user</span>)</span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">user</span> <span class="pl-k">=</span> <span class="pl-smi">$user</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">    </span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">verifyCredentials</span>(): <span class="pl-k">bool</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">UserSettings</span> </span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$user</span>;</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$auth</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-c1">__construct</span>(<span class="pl-c1">User</span> <span class="pl-smi">$user</span>) </span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">user</span> <span class="pl-k">=</span> <span class="pl-smi">$user</span>;</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">auth</span> <span class="pl-k">=</span> <span class="pl-k">new</span> <span class="pl-c1">UserAuth</span>(<span class="pl-smi">$user</span>);</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">changeSettings</span>(<span class="pl-k">array</span> <span class="pl-smi">$settings</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-k">if</span> (<span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">auth</span><span class="pl-k">-&gt;</span>verifyCredentials()) {</span>
<span class="pl-s1">            <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">        }</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#openclosed-principle-ocp" aria-hidden="true" class="anchor" id="user-content-openclosed-principle-ocp"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Open/Closed Principle (OCP)</h3>
<p>As stated by Bertrand Meyer, "software entities (classes, modules, functions,
etc.) should be open for extension, but closed for modification." What does that
mean though? This principle basically states that you should allow users to
add new functionalities without changing existing code.</p>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">abstract</span> <span class="pl-k">class</span> <span class="pl-en">Adapter</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">protected</span> <span class="pl-smi">$name</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">getName</span>(): <span class="pl-k">string</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-k">return</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">name</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">AjaxAdapter</span> <span class="pl-k">extends</span> <span class="pl-e">Adapter</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-c1">__construct</span>()</span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-k">parent</span><span class="pl-k">::</span>__construct();</span>
<span class="pl-s1"></span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">name</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>ajaxAdapter<span class="pl-pds">'</span></span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">NodeAdapter</span> <span class="pl-k">extends</span> <span class="pl-e">Adapter</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-c1">__construct</span>()</span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-k">parent</span><span class="pl-k">::</span>__construct();</span>
<span class="pl-s1"></span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">name</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>nodeAdapter<span class="pl-pds">'</span></span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">HttpRequester</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$adapter</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-c1">__construct</span>(<span class="pl-c1">Adapter</span> <span class="pl-smi">$adapter</span>)</span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">adapter</span> <span class="pl-k">=</span> <span class="pl-smi">$adapter</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">fetch</span>(<span class="pl-c1">string</span> <span class="pl-smi">$url</span>): <span class="pl-c1">Promise</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$adapterName</span> <span class="pl-k">=</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">adapter</span><span class="pl-k">-&gt;</span>getName();</span>
<span class="pl-s1"></span>
<span class="pl-s1">        <span class="pl-k">if</span> (<span class="pl-smi">$adapterName</span> <span class="pl-k">===</span> <span class="pl-s"><span class="pl-pds">'</span>ajaxAdapter<span class="pl-pds">'</span></span>) {</span>
<span class="pl-s1">            <span class="pl-k">return</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span>makeAjaxCall(<span class="pl-smi">$url</span>);</span>
<span class="pl-s1">        } <span class="pl-k">elseif</span> (<span class="pl-smi">$adapterName</span> <span class="pl-k">===</span> <span class="pl-s"><span class="pl-pds">'</span>httpNodeAdapter<span class="pl-pds">'</span></span>) {</span>
<span class="pl-s1">            <span class="pl-k">return</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span>makeHttpCall(<span class="pl-smi">$url</span>);</span>
<span class="pl-s1">        }</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-k">function</span> <span class="pl-en">makeAjaxCall</span>(<span class="pl-c1">string</span> <span class="pl-smi">$url</span>): <span class="pl-c1">Promise</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span> request and return promise</span></span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-k">function</span> <span class="pl-en">makeHttpCall</span>(<span class="pl-c1">string</span> <span class="pl-smi">$url</span>): <span class="pl-c1">Promise</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span> request and return promise</span></span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">interface</span> <span class="pl-en">Adapter</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">request</span>(<span class="pl-c1">string</span> <span class="pl-smi">$url</span>): <span class="pl-c1">Promise</span>;</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">AjaxAdapter</span> <span class="pl-k">implements</span> <span class="pl-e">Adapter</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">request</span>(<span class="pl-c1">string</span> <span class="pl-smi">$url</span>): <span class="pl-c1">Promise</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span> request and return promise</span></span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">NodeAdapter</span> <span class="pl-k">implements</span> <span class="pl-e">Adapter</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">request</span>(<span class="pl-c1">string</span> <span class="pl-smi">$url</span>): <span class="pl-c1">Promise</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span> request and return promise</span></span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">HttpRequester</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$adapter</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-c1">__construct</span>(<span class="pl-c1">Adapter</span> <span class="pl-smi">$adapter</span>)</span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">adapter</span> <span class="pl-k">=</span> <span class="pl-smi">$adapter</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">fetch</span>(<span class="pl-c1">string</span> <span class="pl-smi">$url</span>): <span class="pl-c1">Promise</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-k">return</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">adapter</span><span class="pl-k">-&gt;</span>request(<span class="pl-smi">$url</span>);</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#liskov-substitution-principle-lsp" aria-hidden="true" class="anchor" id="user-content-liskov-substitution-principle-lsp"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Liskov Substitution Principle (LSP)</h3>
<p>This is a scary term for a very simple concept. It's formally defined as "If S
is a subtype of T, then objects of type T may be replaced with objects of type S
(i.e., objects of type S may substitute objects of type T) without altering any
of the desirable properties of that program (correctness, task performed,
etc.)." That's an even scarier definition.</p>
<p>The best explanation for this is if you have a parent class and a child class,
then the base class and child class can be used interchangeably without getting
incorrect results. This might still be confusing, so let's take a look at the
classic Square-Rectangle example. Mathematically, a square is a rectangle, but
if you model it using the "is-a" relationship via inheritance, you quickly
get into trouble.</p>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Rectangle</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">protected</span> <span class="pl-smi">$width</span> <span class="pl-k">=</span> <span class="pl-c1">0</span>;</span>
<span class="pl-s1">    <span class="pl-k">protected</span> <span class="pl-smi">$height</span> <span class="pl-k">=</span> <span class="pl-c1">0</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">render</span>(<span class="pl-c1">int</span> <span class="pl-smi">$area</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">setWidth</span>(<span class="pl-c1">int</span> <span class="pl-smi">$width</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">width</span> <span class="pl-k">=</span> <span class="pl-smi">$width</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">setHeight</span>(<span class="pl-c1">int</span> <span class="pl-smi">$height</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">height</span> <span class="pl-k">=</span> <span class="pl-smi">$height</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">getArea</span>(): <span class="pl-k">int</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-k">return</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">width</span> <span class="pl-k">*</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">height</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Square</span> <span class="pl-k">extends</span> <span class="pl-e">Rectangle</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">setWidth</span>(<span class="pl-c1">int</span> <span class="pl-smi">$width</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">width</span> <span class="pl-k">=</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">height</span> <span class="pl-k">=</span> <span class="pl-smi">$width</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">setHeight</span>(<span class="pl-c1">int</span> <span class="pl-smi">$height</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">width</span> <span class="pl-k">=</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">height</span> <span class="pl-k">=</span> <span class="pl-smi">$height</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-c"><span class="pl-c">/**</span></span></span>
<span class="pl-s1"><span class="pl-c"> * <span class="pl-k">@param</span> Rectangle[] $rectangles</span></span>
<span class="pl-s1"><span class="pl-c"> <span class="pl-c">*/</span></span></span>
<span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">renderLargeRectangles</span>(<span class="pl-k">array</span> <span class="pl-smi">$rectangles</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">foreach</span> (<span class="pl-smi">$rectangles</span> <span class="pl-k">as</span> <span class="pl-smi">$rectangle</span>) {</span>
<span class="pl-s1">        <span class="pl-smi">$rectangle</span><span class="pl-k">-&gt;</span>setWidth(<span class="pl-c1">4</span>);</span>
<span class="pl-s1">        <span class="pl-smi">$rectangle</span><span class="pl-k">-&gt;</span>setHeight(<span class="pl-c1">5</span>);</span>
<span class="pl-s1">        <span class="pl-smi">$area</span> <span class="pl-k">=</span> <span class="pl-smi">$rectangle</span><span class="pl-k">-&gt;</span>getArea(); <span class="pl-c"><span class="pl-c">//</span> BAD: Will return 25 for Square. Should be 20.</span></span>
<span class="pl-s1">        <span class="pl-smi">$rectangle</span><span class="pl-k">-&gt;</span>render(<span class="pl-smi">$area</span>);</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-smi">$rectangles</span> <span class="pl-k">=</span> [<span class="pl-k">new</span> <span class="pl-c1">Rectangle</span>(), <span class="pl-k">new</span> <span class="pl-c1">Rectangle</span>(), <span class="pl-k">new</span> <span class="pl-c1">Square</span>()];</span>
<span class="pl-s1">renderLargeRectangles(<span class="pl-smi">$rectangles</span>);</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">abstract</span> <span class="pl-k">class</span> <span class="pl-en">Shape</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">protected</span> <span class="pl-smi">$width</span> <span class="pl-k">=</span> <span class="pl-c1">0</span>;</span>
<span class="pl-s1">    <span class="pl-k">protected</span> <span class="pl-smi">$height</span> <span class="pl-k">=</span> <span class="pl-c1">0</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">abstract</span> <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">getArea</span>(): <span class="pl-k">int</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">render</span>(<span class="pl-c1">int</span> <span class="pl-smi">$area</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span> ...</span></span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Rectangle</span> <span class="pl-k">extends</span> <span class="pl-e">Shape</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">setWidth</span>(<span class="pl-c1">int</span> <span class="pl-smi">$width</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">width</span> <span class="pl-k">=</span> <span class="pl-smi">$width</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">setHeight</span>(<span class="pl-c1">int</span> <span class="pl-smi">$height</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">height</span> <span class="pl-k">=</span> <span class="pl-smi">$height</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">getArea</span>(): <span class="pl-k">int</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-k">return</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">width</span> <span class="pl-k">*</span> <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">height</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Square</span> <span class="pl-k">extends</span> <span class="pl-e">Shape</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$length</span> <span class="pl-k">=</span> <span class="pl-c1">0</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">setLength</span>(<span class="pl-c1">int</span> <span class="pl-smi">$length</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">length</span> <span class="pl-k">=</span> <span class="pl-smi">$length</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">getArea</span>(): <span class="pl-k">int</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-k">return</span> <span class="pl-c1">pow</span>(<span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">length</span>, <span class="pl-c1">2</span>);</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-c"><span class="pl-c">/**</span></span></span>
<span class="pl-s1"><span class="pl-c"> * <span class="pl-k">@param</span> Rectangle[] $rectangles</span></span>
<span class="pl-s1"><span class="pl-c"> <span class="pl-c">*/</span></span></span>
<span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">renderLargeRectangles</span>(<span class="pl-k">array</span> <span class="pl-smi">$rectangles</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">foreach</span> (<span class="pl-smi">$rectangles</span> <span class="pl-k">as</span> <span class="pl-smi">$rectangle</span>) {</span>
<span class="pl-s1">        <span class="pl-k">if</span> (<span class="pl-smi">$rectangle</span> <span class="pl-k">instanceof</span> <span class="pl-c1">Square</span>) {</span>
<span class="pl-s1">            <span class="pl-smi">$rectangle</span><span class="pl-k">-&gt;</span>setLength(<span class="pl-c1">5</span>);</span>
<span class="pl-s1">        } <span class="pl-k">elseif</span> (<span class="pl-smi">$rectangle</span> <span class="pl-k">instanceof</span> <span class="pl-c1">Rectangle</span>) {</span>
<span class="pl-s1">            <span class="pl-smi">$rectangle</span><span class="pl-k">-&gt;</span>setWidth(<span class="pl-c1">4</span>);</span>
<span class="pl-s1">            <span class="pl-smi">$rectangle</span><span class="pl-k">-&gt;</span>setHeight(<span class="pl-c1">5</span>);</span>
<span class="pl-s1">        }</span>
<span class="pl-s1"></span>
<span class="pl-s1">        <span class="pl-smi">$area</span> <span class="pl-k">=</span> <span class="pl-smi">$rectangle</span><span class="pl-k">-&gt;</span>getArea(); </span>
<span class="pl-s1">        <span class="pl-smi">$rectangle</span><span class="pl-k">-&gt;</span>render(<span class="pl-smi">$area</span>);</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-smi">$shapes</span> <span class="pl-k">=</span> [<span class="pl-k">new</span> <span class="pl-c1">Rectangle</span>(), <span class="pl-k">new</span> <span class="pl-c1">Rectangle</span>(), <span class="pl-k">new</span> <span class="pl-c1">Square</span>()];</span>
<span class="pl-s1">renderLargeRectangles(<span class="pl-smi">$shapes</span>);</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#interface-segregation-principle-isp" aria-hidden="true" class="anchor" id="user-content-interface-segregation-principle-isp"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Interface Segregation Principle (ISP)</h3>
<p>ISP states that "Clients should not be forced to depend upon interfaces that
they do not use."</p>
<p>A good example to look at that demonstrates this principle is for
classes that require large settings objects. Not requiring clients to setup
huge amounts of options is beneficial, because most of the time they won't need
all of the settings. Making them optional helps prevent having a "fat interface".</p>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">interface</span> <span class="pl-en">Employee</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">work</span>(): <span class="pl-c1">void</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">eat</span>(): <span class="pl-c1">void</span>;</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Human</span> <span class="pl-k">implements</span> <span class="pl-e">Employee</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">work</span>(): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span> ....working</span></span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">eat</span>(): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span> ...... eating in lunch break</span></span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Robot</span> <span class="pl-k">implements</span> <span class="pl-e">Employee</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">work</span>(): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span>.... working much more</span></span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">eat</span>(): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span>.... robot can't eat, but it must implement this method</span></span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span></pre></div>
<p><strong>Good:</strong></p>
<p>Not every worker is an employee, but every employee is a worker.</p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">interface</span> <span class="pl-en">Workable</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">work</span>(): <span class="pl-c1">void</span>;</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">interface</span> <span class="pl-en">Feedable</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">eat</span>(): <span class="pl-c1">void</span>;</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">interface</span> <span class="pl-en">Employee</span> <span class="pl-k">extends</span> <span class="pl-e">Feedable</span>, <span class="pl-e">Workable</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Human</span> <span class="pl-k">implements</span> <span class="pl-e">Employee</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">work</span>(): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span> ....working</span></span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">eat</span>(): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span>.... eating in lunch break</span></span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-c"><span class="pl-c">//</span> robot can only work</span></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Robot</span> <span class="pl-k">implements</span> <span class="pl-e">Workable</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">work</span>(): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span> ....working</span></span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h3><a href="#dependency-inversion-principle-dip" aria-hidden="true" class="anchor" id="user-content-dependency-inversion-principle-dip"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Dependency Inversion Principle (DIP)</h3>
<p>This principle states two essential things:</p>
<ol>
<li>High-level modules should not depend on low-level modules. Both should
depend on abstractions.</li>
<li>Abstractions should not depend upon details. Details should depend on
abstractions.</li>
</ol>
<p>This can be hard to understand at first, but if you've worked with PHP frameworks (like Symfony), you've seen an implementation of this principle in the form of Dependency
Injection (DI). While they are not identical concepts, DIP keeps high-level
modules from knowing the details of its low-level modules and setting them up.
It can accomplish this through DI. A huge benefit of this is that it reduces
the coupling between modules. Coupling is a very bad development pattern because
it makes your code hard to refactor.</p>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Employee</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">work</span>(): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span> ....working</span></span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Robot</span> <span class="pl-k">extends</span> <span class="pl-e">Employee</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">work</span>(): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span>.... working much more</span></span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Manager</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$employee</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-c1">__construct</span>(<span class="pl-c1">Employee</span> <span class="pl-smi">$employee</span>)</span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">employee</span> <span class="pl-k">=</span> <span class="pl-smi">$employee</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">manage</span>(): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">employee</span><span class="pl-k">-&gt;</span>work();</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">interface</span> <span class="pl-en">Employee</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">work</span>(): <span class="pl-c1">void</span>;</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Human</span> <span class="pl-k">implements</span> <span class="pl-e">Employee</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">work</span>(): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span> ....working</span></span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Robot</span> <span class="pl-k">implements</span> <span class="pl-e">Employee</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">work</span>(): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-c"><span class="pl-c">//</span>.... working much more</span></span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">class</span> <span class="pl-en">Manager</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">private</span> <span class="pl-smi">$employee</span>;</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-c1">__construct</span>(<span class="pl-c1">Employee</span> <span class="pl-smi">$employee</span>)</span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">employee</span> <span class="pl-k">=</span> <span class="pl-smi">$employee</span>;</span>
<span class="pl-s1">    }</span>
<span class="pl-s1"></span>
<span class="pl-s1">    <span class="pl-k">public</span> <span class="pl-k">function</span> <span class="pl-en">manage</span>(): <span class="pl-c1">void</span></span>
<span class="pl-s1">    {</span>
<span class="pl-s1">        <span class="pl-smi">$this</span><span class="pl-k">-&gt;</span><span class="pl-smi">employee</span><span class="pl-k">-&gt;</span>work();</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h2><a href="#dont-repeat-yourself-dry" aria-hidden="true" class="anchor" id="user-content-dont-repeat-yourself-dry"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Don’t repeat yourself (DRY)</h2>
<p>Try to observe the <a href="https://en.wikipedia.org/wiki/Don%27t_repeat_yourself">DRY</a> principle.</p>
<p>Do your absolute best to avoid duplicate code. Duplicate code is bad because
it means that there's more than one place to alter something if you need to
change some logic.</p>
<p>Imagine if you run a restaurant and you keep track of your inventory: all your
tomatoes, onions, garlic, spices, etc. If you have multiple lists that
you keep this on, then all have to be updated when you serve a dish with
tomatoes in them. If you only have one list, there's only one place to update!</p>
<p>Oftentimes you have duplicate code because you have two or more slightly
different things, that share a lot in common, but their differences force you
to have two or more separate functions that do much of the same things. Removing
duplicate code means creating an abstraction that can handle this set of different
things with just one function/module/class.</p>
<p>Getting the abstraction right is critical, that's why you should follow the
SOLID principles laid out in the <a href="#classes">Classes</a> section. Bad abstractions can be
worse than duplicate code, so be careful! Having said this, if you can make
a good abstraction, do it! Don't repeat yourself, otherwise you'll find yourself
updating multiple places anytime you want to change one thing.</p>
<p><strong>Bad:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">showDeveloperList</span>(<span class="pl-k">array</span> <span class="pl-smi">$developers</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">foreach</span> (<span class="pl-smi">$developers</span> <span class="pl-k">as</span> <span class="pl-smi">$developer</span>) {</span>
<span class="pl-s1">        <span class="pl-smi">$expectedSalary</span> <span class="pl-k">=</span> <span class="pl-smi">$developer</span><span class="pl-k">-&gt;</span>calculateExpectedSalary();</span>
<span class="pl-s1">        <span class="pl-smi">$experience</span> <span class="pl-k">=</span> <span class="pl-smi">$developer</span><span class="pl-k">-&gt;</span>getExperience();</span>
<span class="pl-s1">        <span class="pl-smi">$githubLink</span> <span class="pl-k">=</span> <span class="pl-smi">$developer</span><span class="pl-k">-&gt;</span>getGithubLink();</span>
<span class="pl-s1">        <span class="pl-smi">$data</span> <span class="pl-k">=</span> [</span>
<span class="pl-s1">            <span class="pl-smi">$expectedSalary</span>,</span>
<span class="pl-s1">            <span class="pl-smi">$experience</span>,</span>
<span class="pl-s1">            <span class="pl-smi">$githubLink</span></span>
<span class="pl-s1">        ];</span>
<span class="pl-s1"></span>
<span class="pl-s1">        render(<span class="pl-smi">$data</span>);</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span>
<span class="pl-s1"></span>
<span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">showManagerList</span>(<span class="pl-k">array</span> <span class="pl-smi">$managers</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">foreach</span> (<span class="pl-smi">$managers</span> <span class="pl-k">as</span> <span class="pl-smi">$manager</span>) {</span>
<span class="pl-s1">        <span class="pl-smi">$expectedSalary</span> <span class="pl-k">=</span> <span class="pl-smi">$manager</span><span class="pl-k">-&gt;</span>calculateExpectedSalary();</span>
<span class="pl-s1">        <span class="pl-smi">$experience</span> <span class="pl-k">=</span> <span class="pl-smi">$manager</span><span class="pl-k">-&gt;</span>getExperience();</span>
<span class="pl-s1">        <span class="pl-smi">$githubLink</span> <span class="pl-k">=</span> <span class="pl-smi">$manager</span><span class="pl-k">-&gt;</span>getGithubLink();</span>
<span class="pl-s1">        <span class="pl-smi">$data</span> <span class="pl-k">=</span> [</span>
<span class="pl-s1">            <span class="pl-smi">$expectedSalary</span>,</span>
<span class="pl-s1">            <span class="pl-smi">$experience</span>,</span>
<span class="pl-s1">            <span class="pl-smi">$githubLink</span></span>
<span class="pl-s1">        ];</span>
<span class="pl-s1"></span>
<span class="pl-s1">        render(<span class="pl-smi">$data</span>);</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span></pre></div>
<p><strong>Good:</strong></p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">showList</span>(<span class="pl-k">array</span> <span class="pl-smi">$employees</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">foreach</span> (<span class="pl-smi">$employees</span> <span class="pl-k">as</span> <span class="pl-smi">$employee</span>) {</span>
<span class="pl-s1">        <span class="pl-smi">$expectedSalary</span> <span class="pl-k">=</span> <span class="pl-smi">$employee</span><span class="pl-k">-&gt;</span>calculateExpectedSalary();</span>
<span class="pl-s1">        <span class="pl-smi">$experience</span> <span class="pl-k">=</span> <span class="pl-smi">$employee</span><span class="pl-k">-&gt;</span>getExperience();</span>
<span class="pl-s1">        <span class="pl-smi">$githubLink</span> <span class="pl-k">=</span> <span class="pl-smi">$employee</span><span class="pl-k">-&gt;</span>getGithubLink();</span>
<span class="pl-s1">        <span class="pl-smi">$data</span> <span class="pl-k">=</span> [</span>
<span class="pl-s1">            <span class="pl-smi">$expectedSalary</span>,</span>
<span class="pl-s1">            <span class="pl-smi">$experience</span>,</span>
<span class="pl-s1">            <span class="pl-smi">$githubLink</span></span>
<span class="pl-s1">        ];</span>
<span class="pl-s1"></span>
<span class="pl-s1">        render(<span class="pl-smi">$data</span>);</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span></pre></div>
<p><strong>Very good:</strong></p>
<p>It is better to use a compact version of the code.</p>
<div class="highlight highlight-text-html-php"><pre><span class="pl-s1"><span class="pl-k">function</span> <span class="pl-en">showList</span>(<span class="pl-k">array</span> <span class="pl-smi">$employees</span>): <span class="pl-c1">void</span></span>
<span class="pl-s1">{</span>
<span class="pl-s1">    <span class="pl-k">foreach</span> (<span class="pl-smi">$employees</span> <span class="pl-k">as</span> <span class="pl-smi">$employee</span>) {</span>
<span class="pl-s1">        render([</span>
<span class="pl-s1">            <span class="pl-smi">$employee</span><span class="pl-k">-&gt;</span>calculateExpectedSalary(),</span>
<span class="pl-s1">            <span class="pl-smi">$employee</span><span class="pl-k">-&gt;</span>getExperience(),</span>
<span class="pl-s1">            <span class="pl-smi">$employee</span><span class="pl-k">-&gt;</span>getGithubLink()</span>
<span class="pl-s1">        ]);</span>
<span class="pl-s1">    }</span>
<span class="pl-s1">}</span></pre></div>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
<h2><a href="#translations" aria-hidden="true" class="anchor" id="user-content-translations"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Translations</h2>
<p>This is also available in other languages:</p>
<ul>
<li><g-emoji alias="cn" fallback-src="https://assets-cdn.github.com/images/icons/emoji/unicode/1f1e8-1f1f3.png" ios-version="6.0">🇨🇳</g-emoji> <strong>Chinese:</strong>
<ul>
<li><a href="https://github.com/php-cpm/clean-code-php">php-cpm/clean-code-php</a></li>
</ul>
</li>
<li><g-emoji alias="ru" fallback-src="https://assets-cdn.github.com/images/icons/emoji/unicode/1f1f7-1f1fa.png" ios-version="6.0">🇷🇺</g-emoji> <strong>Russian:</strong>
<ul>
<li><a href="https://github.com/peter-gribanov/clean-code-php">peter-gribanov/clean-code-php</a></li>
</ul>
</li>
<li><g-emoji alias="es" fallback-src="https://assets-cdn.github.com/images/icons/emoji/unicode/1f1ea-1f1f8.png" ios-version="6.0">🇪🇸</g-emoji> <strong>Spanish:</strong>
<ul>
<li><a href="https://github.com/fikoborquez/clean-code-php">fikoborquez/clean-code-php</a></li>
</ul>
</li>
<li><g-emoji alias="brazil" fallback-src="https://assets-cdn.github.com/images/icons/emoji/unicode/1f1e7-1f1f7.png" ios-version="8.3">🇧🇷</g-emoji> <strong>Portuguese:</strong>
<ul>
<li><a href="https://github.com/fabioars/clean-code-php">fabioars/clean-code-php</a></li>
<li><a href="https://github.com/jeanjar/clean-code-php/tree/pt-br">jeanjar/clean-code-php</a></li>
</ul>
</li>
<li><g-emoji alias="thailand" fallback-src="https://assets-cdn.github.com/images/icons/emoji/unicode/1f1f9-1f1ed.png" ios-version="8.3">🇹🇭</g-emoji> <strong>Thai:</strong>
<ul>
<li><a href="https://github.com/panuwizzle/clean-code-php">panuwizzle/clean-code-php</a></li>
</ul>
</li>
</ul>
<p><strong><a href="#table-of-contents">⬆ back to top</a></strong></p>
</article>
