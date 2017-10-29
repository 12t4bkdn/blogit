<h2>NAME</h2>

<p>git-clean - Remove untracked files from the working tree</p>

<h2>SYNOPSIS</h2>

<pre>
<em>git clean</em> [-d] [-f] [-i] [-n] [-q] [-e &lt;pattern&gt;] [-x | -X] [--] &lt;path&gt;&hellip;​</pre>

<h2>DESCRIPTION</h2>

<p>Cleans the working tree by recursively removing files that are not under version control, starting from the current directory.</p>

<p>Normally, only files unknown to Git are removed, but if the&nbsp;<code>-x</code>&nbsp;option is specified, ignored files are also removed. This can, for example, be useful to remove all build products.</p>

<p>If any optional&nbsp;<code>&lt;path&gt;...</code>&nbsp;arguments are given, only those paths are affected.</p>

<h2>OPTIONS</h2>

<p>-d</p>

<p>Remove untracked directories in addition to untracked files. If an untracked directory is managed by a different Git repository, it is not removed by default. Use -f option twice if you really want to remove such a directory.</p>

<p>-f</p>

<p>--force</p>

<p>If the Git configuration variable clean.requireForce is not set to false,&nbsp;<em>git clean</em>&nbsp;will refuse to delete files or directories unless given -f, -n or -i. Git will refuse to delete directories with .git sub directory or file unless a second -f is given.</p>

<p>-i</p>

<p>--interactive</p>

<p>Show what would be done and clean files interactively. See &ldquo;Interactive mode&rdquo; for details.</p>

<p>-n</p>

<p>--dry-run</p>

<p>Don&rsquo;t actually remove anything, just show what would be done.</p>

<p>-q</p>

<p>--quiet</p>

<p>Be quiet, only report errors, but not the files that are successfully removed.</p>

<p>-e &lt;pattern&gt;</p>

<p>--exclude=&lt;pattern&gt;</p>

<p>In addition to those found in .gitignore (per directory) and $GIT_DIR/info/exclude, also consider these patterns to be in the set of the ignore rules in effect.</p>

<p>-x</p>

<p>Don&rsquo;t use the standard ignore rules read from .gitignore (per directory) and $GIT_DIR/info/exclude, but do still use the ignore rules given with&nbsp;<code>-e</code>&nbsp;options. This allows removing all untracked files, including build products. This can be used (possibly in conjunction with&nbsp;<em>git reset</em>) to create a pristine working directory to test a clean build.</p>

<p>-X</p>

<p>Remove only files ignored by Git. This may be useful to rebuild everything from scratch, but keep manually created files.</p>

<h2>Interactive mode</h2>

<p>When the command enters the interactive mode, it shows the files and directories to be cleaned, and goes into its interactive command loop.</p>

<p>The command loop shows the list of subcommands available, and gives a prompt &quot;What now&gt; &quot;. In general, when the prompt ends with a single&nbsp;<em>&gt;</em>, you can pick only one of the choices given and type return, like this:</p>

<pre>
    *** Commands ***
	1: clean                2: filter by pattern    3: select by numbers
	4: ask each             5: quit                 6: help
    What now&gt; 1</pre>

<p>You also could say&nbsp;<code>c</code>&nbsp;or&nbsp;<code>clean</code>&nbsp;above as long as the choice is unique.</p>

<p>The main command loop has 6 subcommands.</p>

<p>clean</p>

<p>Start cleaning files and directories, and then quit.</p>

<p>filter by pattern</p>

<p>This shows the files and directories to be deleted and issues an &quot;Input ignore patterns&gt;&gt;&quot; prompt. You can input space-separated patterns to exclude files and directories from deletion. E.g. &quot;*.c *.h&quot; will excludes files end with &quot;.c&quot; and &quot;.h&quot; from deletion. When you are satisfied with the filtered result, press ENTER (empty) back to the main menu.</p>

<p>select by numbers</p>

<p>This shows the files and directories to be deleted and issues an &quot;Select items to delete&gt;&gt;&quot; prompt. When the prompt ends with double&nbsp;<em>&gt;&gt;</em>&nbsp;like this, you can make more than one selection, concatenated with whitespace or comma. Also you can say ranges. E.g. &quot;2-5 7,9&quot; to choose 2,3,4,5,7,9 from the list. If the second number in a range is omitted, all remaining items are selected. E.g. &quot;7-&quot; to choose 7,8,9 from the list. You can say&nbsp;<em>*</em>&nbsp;to choose everything. Also when you are satisfied with the filtered result, press ENTER (empty) back to the main menu.</p>

<p>ask each</p>

<p>This will start to clean, and you must confirm one by one in order to delete items. Please note that this action is not as efficient as the above two actions.</p>

<p>quit</p>

<p>This lets you quit without do cleaning.</p>

<p>help</p>

<p>Show brief usage of interactive git-clean.</p>
