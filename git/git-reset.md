<h2>NAME</h2>

<p>git-reset - Reset current HEAD to the specified state</p>

<h2>SYNOPSIS</h2>

<pre>
<em>git reset</em> [-q] [&lt;tree-ish&gt;] [--] &lt;paths&gt;&hellip;​
<em>git reset</em> (--patch | -p) [&lt;tree-ish&gt;] [--] [&lt;paths&gt;&hellip;​]
<em>git reset</em> [--soft | --mixed [-N] | --hard | --merge | --keep] [-q] [&lt;commit&gt;]</pre>

<h2>DESCRIPTION</h2>

<p>In the first and second form, copy entries from &lt;tree-ish&gt; to the index. In the third form, set the current branch head (HEAD) to &lt;commit&gt;, optionally modifying index and working tree to match. The &lt;tree-ish&gt;/&lt;commit&gt; defaults to HEAD in all forms.</p>

<p><em>git reset</em>&nbsp;[-q] [&lt;tree-ish&gt;] [--] &lt;paths&gt;&hellip;​</p>

<p>This form resets the index entries for all &lt;paths&gt; to their state at &lt;tree-ish&gt;. (It does not affect the working tree or the current branch.)</p>

<p>This means that&nbsp;<code>git reset &lt;paths&gt;</code>&nbsp;is the opposite of&nbsp;<code>git add &lt;paths&gt;</code>.</p>

<p>After running&nbsp;<code>git reset &lt;paths&gt;</code>&nbsp;to update the index entry, you can use&nbsp;<a href="https://git-scm.com/docs/git-checkout">git-checkout[1]</a>&nbsp;to check the contents out of the index to the working tree. Alternatively, using&nbsp;<a href="https://git-scm.com/docs/git-checkout">git-checkout[1]</a>&nbsp;and specifying a commit, you can copy the contents of a path out of a commit to the index and to the working tree in one go.</p>

<p><em>git reset</em>&nbsp;(--patch | -p) [&lt;tree-ish&gt;] [--] [&lt;paths&gt;&hellip;​]</p>

<p>Interactively select hunks in the difference between the index and &lt;tree-ish&gt; (defaults to HEAD). The chosen hunks are applied in reverse to the index.</p>

<p>This means that&nbsp;<code>git reset -p</code>&nbsp;is the opposite of&nbsp;<code>git add -p</code>, i.e. you can use it to selectively reset hunks. See the &ldquo;Interactive Mode&rdquo; section of&nbsp;<a href="https://git-scm.com/docs/git-add">git-add[1]</a>&nbsp;to learn how to operate the&nbsp;<code>--patch</code>mode.</p>

<p><em>git reset</em>&nbsp;[&lt;mode&gt;] [&lt;commit&gt;]</p>

<p>This form resets the current branch head to &lt;commit&gt; and possibly updates the index (resetting it to the tree of &lt;commit&gt;) and the working tree depending on &lt;mode&gt;. If &lt;mode&gt; is omitted, defaults to &quot;--mixed&quot;. The &lt;mode&gt; must be one of the following:</p>

<p>--soft</p>

<p>Does not touch the index file or the working tree at all (but resets the head to &lt;commit&gt;, just like all modes do). This leaves all your changed files &quot;Changes to be committed&quot;, as&nbsp;<em>git status</em>&nbsp;would put it.</p>

<p>--mixed</p>

<p>Resets the index but not the working tree (i.e., the changed files are preserved but not marked for commit) and reports what has not been updated. This is the default action.</p>

<p>If&nbsp;<code>-N</code>&nbsp;is specified, removed paths are marked as intent-to-add (see&nbsp;<a href="https://git-scm.com/docs/git-add">git-add[1]</a>).</p>

<p>--hard</p>

<p>Resets the index and working tree. Any changes to tracked files in the working tree since &lt;commit&gt; are discarded.</p>

<p>--merge</p>

<p>Resets the index and updates the files in the working tree that are different between &lt;commit&gt; and HEAD, but keeps those which are different between the index and working tree (i.e. which have changes which have not been added). If a file that is different between &lt;commit&gt; and the index has unstaged changes, reset is aborted.</p>

<p>In other words, --merge does something like a&nbsp;<em>git read-tree -u -m &lt;commit&gt;</em>, but carries forward unmerged index entries.</p>

<p>--keep</p>

<p>Resets index entries and updates files in the working tree that are different between &lt;commit&gt; and HEAD. If a file that is different between &lt;commit&gt; and HEAD has local changes, reset is aborted.</p>

<p>If you want to undo a commit other than the latest on a branch,&nbsp;<a href="https://git-scm.com/docs/git-revert">git-revert[1]</a>&nbsp;is your friend.</p>

<h2>OPTIONS</h2>

<p>-q</p>

<p>--quiet</p>

<p>Be quiet, only report errors.</p>

<h2>EXAMPLES</h2>

<p>Undo add</p>

<pre>
$ edit                                     <strong>(1)</strong>
$ git add frotz.c filfre.c
$ mailx                                    <strong>(2)</strong>
$ git reset                                <strong>(3)</strong>
$ git pull git://info.example.com/ nitfol  <strong>(4)</strong></pre>

<ol>
	<li>
	<p>You are happily working on something, and find the changes in these files are in good order. You do not want to see them when you run &quot;git diff&quot;, because you plan to work on other files and changes with these files are distracting.</p>
	</li>
	<li>
	<p>Somebody asks you to pull, and the changes sound worthy of merging.</p>
	</li>
	<li>
	<p>However, you already dirtied the index (i.e. your index does not match the HEAD commit). But you know the pull you are going to make does not affect frotz.c or filfre.c, so you revert the index changes for these two files. Your changes in working tree remain there.</p>
	</li>
	<li>
	<p>Then you can pull and merge, leaving frotz.c and filfre.c changes still in the working tree.</p>
	</li>
</ol>

<p>Undo a commit and redo</p>

<pre>
$ git commit ...
$ git reset --soft HEAD^      <strong>(1)</strong>
$ edit                        <strong>(2)</strong>
$ git commit -a -c ORIG_HEAD  <strong>(3)</strong></pre>

<ol>
	<li>
	<p>This is most often done when you remembered what you just committed is incomplete, or you misspelled your commit message, or both. Leaves working tree as it was before &quot;reset&quot;.</p>
	</li>
	<li>
	<p>Make corrections to working tree files.</p>
	</li>
	<li>
	<p>&quot;reset&quot; copies the old head to .git/ORIG_HEAD; redo the commit by starting with its log message. If you do not need to edit the message further, you can give -C option instead.</p>
	</li>
</ol>

<p>See also the --amend option to&nbsp;<a href="https://git-scm.com/docs/git-commit">git-commit[1]</a>.</p>

<p>Undo a commit, making it a topic branch</p>

<pre>
$ git branch topic/wip     <strong>(1)</strong>
$ git reset --hard HEAD~3  <strong>(2)</strong>
$ git checkout topic/wip   <strong>(3)</strong></pre>

<ol>
	<li>
	<p>You have made some commits, but realize they were premature to be in the &quot;master&quot; branch. You want to continue polishing them in a topic branch, so create &quot;topic/wip&quot; branch off of the current HEAD.</p>
	</li>
	<li>
	<p>Rewind the master branch to get rid of those three commits.</p>
	</li>
	<li>
	<p>Switch to &quot;topic/wip&quot; branch and keep working.</p>
	</li>
</ol>

<p>Undo commits permanently</p>

<pre>
$ git commit ...
$ git reset --hard HEAD~3   <strong>(1)</strong></pre>

<ol>
	<li>
	<p>The last three commits (HEAD, HEAD^, and HEAD~2) were bad and you do not want to ever see them again. Do&nbsp;<strong>not</strong>&nbsp;do this if you have already given these commits to somebody else. (See the &quot;RECOVERING FROM UPSTREAM REBASE&quot; section in&nbsp;<a href="https://git-scm.com/docs/git-rebase">git-rebase[1]</a>&nbsp;for the implications of doing so.)</p>
	</li>
</ol>

<p>Undo a merge or pull</p>

<pre>
$ git pull                         <strong>(1)</strong>
Auto-merging nitfol
CONFLICT (content): Merge conflict in nitfol
Automatic merge failed; fix conflicts and then commit the result.
$ git reset --hard                 <strong>(2)</strong>
$ git pull . topic/branch          <strong>(3)</strong>
Updating from 41223... to 13134...
Fast-forward
$ git reset --hard ORIG_HEAD       <strong>(4)</strong></pre>

<ol>
	<li>
	<p>Try to update from the upstream resulted in a lot of conflicts; you were not ready to spend a lot of time merging right now, so you decide to do that later.</p>
	</li>
	<li>
	<p>&quot;pull&quot; has not made merge commit, so &quot;git reset --hard&quot; which is a synonym for &quot;git reset --hard HEAD&quot; clears the mess from the index file and the working tree.</p>
	</li>
	<li>
	<p>Merge a topic branch into the current branch, which resulted in a fast-forward.</p>
	</li>
	<li>
	<p>But you decided that the topic branch is not ready for public consumption yet. &quot;pull&quot; or &quot;merge&quot; always leaves the original tip of the current branch in ORIG_HEAD, so resetting hard to it brings your index file and the working tree back to that state, and resets the tip of the branch to that commit.</p>
	</li>
</ol>

<p>Undo a merge or pull inside a dirty working tree</p>

<pre>
$ git pull                         <strong>(1)</strong>
Auto-merging nitfol
Merge made by recursive.
 nitfol                |   20 +++++----
 ...
$ git reset --merge ORIG_HEAD      <strong>(2)</strong></pre>

<ol>
	<li>
	<p>Even if you may have local modifications in your working tree, you can safely say &quot;git pull&quot; when you know that the change in the other branch does not overlap with them.</p>
	</li>
	<li>
	<p>After inspecting the result of the merge, you may find that the change in the other branch is unsatisfactory. Running &quot;git reset --hard ORIG_HEAD&quot; will let you go back to where you were, but it will discard your local changes, which you do not want. &quot;git reset --merge&quot; keeps your local changes.</p>
	</li>
</ol>

<p>Interrupted workflow</p>

<p>Suppose you are interrupted by an urgent fix request while you are in the middle of a large change. The files in your working tree are not in any shape to be committed yet, but you need to get to the other branch for a quick bugfix.</p>

<pre>
$ git checkout feature ;# you were working in &quot;feature&quot; branch and
$ work work work       ;# got interrupted
$ git commit -a -m &quot;snapshot WIP&quot;                 <strong>(1)</strong>
$ git checkout master
$ fix fix fix
$ git commit ;# commit with real log
$ git checkout feature
$ git reset --soft HEAD^ ;# go back to WIP state  <strong>(2)</strong>
$ git reset                                       <strong>(3)</strong></pre>

<ol>
	<li>
	<p>This commit will get blown away so a throw-away log message is OK.</p>
	</li>
	<li>
	<p>This removes the&nbsp;<em>WIP</em>&nbsp;commit from the commit history, and sets your working tree to the state just before you made that snapshot.</p>
	</li>
	<li>
	<p>At this point the index file still has all the WIP changes you committed as&nbsp;<em>snapshot WIP</em>. This updates the index to show your WIP files as uncommitted.</p>
	</li>
</ol>

<p>See also&nbsp;<a href="https://git-scm.com/docs/git-stash">git-stash[1]</a>.</p>

<p>Reset a single file in the index</p>

<p>Suppose you have added a file to your index, but later decide you do not want to add it to your commit. You can remove the file from the index while keeping your changes with git reset.</p>

<pre>
$ git reset -- frotz.c                      <strong>(1)</strong>
$ git commit -m &quot;Commit files in index&quot;     <strong>(2)</strong>
$ git add frotz.c                           <strong>(3)</strong></pre>

<ol>
	<li>
	<p>This removes the file from the index while keeping it in the working directory.</p>
	</li>
	<li>
	<p>This commits all other changes in the index.</p>
	</li>
	<li>
	<p>Adds the file to the index again.</p>
	</li>
</ol>

<p>Keep changes in working tree while discarding some previous commits</p>

<p>Suppose you are working on something and you commit it, and then you continue working a bit more, but now you think that what you have in your working tree should be in another branch that has nothing to do with what you committed previously. You can start a new branch and reset it while keeping the changes in your working tree.</p>

<pre>
$ git tag start
$ git checkout -b branch1
$ edit
$ git commit ...                            <strong>(1)</strong>
$ edit
$ git checkout -b branch2                   <strong>(2)</strong>
$ git reset --keep start                    <strong>(3)</strong></pre>

<ol>
	<li>
	<p>This commits your first edits in branch1.</p>
	</li>
	<li>
	<p>In the ideal world, you could have realized that the earlier commit did not belong to the new topic when you created and switched to branch2 (i.e. &quot;git checkout -b branch2 start&quot;), but nobody is perfect.</p>
	</li>
	<li>
	<p>But you can use &quot;reset --keep&quot; to remove the unwanted commit after you switched to &quot;branch2&quot;.</p>
	</li>
</ol>

<p>Split a commit apart into a sequence of commits</p>

<p>Suppose that you have created lots of logically separate changes and committed them together. Then, later you decide that it might be better to have each logical chunk associated with its own commit. You can use git reset to rewind history without changing the contents of your local files, and then successively use&nbsp;<code>git add -p</code>&nbsp;to interactively select which hunks to include into each commit, using&nbsp;<code>git commit -c</code>&nbsp;to pre-populate the commit message.</p>

<pre>
$ git reset -N HEAD^                        <strong>(1)</strong>
$ git add -p                                <strong>(2)</strong>
$ git diff --cached                         <strong>(3)</strong>
$ git commit -c HEAD@{1}                    <strong>(4)</strong>
...                                         <strong>(5)</strong>
$ git add ...                               <strong>(6)</strong>
$ git diff --cached                         <strong>(7)</strong>
$ git commit ...                            <strong>(8)</strong></pre>

<ol>
	<li>
	<p>First, reset the history back one commit so that we remove the original commit, but leave the working tree with all the changes. The -N ensures that any new files added with HEAD are still marked so that git add -p will find them.</p>
	</li>
	<li>
	<p>Next, we interactively select diff hunks to add using the git add -p facility. This will ask you about each diff hunk in sequence and you can use simple commands such as &quot;yes, include this&quot;, &quot;No don&rsquo;t include this&quot; or even the very powerful &quot;edit&quot; facility.</p>
	</li>
	<li>
	<p>Once satisfied with the hunks you want to include, you should verify what has been prepared for the first commit by using git diff --cached. This shows all the changes that have been moved into the index and are about to be committed.</p>
	</li>
	<li>
	<p>Next, commit the changes stored in the index. The -c option specifies to pre-populate the commit message from the original message that you started with in the first commit. This is helpful to avoid retyping it. The HEAD@{1} is a special notation for the commit that HEAD used to be at prior to the original reset commit (1 change ago). See&nbsp;<a href="https://git-scm.com/docs/git-reflog">git-reflog[1]</a>&nbsp;for more details. You may also use any other valid commit reference.</p>
	</li>
	<li>
	<p>You can repeat steps 2-4 multiple times to break the original code into any number of commits.</p>
	</li>
	<li>
	<p>Now you&rsquo;ve split out many of the changes into their own commits, and might no longer use the patch mode of git add, in order to select all remaining uncommitted changes.</p>
	</li>
	<li>
	<p>Once again, check to verify that you&rsquo;ve included what you want to. You may also wish to verify that git diff doesn&rsquo;t show any remaining changes to be committed later.</p>
	</li>
	<li>
	<p>And finally create the final commit.</p>
	</li>
</ol>

<h2>DISCUSSION</h2>

<p>The tables below show what happens when running:</p>

<pre>
git reset --option target</pre>

<p>to reset the HEAD to another commit (<code>target</code>) with the different reset options depending on the state of the files.</p>

<p>In these tables, A, B, C and D are some different states of a file. For example, the first line of the first table means that if a file is in state A in the working tree, in state B in the index, in state C in HEAD and in state D in the target, then &quot;git reset --soft target&quot; will leave the file in the working tree in state A and in the index in state B. It resets (i.e. moves) the HEAD (i.e. the tip of the current branch, if you are on one) to &quot;target&quot; (which has the file in state D).</p>

<pre>
  working index HEAD target         working index HEAD
  ----------------------------------------------------
   A       B     C    D     --soft   A       B     D
--mixed  A       D     D
--hard   D       D     D
--merge (disallowed)
--keep  (disallowed)</pre>

<pre>
  working index HEAD target         working index HEAD
  ----------------------------------------------------
   A       B     C    C     --soft   A       B     C
--mixed  A       C     C
--hard   C       C     C
--merge (disallowed)
--keep   A       C     C</pre>

<pre>
  working index HEAD target         working index HEAD
  ----------------------------------------------------
   B       B     C    D     --soft   B       B     D
--mixed  B       D     D
--hard   D       D     D
--merge  D       D     D
--keep  (disallowed)</pre>

<pre>
  working index HEAD target         working index HEAD
  ----------------------------------------------------
   B       B     C    C     --soft   B       B     C
--mixed  B       C     C
--hard   C       C     C
--merge  C       C     C
--keep   B       C     C</pre>

<pre>
  working index HEAD target         working index HEAD
  ----------------------------------------------------
   B       C     C    D     --soft   B       C     D
--mixed  B       D     D
--hard   D       D     D
--merge (disallowed)
--keep  (disallowed)</pre>

<pre>
  working index HEAD target         working index HEAD
  ----------------------------------------------------
   B       C     C    C     --soft   B       C     C
--mixed  B       C     C
--hard   C       C     C
--merge  B       C     C
--keep   B       C     C</pre>

<p>&quot;reset --merge&quot; is meant to be used when resetting out of a conflicted merge. Any mergy operation guarantees that the working tree file that is involved in the merge does not have local change wrt the index before it starts, and that it writes the result out to the working tree. So if we see some difference between the index and the target and also between the index and the working tree, then it means that we are not resetting out from a state that a mergy operation left after failing with a conflict. That is why we disallow --merge option in this case.</p>

<p>&quot;reset --keep&quot; is meant to be used when removing some of the last commits in the current branch while keeping changes in the working tree. If there could be conflicts between the changes in the commit we want to remove and the changes in the working tree we want to keep, the reset is disallowed. That&rsquo;s why it is disallowed if there are both changes between the working tree and HEAD, and between HEAD and the target. To be safe, it is also disallowed when there are unmerged entries.</p>

<p>The following tables show what happens when there are unmerged entries:</p>

<pre>
  working index HEAD target         working index HEAD
  ----------------------------------------------------
   X       U     A    B     --soft  (disallowed)
--mixed  X       B     B
--hard   B       B     B
--merge  B       B     B
--keep  (disallowed)</pre>

<pre>
  working index HEAD target         working index HEAD
  ----------------------------------------------------
   X       U     A    A     --soft  (disallowed)
--mixed  X       A     A
--hard   A       A     A
--merge  A       A     A
--keep  (disallowed)</pre>

<p>X means any state and U means an unmerged index.</p>
