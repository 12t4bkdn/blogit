<h2>Installing Bower</h2>

<p>Where Should Bower Run?</p>

<p>Bower&rsquo;s one of those utilities you can run either from your Host OS or from the Homestead VM. In this book I&rsquo;ll use the Host OS, but if you have any issues just use the Homestead VM.</p>

<p>Decide where you&rsquo;ll run bower and consistently&nbsp;<em>only run it from there</em>.</p>

<p>Since bower runs with NodeJS, you need to install it globally first. If you haven&rsquo;t already installed bower globally, follow the instructions below.</p>

<p>Installing Bower Globally</p>

<pre>
<code>~% npm install -g bower
/usr/local/bin/bower -&gt; /usr/local/lib/node_modules/bower/bin/bower
bower@1.4.1 /usr/local/lib/node_modules/bower
├── is-root@1.0.0
[snip]
</code></pre>

<p><em>(Note you may need to use&nbsp;<code>sudo</code>&nbsp;or run the above command from a Windows Command Prompt with Administration privileges.)</em></p>

<p>Next create a&nbsp;<code>.bowerrc</code>&nbsp;file in the root of the&nbsp;<strong>l5beauty</strong>&nbsp;project. This is optional. What we&rsquo;re doing here is telling bower to stash anything it downloads into the&nbsp;<code>vendor</code>&nbsp;directory. If you skip this step then bower will create a directory named&nbsp;<code>bower_dl</code>&nbsp;in your root directory and store items there.</p>

<p>Contents of .bowerrc</p>

<pre>
<code>{
  "directory": "vendor/bower_dl"
}
</code></pre>

<p>Then install bower locally within the&nbsp;<strong>l5project</strong></p>

<p>Installing Bower Locally</p>

<pre>
<code>~% cd Code/l5beauty
~/Code/l5beauty% npm install bower
bower@1.4.1 node_modules/bower
├── is-root@1.0.0
├── junk@1.0.1
[snip]
</code></pre>

<p>Finally, create the&nbsp;<code>bower.json</code>&nbsp;file in the project root. This is will be where bower keeps track of packages to maintain. It&rsquo;s like&nbsp;<code>composer.json</code>, but for bower.</p>

<p>Contents bower.json file</p>

<pre>
<code>{
  "name": "l5beauty",
  "description": "My awesome blog",
  "ignore": [
    "**/.*",
    "node_modules",
    "vendor/bower_dl",
    "test",
    "tests"
  ]
}
</code></pre>

<h2>Pulling in Bootstrap</h2>

<p>Now that bower&rsquo;s set up to use, let&rsquo;s use it to pull some assets off from the web which we want to be part of the administration area of&nbsp;<strong>l5beauty</strong>.</p>

<p>Since we&rsquo;re currently using Bootstrap, we&rsquo;ll start with that (and jquery).</p>

<p>Installing Jquery and Bootstrap</p>

<pre>
<code>~/Code/l5beauty% bower install jquery bootstrap --save
bower jquery#*              not-cached git://github.com/jquery/jquery.git#*
bower jquery#*                 resolve git://github.com/jquery/jquery.git#*
bower bootstrap#*           not-cached git://github.com/twbs/bootstrap.git#*
bower bootstrap#*              resolve git://github.com/twbs/bootstrap.git#*
bower jquery#*                download https://github.com/.../2.1.4.tar.gz
bower bootstrap#*             download https://github.com/.../v3.3.5.tar.gz
bower jquery#*                 extract archive.tar.gz
bower bootstrap#*              extract archive.tar.gz
bower jquery#*                resolved git://github.com/jquery/jquery.git#2.1.4
bower bootstrap#*             resolved git://github.com/....git#3.3.5
bower jquery#&gt;= 1.9.1          install jquery#2.1.4
bower bootstrap#~3.3.5         install bootstrap#3.3.5

jquery#2.1.4 vendor/bower_dl/jquery

bootstrap#3.3.5 vendor/bower_dl/bootstrap
└── jquery#2.1.4
</code></pre>

<p><em>(Your output may vary slightly.)</em></p>

<p>Now if you look at&nbsp;<code>bower.json</code>&nbsp;you&rsquo;ll notice two dependencies were added. One for jquery and one for bootstrap.</p>

<p>New dependencies in bower.json</p>

<pre>
<code>{
  ...
  "dependencies": {
    "jquery": "~2.1.4",
    "bootstrap": "~3.3.5"
  }
}
</code></pre>

<p>These two packages were downloaded into the&nbsp;<code>vendor/bower_dl</code>&nbsp;directory.</p>

<p>The bower update command</p>

<p>To get the latest versions of any of your bower dependencies, simply run the&nbsp;<code>bower update</code>&nbsp;command from the root directory of the&nbsp;<strong>l5beauty</strong>&nbsp;project.</p>

<h2>Creating admin.less</h2>

<p>We&rsquo;ll use gulp to compile Bootstrap&rsquo;s less file for the administration pages. Create&nbsp;<code>admin.less</code>&nbsp;in the&nbsp;<code>resources/assets/less</code>&nbsp;directory with the following content.</p>

<p>Content of admin.less</p>

<pre>
<code>@import "bootstrap/bootstrap";
@import "//fonts.googleapis.com/css?family=Roboto:400,300";

@btn-font-weight: 300;
@font-family-sans-serif: "Roboto", Helvetica, Arial, sans-serif;

body, label, .checkbox label {
  font-weight: 300;
}
</code></pre>

<p>First we import the bootstrap.less file&nbsp;<em>(which doesn&rsquo;t exist yet, we&rsquo;ll copy it to the correct location with gulp shortly.)</em>&nbsp;Then we import the font we&rsquo;ll be using and add a few small tweaks to the CSS.</p>

<h2>Gulping Bootstrap</h2>

<p>Now that bower is pulling in the latest jquery and bootstrap, gulp can be used to merge it into your project.</p>

<p>Update&nbsp;<code>gulpfile.js</code>&nbsp;to match what&rsquo;s below.</p>

<p>New gulpfile.js</p>

<pre>
<code>var gulp = require('gulp');
var elixir = require('laravel-elixir');

/**
 * Copy any needed files.
 *
 * Do a 'gulp copyfiles' after bower updates
 */
gulp.task("copyfiles", function() {

  gulp.src("vendor/bower_dl/jquery/dist/jquery.js")
    .pipe(gulp.dest("resources/assets/js/"));

  gulp.src("vendor/bower_dl/bootstrap/less/**")
    .pipe(gulp.dest("resources/assets/less/bootstrap"));

  gulp.src("vendor/bower_dl/bootstrap/dist/js/bootstrap.js")
    .pipe(gulp.dest("resources/assets/js/"));

  gulp.src("vendor/bower_dl/bootstrap/dist/fonts/**")
    .pipe(gulp.dest("public/assets/fonts"));

});

/**
 * Default gulp is to run this elixir stuff
 */
elixir(function(mix) {

  // Combine scripts
  mix.scripts([
      'js/jquery.js',
      'js/bootstrap.js'
    ],
    'public/assets/js/admin.js',
    'resources/assets'
  );

  // Compile Less
  mix.less('admin.less', 'public/assets/css/admin.css');
});
</code></pre>

<p>This file changed quite a bit.</p>

<p>First of all we added a&nbsp;<strong>copyfiles</strong>&nbsp;gulp task. The reason we&rsquo;re doing this is twofold:</p>

<ol>
	<li>Gulp runs asynchronously. When files are copied they may still be being copied when they&rsquo;re combined with&nbsp;<code>mix.less()</code>&nbsp;or&nbsp;<code>mix.scripts()</code>.</li>
	<li>Copying the files only needs to occur after a&nbsp;<code>bower update</code>.</li>
</ol>

<p>The&nbsp;<code>scripts()</code>&nbsp;function will combine&nbsp;<code>jquery.js</code>&nbsp;and&nbsp;<code>bootstrap.js</code>&nbsp;into one file, which we&rsquo;re naming&nbsp;<code>public/assets/js/admin.js</code>. And the&nbsp;<code>less()</code>function will process the&nbsp;<code>admin.less</code>&nbsp;file we just created, pulling in bootstrap.</p>

<p><code>phpUnit()</code>&nbsp;was removed from&nbsp;<code>gulpfile.js</code>&nbsp;because we&rsquo;re not worried about testing in this book.</p>

<h2>Running gulp</h2>

<p>Since bower has been updated, run&nbsp;<code>gulp copyfiles</code>&nbsp;followed by&nbsp;<code>gulp</code>&nbsp;without any argument.</p>

<p>Running gulp twice</p>

<pre>
<code>~/Code/l5beauty% gulp copyfiles
[11:54:39] Using gulpfile ~/Projects/l5beauty/gulpfile.js
[11:54:39] Starting 'copyfiles'...
[11:54:39] Finished 'copyfiles' after 19 ms

~/Code/l5beauty% gulp
[11:55:33] Using gulpfile ~/Projects/l5beauty/gulpfile.js
[11:55:33] Starting 'default'...
[11:55:33] Starting 'scripts'...
[11:55:33] Merging: resources/assets/js/jquery.js,
  resources/assets/js/bootstrap.js
[11:55:34] Finished 'default' after 106 ms
[11:55:34] Finished 'scripts' after 228 ms
[11:55:34] Starting 'less'...
[11:55:34] Running Less: resources/assets/less/admin.less
[11:55:35] gulp-notify: [Laravel Elixir] Less Compiled!
[11:55:35] Finished 'less' after 829 ms
</code></pre>

<p>Everything should copy, combine, and compile as expected. Examine the&nbsp;<code>public/assets</code>&nbsp;directory to double-check what&rsquo;s expected there exists. You should have the following:</p>

<ul>
	<li>The directory&nbsp;<code>public/assets/fonts</code></li>
	<li>The file&nbsp;<code>public/assets/css/admin.css</code></li>
	<li>The file&nbsp;<code>public/assets/js/admin.js</code></li>
</ul>

<h2>Updating the admin layout</h2>

<p>Since we&rsquo;re loading jQuery and Bootstrap locally now from the combined files, the administration layout can be updated. Update&nbsp;<code>layout.blade.php</code>&nbsp;in the&nbsp;<code>resources/views/admin</code>&nbsp;directory to match what&rsquo;s below.</p>

<p>New admin layout</p>

<pre>
<code>&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
  &lt;meta charset="utf-8"&gt;
  &lt;meta http-equiv="X-UA-Compatible" content="IE=edge"&gt;
  &lt;meta name="viewport" content="width=device-width, initial-scale=1"&gt;

  &lt;title&gt;{{ config('blog.title') }} Admin&lt;/title&gt;

  &lt;link href="/assets/css/admin.css" rel="stylesheet"&gt;
  @yield('styles')

  &lt;!--[if lt IE 9]&gt;
    &lt;script src="//oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"&gt;&lt;/script&gt;
    &lt;script src="//oss.maxcdn.com/respond/1.4.2/respond.min.js"&gt;&lt;/script&gt;
  &lt;![endif]--&gt;
&lt;/head&gt;
&lt;body&gt;

&lt;nav class="navbar navbar-default"&gt;
  &lt;div class="container-fluid"&gt;
    &lt;div class="navbar-header"&gt;
      &lt;button type="button" class="navbar-toggle collapsed"
              data-toggle="collapse" data-target="#navbar-menu"&gt;
        &lt;span class="sr-only"&gt;Toggle Navigation&lt;/span&gt;
        &lt;span class="icon-bar"&gt;&lt;/span&gt;
        &lt;span class="icon-bar"&gt;&lt;/span&gt;
        &lt;span class="icon-bar"&gt;&lt;/span&gt;
      &lt;/button&gt;
      &lt;a class="navbar-brand" href="#"&gt;{{ config('blog.title') }} Admin&lt;/a&gt;
    &lt;/div&gt;
    &lt;div class="collapse navbar-collapse" id=navbar-menu"&gt;
      @include('admin.partials.navbar')
    &lt;/div&gt;
  &lt;/div&gt;
&lt;/nav&gt;

@yield('content')

&lt;script src="/assets/js/admin.js"&gt;&lt;/script&gt;

@yield('scripts')

&lt;/body&gt;
&lt;/html&gt;
</code></pre>

<p>The only changes were the CSS link in the header and replacing the two script lines at the bottom with the new, combined&nbsp;<code>admin.js</code>.</p>

<p>Go to&nbsp;<code>http://l5beauty.app/admin</code>&nbsp;in your browser. The administration area (and logon form) should look exactly the same as it did before.</p>

<h2>Adding FontAwesome and DataTables</h2>

<p>Now that bower and gulp are set up to handle our assets correctly, let&rsquo;s add two more packages:&nbsp;<a href="http://fortawesome.github.io/Font-Awesome/">Font Awesome</a>&nbsp;and&nbsp;<a href="https://www.datatables.net/">DataTables</a>.</p>

<p>Follow the instructions below to add these packages as bower dependancies.</p>

<p>Adding FontAwesome and DataTables to bower</p>

<pre>
<code>~/Code/l5beauty% bower install fontawesome --save
~/Code/l5beauty% bower install datatables --save
~/Code/l5beauty% bower install datatables-plugins --save
</code></pre>

<p><em>(We&rsquo;re adding datatables-plugins in order to use bootstrap specific styles in DataTables.)</em></p>

<p>Next edit&nbsp;<code>gulpfile.js</code>&nbsp;to copy the needed assets into our project.</p>

<p>Updated gulpfile.js</p>

<pre>
<code>var gulp = require('gulp');
var rename = require('gulp-rename');
var elixir = require('laravel-elixir');

/**
 * Copy any needed files.
 *
 * Do a 'gulp copyfiles' after bower updates
 */
gulp.task("copyfiles", function() {

  // Copy jQuery, Bootstrap, and FontAwesome
  gulp.src("vendor/bower_dl/jquery/dist/jquery.js")
      .pipe(gulp.dest("resources/assets/js/"));

  gulp.src("vendor/bower_dl/bootstrap/less/**")
      .pipe(gulp.dest("resources/assets/less/bootstrap"));

  gulp.src("vendor/bower_dl/bootstrap/dist/js/bootstrap.js")
      .pipe(gulp.dest("resources/assets/js/"));

  gulp.src("vendor/bower_dl/bootstrap/dist/fonts/**")
      .pipe(gulp.dest("public/assets/fonts"));

  gulp.src("vendor/bower_dl/fontawesome/less/**")
      .pipe(gulp.dest("resources/assets/less/fontawesome"));

  gulp.src("vendor/bower_dl/fontawesome/fonts/**")
      .pipe(gulp.dest("public/assets/fonts"));

  // Copy datatables
  var dtDir = 'vendor/bower_dl/datatables-plugins/integration/';

  gulp.src("vendor/bower_dl/datatables/media/js/jquery.dataTables.js")
      .pipe(gulp.dest('resources/assets/js/'));

  gulp.src(dtDir + 'bootstrap/3/dataTables.bootstrap.css')
      .pipe(rename('dataTables.bootstrap.less'))
      .pipe(gulp.dest('resources/assets/less/others/'));

  gulp.src(dtDir + 'bootstrap/3/dataTables.bootstrap.js')
      .pipe(gulp.dest('resources/assets/js/'));

});

/**
 * Default gulp is to run this elixir stuff
 */
elixir(function(mix) {

  // Combine scripts
  mix.scripts([
      'js/jquery.js',
      'js/bootstrap.js',
      'js/jquery.dataTables.js',
      'js/dataTables.bootstrap.js'
    ],
    'public/assets/js/admin.js',
    'resources/assets'
);

  // Compile Less
  mix.less('admin.less', 'public/assets/css/admin.css');
});
</code></pre>

<p>Now edit the&nbsp;<code>admin.less</code>&nbsp;file in&nbsp;<code>resources/assets/less</code>&nbsp;to match what&rsquo;s below.</p>

<p>Content of admin.less</p>

<pre>
<code>@import "bootstrap/bootstrap";
@import "//fonts.googleapis.com/css?family=Roboto:400,300";

@btn-font-weight: 300;
@font-family-sans-serif: "Roboto", Helvetica, Arial, sans-serif;

body, label, .checkbox label {
  font-weight: 300;
}

@import "fontawesome/font-awesome";
@import "others/dataTables.bootstrap.less";
</code></pre>

<p>Since we&rsquo;re renaming a file using gulp instead of elixir (for that&nbsp;<em>copyfiles</em>&nbsp;task), we need to pull in the gulp-rename module.</p>

<p>Pulling in gulp-rename</p>

<pre>
<code>%/Code/l5beauty% npm install gulp-rename --save
gulp-rename@1.2.2 node_modules/gulp-rename
</code></pre>

<p>Now run&nbsp;<code>gulp</code>&nbsp;twice. (Once to copy the files because we added bower assets and once to process and combine the assets.)</p>

<p>Running gulp twice</p>

<pre>
<code>~/Code/l5beauty% gulp copyfiles
[12:52:02] Using gulpfile ~/Projects/l5beauty/gulpfile.js
[12:52:02] Starting 'copyfiles'...
[12:52:02] Finished 'copyfiles' after 31 ms

~/Code/l5beauty% gulp
[12:52:26] Using gulpfile ~/Projects/l5beauty/gulpfile.js
[12:52:26] Starting 'default'...
[12:52:26] Starting 'scripts'...
[12:52:26] Merging: resources/assets/js/jquery.js,
  resources/assets/js/bootstrap.js, resources/assets/js/jquery.dataTables.js,
  resources/assets/js/dataTables.bootstrap.js
[12:52:26] Finished 'default' after 107 ms
[12:52:26] Finished 'scripts' after 401 ms
[12:52:26] Starting 'less'...
[12:52:26] Running Less: resources/assets/less/admin.less
[12:52:30] gulp-notify: [Laravel Elixir] Less Compiled!
[12:52:30] Finished 'less' after 4.19 s
</code></pre>

<h2>Recap</h2>

<p>In this chapter we used bower to download jQuery, Bootstrap, Font Awesome, and Datatables from the Internet. Then gulp was used to combine everything into a single CSS file (admin.css) and a single Javascript file (admin.js).</p>
