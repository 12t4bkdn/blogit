<p>In this chapter we&rsquo;ll add a&nbsp;<em>Contact Us</em>&nbsp;form to the blog. To do this we&rsquo;ll explore Laravel&rsquo;s mailing functions and set up a queue for asynchronous processing.</p>

<h2>Contents</h2>

<ul>
	<li><a href="http://laravelcoding.com/blog/laravel-5-beauty-sending-mail-and-using-queues?tag=L5+Beauty#14-email-setup">Setting Up for Emails</a>

	<ul>
		<li><a href="http://laravelcoding.com/blog/laravel-5-beauty-sending-mail-and-using-queues?tag=L5+Beauty#14-email-gmail">Configuring for Gmail</a></li>
		<li><a href="http://laravelcoding.com/blog/laravel-5-beauty-sending-mail-and-using-queues?tag=L5+Beauty#14-email-mailgun">Configuring for Mailgun</a></li>
		<li><a href="http://laravelcoding.com/blog/laravel-5-beauty-sending-mail-and-using-queues?tag=L5+Beauty#14-email-tinker">Testing Mail with Tinker</a></li>
	</ul>
	</li>
	<li><a href="http://laravelcoding.com/blog/laravel-5-beauty-sending-mail-and-using-queues?tag=L5+Beauty#14-contact-us">Adding a Contact Us Form</a>
	<ul>
		<li><a href="http://laravelcoding.com/blog/laravel-5-beauty-sending-mail-and-using-queues?tag=L5+Beauty#14-contact-link">Adding the Link and Route</a></li>
		<li><a href="http://laravelcoding.com/blog/laravel-5-beauty-sending-mail-and-using-queues?tag=L5+Beauty#14-contact-request">Creating the FormRequest</a></li>
		<li><a href="http://laravelcoding.com/blog/laravel-5-beauty-sending-mail-and-using-queues?tag=L5+Beauty#14-contact-ctrl">Adding the Controller</a></li>
		<li><a href="http://laravelcoding.com/blog/laravel-5-beauty-sending-mail-and-using-queues?tag=L5+Beauty#14-contact-views">Creating the Views</a></li>
		<li><a href="http://laravelcoding.com/blog/laravel-5-beauty-sending-mail-and-using-queues?tag=L5+Beauty#14-contact-send">Sending the Mail</a></li>
	</ul>
	</li>
	<li><a href="http://laravelcoding.com/blog/laravel-5-beauty-sending-mail-and-using-queues?tag=L5+Beauty#14-about-queues">About Queues</a>
	<ul>
		<li><a href="http://laravelcoding.com/blog/laravel-5-beauty-sending-mail-and-using-queues?tag=L5+Beauty#14-queue-how">How they Work</a></li>
		<li><a href="http://laravelcoding.com/blog/laravel-5-beauty-sending-mail-and-using-queues?tag=L5+Beauty#14-queue-drivers">The Different Queue Drivers</a></li>
		<li><a href="http://laravelcoding.com/blog/laravel-5-beauty-sending-mail-and-using-queues?tag=L5+Beauty#14-queue-dbdrv">Using the Database Driver</a></li>
	</ul>
	</li>
	<li><a href="http://laravelcoding.com/blog/laravel-5-beauty-sending-mail-and-using-queues?tag=L5+Beauty#14-queue-email">Queuing the Contact Us Email</a>
	<ul>
		<li><a href="http://laravelcoding.com/blog/laravel-5-beauty-sending-mail-and-using-queues?tag=L5+Beauty#14-queue-ctrl">Changing the Controller</a></li>
		<li><a href="http://laravelcoding.com/blog/laravel-5-beauty-sending-mail-and-using-queues?tag=L5+Beauty#14-queue-where">Where&rsquo;s the Email</a></li>
		<li><a href="http://laravelcoding.com/blog/laravel-5-beauty-sending-mail-and-using-queues?tag=L5+Beauty#14-queue-work">Running queue:work</a></li>
	</ul>
	</li>
	<li><a href="http://laravelcoding.com/blog/laravel-5-beauty-sending-mail-and-using-queues?tag=L5+Beauty#14-queue-auto">Automatically Processing the Queue</a>
	<ul>
		<li><a href="http://laravelcoding.com/blog/laravel-5-beauty-sending-mail-and-using-queues?tag=L5+Beauty#14-queue-supervise">Running queue:listen with supervisord</a></li>
		<li><a href="http://laravelcoding.com/blog/laravel-5-beauty-sending-mail-and-using-queues?tag=L5+Beauty#14-queue-schedule">Using a Scheduled Command</a></li>
	</ul>
	</li>
	<li><a href="http://laravelcoding.com/blog/laravel-5-beauty-sending-mail-and-using-queues?tag=L5+Beauty#14-queue-jobs">Queing Jobs</a></li>
	<li><a href="http://laravelcoding.com/blog/laravel-5-beauty-sending-mail-and-using-queues?tag=L5+Beauty#queue-recap">Recap</a></li>
</ul>

<h2>Setting Up for Emails</h2>

<p>In order to use Laravel 5.1&rsquo;s mail functionality it first needs to be configured. Configuration is easy. Look at the mail settings that come out of the box in the&nbsp;<code>.env</code>&nbsp;file.</p>

<p>Mail Configuration in .env</p>

<pre>
<code>MAIL_DRIVER=smtp
MAIL_HOST=mailtrap.io
MAIL_PORT=2525
MAIL_USERNAME=null
MAIL_PASSWORD=null
</code></pre>

<p>As you can see, just a few simple settings.</p>

<h3>Configuring for Gmail</h3>

<p>Let&rsquo;s say you have a gmail account you wish to configure. Here&rsquo;s how to do it.</p>

<p>First, edit&nbsp;<code>config/mail.php</code>&nbsp;as instructed below.</p>

<p>Changes to config/mail.php</p>

<pre>
<code>// Find the following line
  'from' =&gt; ['address' =&gt; null, 'name' =&gt; null],
// Change it to
  'from' =&gt; ['address' =&gt; env('MAIL_FROM'), 'name' =&gt; env('MAIL_NAME')],
</code></pre>

<p>This sets up who the emails are from which is required by Gmail and is good practice for others.</p>

<p>Next, edit&nbsp;<code>.env</code>, changing the mail configuration to what&rsquo;s below (replacing USERNAME, PASSWORD, FROM, etc. your own settings).</p>

<p>Gmail Configuration in .env</p>

<pre>
<code>MAIL_DRIVER=smtp
MAIL_HOST=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=YOUR@EMAIL.COM
MAIL_PASSWORD=YOUR-GMAIL-PASSWORD
MAIL_FROM=YOUR@EMAIL.COM
MAIL_NAME=YOUR-NAME
</code></pre>

<p>Are You Using 2-Step Authentication</p>

<p>If your Gmail account uses 2-Step Authentication then the password required will not be the same one you log into Gmail with. You&rsquo;ll need to set up an App Password. See&nbsp;<a href="https://support.google.com/accounts/answer/185833">Google Help</a>&nbsp;for instructions on how to do this.</p>

<p>The section after the next one (Testing Mail with Tinker) will explain how you can test your mail configuration.</p>

<h3>Configuring for Mailgun</h3>

<p>Another popular option is to use&nbsp;<a href="http://www.mailgun.com/">Mailgun</a>&nbsp;to send your email. I use Mailgun. It&rsquo;s completely free for the first 10,000 emails you send each month. After that it&rsquo;s a penny for every 20 emails.</p>

<p>To configure to send through mailgun, first edit&nbsp;<code>config/services.php</code>&nbsp;to match what&rsquo;s below.</p>

<p>Mailgun Settings in config/services.php</p>

<pre>
<code>  'mailgun' =&gt; [
    'domain' =&gt; env('MAILGUN_DOMAIN'),
    'secret' =&gt; env('MAILGUN_SECRET'),
  ],
</code></pre>

<p>Yes, we&rsquo;re just setting it up to read the values from the&nbsp;<code>.env</code>&nbsp;file.</p>

<p>Next, Mailgun requires the&nbsp;<a href="http://docs.guzzlephp.org/en/latest/">Guzzle Http</a>&nbsp;library, so use composer to require it.</p>

<p>Requiring Guzzle Http</p>

<pre>
<code>~/Code/l5beauty% composer require "guzzlehttp/guzzle=~5.0"
./composer.json has been updated
Loading composer repositories with package information
Updating dependencies (including require-dev)
  - Installing react/promise (v2.2.0)
    Loading from cache

  - Installing guzzlehttp/streams (3.0.0)
    Loading from cache

  - Installing guzzlehttp/ringphp (1.1.0)
    Loading from cache

  - Installing guzzlehttp/guzzle (5.3.0)
    Loading from cache

Writing lock file
Generating autoload files
Generating optimized class loader
</code></pre>

<p>Finally, edit&nbsp;<code>.env</code>&nbsp;and change the settings for Mailgun.</p>

<p>Mailgun Configuration in .env</p>

<pre>
<code>MAIL_DRIVER=mailgun
MAIL_FROM=YOUR@EMAIL.COM
MAIL_NAME=YOUR-NAME
MAILGUN_DOMAIN=THE-DOMAIN-SETUP-IN-MAILGUN
MAILGUN_SECRET=THE-API-KEY-FOR-DOMAIN
</code></pre>

<p>The nice thing about Mailgun is that email is sent via an API, which is faster than using SMTP.</p>

<h3>Testing Mail with Tinker</h3>

<p>Laravel&rsquo;s emailer always uses views to send the email. So let&rsquo;s first create a simple test view.</p>

<p>Create the&nbsp;<code>resources/views/emails</code>&nbsp;directory and within it create the&nbsp;<code>test.blade.php</code>&nbsp;file with the following content.</p>

<p>Content of emails.test view</p>

<pre>
<code>&lt;p&gt;
  This is a test, an email test.
&lt;/p&gt;
&lt;p&gt;
  The variable &lt;code&gt;$testVar&lt;/code&gt; contains the value:
&lt;/p&gt;
&lt;ul&gt;
  &lt;li&gt;&lt;strong&gt;{{ $testVar }}&lt;/strong&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;hr&gt;
&lt;p&gt;
  That is all.
&lt;/p&gt;
</code></pre>

<p>Now fire up the&nbsp;<code>artisan tinker</code>&nbsp;command and send an email to yourself as instructed below.</p>

<p>Testing Email with Tinker</p>

<pre>
<code>~/Code/l5beauty$ php artisan tinker
Psy Shell v0.4.4 (PHP 5.6.2 — cli) by Justin Hileman
&gt;&gt;&gt; Mail::send('emails.test',
... ['testVar' =&gt; 'Just a silly test'],
... function($message) {
...   $message-&gt;to('YOUR@EMAIL.com')
...           -&gt;subject('A simple test');
... });
=&gt; 1
&gt;&gt;&gt; exit
</code></pre>

<p>The first argument is the view. The second is an array of any variables the view requires (and&nbsp;<code>emails.test</code>&nbsp;requires&nbsp;<code>testVar</code>). The third is a closure to do additional processing on the message. Here we just set the to address and the subject line.</p>

<p>You can do many things in this closure. Here&rsquo;s just a few.</p>

<ul>
	<li><code>-&gt;from($address, $name = null)</code>&nbsp;- Add a from address to the message.</li>
	<li><code>-&gt;sender($address, $name = null)</code>&nbsp;- Set the sender of the message.</li>
	<li><code>-&gt;to($address, $name = null)</code>&nbsp;- Add a recipient to the message.</li>
	<li><code>-&gt;cc($address, $name = null)</code>&nbsp;- Add a carbon copy recipient to the message.</li>
	<li><code>-&gt;bcc($address, $name = null)</code>&nbsp;- Add a blind carbon copy.</li>
	<li><code>-&gt;replyTo($address, $name = null)</code>&nbsp;- Add a reply-to recipient.</li>
	<li><code>-&gt;subject($subject)</code>&nbsp;- Set the subject of the message.</li>
	<li><code>-&gt;attach($file, array $options = [])</code>&nbsp;- Attach a file to the message.</li>
</ul>

<p>The above tinker example used a Gmail configuration, which returns&nbsp;<code>1</code>indicating success. If you use the Mailgun driver in your configuration, a successful return value will look different.</p>

<p>Testing Email with Tinker (Mailgun config)</p>

<pre>
<code>~/Code/l5beauty$ php artisan tinker
Psy Shell v0.4.4 (PHP 5.6.2 — cli) by Justin Hileman
&gt;&gt;&gt; Mail::send('emails.test',
... ['testVar' =&gt; 'Just a silly test'],
... function($message) {
...   $message-&gt;to('YOUR@EMAIL.com')
...           -&gt;subject('A simple test');
... });
=&gt; &lt;GuzzleHttp\Message\Response #0000000024da8555000000017f74f2c8&gt; {}
&gt;&gt;&gt; exit
</code></pre>

<h2>Adding a Contact Us Form</h2>

<p>Now that we know Laravel&rsquo;s mailer will work, let&rsquo;s create a form to email us contact information from the user.</p>

<h3>Adding the Link and Route</h3>

<p>The link to the contact form should appear on every blog page. Edit the navbar partials view as below.</p>

<p>Changes to partials.navbar view</p>

<pre>
<code>// Change the following area
  {{-- Collect the nav links, forms, and other content for toggling --}}
  &lt;div class="collapse navbar-collapse" id="navbar-main"&gt;
    &lt;ul class="nav navbar-nav"&gt;
      &lt;li&gt;
        &lt;a href="/"&gt;Home&lt;/a&gt;
      &lt;/li&gt;
    &lt;/ul&gt;
  &lt;/div&gt;

// To the following
  {{-- Collect the nav links, forms, and other content for toggling --}}
  &lt;div class="collapse navbar-collapse" id="navbar-main"&gt;
    &lt;ul class="nav navbar-nav"&gt;
      &lt;li&gt;
        &lt;a href="/"&gt;Home&lt;/a&gt;
      &lt;/li&gt;
    &lt;/ul&gt;
    &lt;ul class="nav navbar-nav navbar-right"&gt;
      &lt;li&gt;
        &lt;a href="/contact"&gt;Contact&lt;/a&gt;
      &lt;/li&gt;
    &lt;/ul&gt;
  &lt;/div&gt;
</code></pre>

<p>Easy, just a link which we&rsquo;ll now create a route for.</p>

<p>Changes to routes.php</p>

<pre>
<code>// After the following line
get('blog/{slug}', 'BlogController@showPost');

// Add these two lines
$router-&gt;get('contact', 'ContactController@showForm');
Route::post('contact', 'ContactController@sendContactInfo');
</code></pre>

<p>Notice we used&nbsp;<code>$router</code>&nbsp;directly instead of the&nbsp;<code>get()</code>&nbsp;function. Then instead of the&nbsp;<code>post()</code>&nbsp;function, the&nbsp;<code>Route</code>&nbsp;facade was used. This is simply to illustrate there&rsquo;s multiple ways to set up the routes. Normally, I just use the helper functions directly, but some people prefer the&nbsp;<code>$router</code>&nbsp;variable or the&nbsp;<code>Route</code>facade.</p>

<p>Routing Shortcut Functions</p>

<p>Laravel 5.1 also provides the following shortcut functions for routing. Any of these can be used directly on the&nbsp;<code>$router</code>&nbsp;variable or with the<code>Route</code>&nbsp;facade.</p>

<ul>
	<li><code>delete($uri, $action)</code>&nbsp;registers a new DELETE route.</li>
	<li><code>get($uri, $action)</code>&nbsp;registers a new GET route.</li>
	<li><code>patch($uri, $aciton)</code>&nbsp;registers a new PATCH route.</li>
	<li><code>post($uri, $action)</code>&nbsp;registers a new POST route.</li>
	<li><code>put($uri, $action)</code>&nbsp;registers a new PUT route.</li>
	<li><code>resource($name, $controller, $options)</code>&nbsp;registers a resource controller.</li>
</ul>

<p>When you group routes together, there&rsquo;s no short helper function so either&nbsp;<code>Route::group()</code>&nbsp;or&nbsp;<code>$router-&gt;group()</code>&nbsp;must be used.</p>

<h3>Creating the FormRequest</h3>

<p>We know the contact form will contain a name, email address, and a message. The Laravel&nbsp;<em>&ldquo;way&rdquo;</em>&nbsp;to validate forms is through FormRequest objects which we used quite a bit in the administration area of our blog.</p>

<p>Let&rsquo;s create the FormRequest now, so it&rsquo;s all ready when we build the controller. First use artisan to create the skeleton.</p>

<p>Creating the FormRequest with Artisan</p>

<pre>
<code>~/Code/l5beauty$ php artisan make:request ContactMeRequest
Request created successfully.
</code></pre>

<p>Update its contents to match what&rsquo;s below.</p>

<p>Content of ContactMeRequest.php</p>

<pre>
<code>&lt;?php
namespace App\Http\Requests;

class ContactMeRequest extends Request
{
  /**
   * Determine if the user is authorized to make this request.
   */
  public function authorize()
  {
    return true;
  }

  /**
   * Get the validation rules that apply to the request.
   */
  public function rules()
  {
    return [
      'name' =&gt; 'required',
      'email' =&gt; 'required|email',
      'message' =&gt; 'required',
    ];
  }
}

</code></pre>

<p>No need to comment on the request. You should be thoroughly familiar with FormRequests after building the administration side of this blog.</p>

<h3>Adding the Controller</h3>

<p>Now we&rsquo;ll create the controller we specified in the routes file.</p>

<p>Optionally, you can create the skeleton of the controller with artisan.</p>

<p>Creating ContactController with Artisan</p>

<pre>
<code>~/Code/l5beauty$ php artisan make:controller --plain ContactController
Controller created successfully.
</code></pre>

<p>Make the content of ContactController.php match what&rsquo;s below.</p>

<p>Content of ContactController.php</p>

<pre>
<code>&lt;?php
namespace App\Http\Controllers;

use App\Http\Requests\ContactMeRequest;
use Illuminate\Support\Facades\Mail;

class ContactController extends Controller
{
  /**
   * Show the form
   *
   * @return View
   */
  public function showForm()
  {
    return view('blog.contact');
  }

  /**
   * Email the contact request
   *
   * @param ContactMeRequest $request
   * @return Redirect
   */
  public function sendContactInfo(ContactMeRequest $request)
  {
    $data = $request-&gt;only('name', 'email', 'phone');
    $data['messageLines'] = explode("\n", $request-&gt;get('message'));

    Mail::send('emails.contact', $data, function ($message) use ($data) {
      $message-&gt;subject('Blog Contact Form: '.$data['name'])
              -&gt;to(config('blog.contact_email'))
              -&gt;replyTo($data['email']);
    });

    return back()
        -&gt;withSuccess("Thank you for your message. It has been sent.");
  }
}

</code></pre>

<p>In the&nbsp;<code>sendContactInfo()</code>&nbsp;method, we use the&nbsp;<code>ContactMeRequest</code>&nbsp;to validate. Then we fill&nbsp;<code>$data</code>&nbsp;with the form fields. For the&nbsp;<code>message</code>&nbsp;field, we break the message into individual lines to pass to the view as&nbsp;<code>messageLines</code>.</p>

<p>Then we use the&nbsp;<code>Mail</code>&nbsp;facade to send the message. You could optionally have the&nbsp;<code>sendContactInfo()</code>&nbsp;method take an&nbsp;<code>Illuminate\Mail\Mailer</code>&nbsp;object as an argument (Laravel 5.1 is smart enough to automatically inject it) and use this object to send mail.</p>

<p>See the&nbsp;<a href="http://laravel.com/docs/5.1/facades#facade-class-reference">Official Documentation</a>&nbsp;for a list of facades and the equivalent class to use if you want to access the instance directly.</p>

<p>After the message is sent, we redirect back to the contact page, passing a success message.</p>

<p><strong>ADD contact_email to your blog config file.</strong>&nbsp;It is needed in the controller just created (<code>config(&#39;blog.contact_email&#39;)</code>). It&rsquo;s easy to add this configuration value, just edit&nbsp;<code>config/blog.php</code>&nbsp;and add an additional option.</p>

<h3>Creating the Views</h3>

<p>Two views need to be created for the contact form. The one which will display the form and the one that formats the email to be sent.</p>

<p>Create&nbsp;<code>contact.blade.php</code>&nbsp;in the&nbsp;<code>resources/views/blog</code>&nbsp;directory.</p>

<p>Content of blog.contact view</p>

<pre>
<code>@extends('blog.layouts.master', ['meta_description' =&gt; 'Contact Form'])

@section('page-header')
  &lt;header class="intro-header"
          style="background-image: url('{{ page_image('contact-bg.jpg') }}')"&gt;
    &lt;div class="container"&gt;
      &lt;div class="row"&gt;
        &lt;div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1"&gt;
          &lt;div class="site-heading"&gt;
            &lt;h1&gt;Contact Me&lt;/h1&gt;
            &lt;hr class="small"&gt;
            &lt;h2 class="subheading"&gt;
              Have questions? I have answers (maybe).
            &lt;/h2&gt;
          &lt;/div&gt;
        &lt;/div&gt;
      &lt;/div&gt;
    &lt;/div&gt;
  &lt;/header&gt;
@stop

@section('content')
  &lt;div class="container"&gt;
    &lt;div class="row"&gt;
      &lt;div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1"&gt;
        @include('admin.partials.errors')
        @include('admin.partials.success')
        &lt;p&gt;
          Want to get in touch with me? Fill out the form below to send me a
          message and I will try to get back to you within 24 hours!
        &lt;/p&gt;
        &lt;form action="/contact" method="post"&gt;
          &lt;input type="hidden" name="_token" value="{!! csrf_token() !!}"&gt;
          &lt;div class="row control-group"&gt;
            &lt;div class="form-group col-xs-12"&gt;
              &lt;label for="name"&gt;Name&lt;/label&gt;
              &lt;input type="text" class="form-control" id="name" name="name"
                     value="{{ old('name') }}"&gt;
            &lt;/div&gt;
          &lt;/div&gt;
          &lt;div class="row control-group"&gt;
            &lt;div class="form-group col-xs-12"&gt;
              &lt;label for="email"&gt;Email Address&lt;/label&gt;
              &lt;input type="email" class="form-control" id="email" name="email"
                     value="{{ old('email') }}"&gt;
            &lt;/div&gt;
          &lt;/div&gt;
          &lt;div class="row control-group"&gt;
            &lt;div class="form-group col-xs-12 controls"&gt;
              &lt;label for="phone"&gt;Phone Number&lt;/label&gt;
              &lt;input type="tel" class="form-control" id="phone" name="phone"
                     value="{{ old('phone') }}"&gt;
            &lt;/div&gt;
          &lt;/div&gt;
          &lt;div class="row control-group"&gt;
            &lt;div class="form-group col-xs-12 controls"&gt;
              &lt;label for="message"&gt;Message&lt;/label&gt;
              &lt;textarea rows="5" class="form-control" id="message"
                        name="message"&gt;{{ old('message') }}&lt;/textarea&gt;
            &lt;/div&gt;
          &lt;/div&gt;
          &lt;br&gt;
          &lt;div class="row"&gt;
            &lt;div class="form-group col-xs-12"&gt;
              &lt;button type="submit" class="btn btn-default"&gt;Send&lt;/button&gt;
            &lt;/div&gt;
          &lt;/div&gt;
        &lt;/form&gt;
      &lt;/div&gt;
    &lt;/div&gt;
  &lt;/div&gt;
@endsection
</code></pre>

<p>The&nbsp;<code>blog.contact</code>&nbsp;view should be easy to follow. Notice how we included the&nbsp;<strong>errors</strong>&nbsp;and&nbsp;<strong>success</strong>&nbsp;partials from the administration area? They perfectly fit what was needed.</p>

<p>Now create&nbsp;<code>contact.blade.php</code>&nbsp;in the&nbsp;<code>resources/views/emails</code>&nbsp;directory. This is what will format the email we&rsquo;ll send to ourselves.</p>

<p>Content of email.contact view</p>

<pre>
<code>&lt;p&gt;
  You have received a new message from your website contact form.
&lt;/p&gt;
&lt;p&gt;
  Here are the details:
&lt;/p&gt;
&lt;ul&gt;
  &lt;li&gt;Name: &lt;strong&gt;{{ $name }}&lt;/strong&gt;&lt;/li&gt;
  &lt;li&gt;Email: &lt;strong&gt;{{ $email }}&lt;/strong&gt;&lt;/li&gt;
  &lt;li&gt;Phone: &lt;strong&gt;{{ $phone }}&lt;/strong&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;hr&gt;
&lt;p&gt;
  @foreach ($messageLines as $messageLine)
    {{ $messageLine }}&lt;br&gt;
  @endforeach
&lt;/p&gt;
&lt;hr&gt;
</code></pre>

<p>Nothing too fancy there. Just a smidge of formatting.</p>

<h3>Sending the Mail</h3>

<p>The contact form should now be fully functional. Fire up your web browser, point it to your&nbsp;<code>http://l5beauty.app</code>&nbsp;project and test it out.</p>

<p>You may notice there&rsquo;s a slight delay between clicking&nbsp;<strong>[Send]</strong>&nbsp;and receiving a response of success back. This delay can be especially long when you&rsquo;re using the&nbsp;<code>smtp</code>&nbsp;mail driver.</p>

<p>Does this delay really need to be there? The answer is no, not if we set up a queue to handle running tasks in the back ground.</p>

<h2>About Queues</h2>

<p>Queues allow you to defer the processing of time consuming tasks, such as emails. This allows your web requests to respond quicker to the user.</p>

<h3>How they Work</h3>

<p>Queues are actually quite simple to understand.</p>

<p>Figure 14.1 - Flow Through Queue</p>

<p><img alt="Queue Flow" src="http://chuckheintzelman.com.s3-us-west-2.amazonaws.com/l5beauty/queue.jpg" /></p>

<p>A web request hits the controller where it&rsquo;s processed. During the processing something is added to the queue (an Email in this figure) and then the response is returned.</p>

<p>Somewhere in the background a queue worker runs. It fetches the next thing from the queue and processes it.</p>

<p>Bam!</p>

<h3>The Different Queue Drivers</h3>

<p>Laravel provides drivers for several different queue implementation. They are:</p>

<ul>
	<li><code>sync</code>&nbsp;- The&nbsp;<code>sync</code>&nbsp;driver effectively short circuits the entire queuing process. When something is queued and the&nbsp;<code>sync</code>&nbsp;driver is being used, the item is fully processed immediately and&nbsp;<em>synchronously</em>.</li>
	<li><code>database</code>&nbsp;- The&nbsp;<code>database</code>&nbsp;driver stores queued items in the local database. Specifically, in a&nbsp;<code>jobs</code>&nbsp;table.</li>
	<li><code>beanstalkd</code>&nbsp;- The&nbsp;<code>beanstalkd</code>&nbsp;driver expects&nbsp;<a href="https://kr.github.io/beanstalkd/">beanstalkd</a>&nbsp;to be configured and running. You&rsquo;ll also have to do a&nbsp;<code>composer require &quot;pda/pheanstalk=~3.0&quot;</code>&nbsp;to use it.</li>
	<li><code>sqs</code>&nbsp;- The&nbsp;<code>sqs</code>&nbsp;driver will queue to your&nbsp;<a href="http://aws.amazon.com/sqs/">Amazon SQS</a>&nbsp;queue. Also&nbsp;<code>composer require aws/aws-sdk-php</code>&nbsp;is required to use it.</li>
	<li><code>iron</code>&nbsp;- The&nbsp;<code>iron</code>&nbsp;driver will queue to your&nbsp;<a href="http://www.iron.io/">IronMQ</a>&nbsp;account and&nbsp;<code>composer required &quot;iron-io/iron_mq=~1.5&quot;</code>&nbsp;is required.</li>
	<li><code>redis</code>&nbsp;- The&nbsp;<code>redis</code>&nbsp;driver will store queued items in the Redis database. It requires&nbsp;<code>composer require &quot;predis/predis=~1.0&quot;</code>&nbsp;to operate.</li>
</ul>

<h3>Using the Database Driver</h3>

<p>We&rsquo;ll be using the Database Driver for our queue. To do this we&rsquo;ll need to create the&nbsp;<code>jobs</code>&nbsp;table and run migrations as instructed below.</p>

<p>Creating and Running Queue Jobs Migration</p>

<pre>
<code>vagrant@homestead:~/Code/l5beauty$ php artisan queue:table
Migration created successfully!
vagrant@homestead:~/Code/l5beauty$ php artisan migrate
Migrated: 2015_06_06_130436_create_jobs_table
</code></pre>

<p>Finally, edit&nbsp;<code>.env</code>&nbsp;and change the&nbsp;<code>QUEUE_DRIVER</code>&nbsp;setting from&nbsp;<code>sync</code>&nbsp;to&nbsp;<code>database</code>.</p>

<h2>Queuing the Contact Us Email</h2>

<p>Now that the queue is set up, we&rsquo;re ready to queue emails from the Contact Us form instead of waiting for the delivery to finish before responding to the user.</p>

<h3>Changing the Controller</h3>

<p>To queue the email, there&rsquo;s only a single small change to make. Update your&nbsp;<code>ContractController</code>&nbsp;class as instructed.</p>

<p>Change to ContractController.php</p>

<pre>
<code>// Find the line below
   Mail::send('emails.contact', $data, function ($message) use ($data) {

// And change it to match what's below
   Mail::queue('emails.contact', $data, function ($message) use ($data) {

</code></pre>

<p>That&rsquo;s it! Instead of&nbsp;<code>Mail::send()</code>&nbsp;we call&nbsp;<code>Mail::queue()</code>&nbsp;and Laravel will automatically queue it for us.</p>

<h3>Where&rsquo;s the Email</h3>

<p>Test out the Contact Us form again. After you click&nbsp;<em>[Send]</em>&nbsp;there should be no delay before you see the&nbsp;<strong>Success</strong>&nbsp;message.</p>

<p>Still, you can wait forever for the email and it will never arrive.</p>

<p>Why?</p>

<p>Because there&rsquo;s no process running in the background, watching for and handling items arriving in the queue.</p>

<h3>Running queue:work</h3>

<p>To process the next item on the queue, we can manually run artisan&rsquo;s&nbsp;<code>queue:work</code>&nbsp;command.</p>

<p>This command will do nothing if the queue is empty. But if there&rsquo;s an item on the queue it will fetch the item and attempt to execute it.</p>

<p>Running Artisan queue:work</p>

<pre>
<code>vagrant@homestead:~/Code/l5beauty$ php artisan queue:work
Processed: mailer@handleQueuedMessage
</code></pre>

<p>As you can see here it handled the queued email message. Now the email should arrive in your inbox within moments.</p>

<h2>Automatically Processing the Queue</h2>

<p>Of course, having to manually log into our server and run the&nbsp;<code>artisan queue:work</code>&nbsp;each time we want to process the next item on the queue is ridiculous.</p>

<p>There&rsquo;s a few options to automate this.</p>

<p>One is load up&nbsp;<code>artisan queue:listen</code>&nbsp;in the startup scripts of your server. This command automatically calls&nbsp;<code>artisan queue:work</code>&nbsp;when items appear in the queue.</p>

<p>The problem with this technique is something will invariably happen. The&nbsp;<code>queue:listen</code>&nbsp;command will hang. Or it will stop running. A better way to run&nbsp;<code>queue:listen</code>&nbsp;is with&nbsp;<strong>supervisord</strong>.</p>

<h3>Running queue:listen with supervisord</h3>

<p><strong>supervisord</strong>&nbsp;is a *nix utility to monitor and control processes. We&rsquo;re not delving into how to install this utility, but if you have it and get it installed, below is a portion of&nbsp;<code>/etc/supervisord.conf</code>&nbsp;that works well.</p>

<p>Portion of supervisord.conf for queue:listen</p>

<pre>
<code>[program:l5beauty-queue-listen]
command=php /PATH/TO/l5beauty/artisan queue:listen
user=NONROOT-USER
process_name=%(program_name)s_%(process_num)d
directory=/PATH/TO/l5beauty
stdout_logfile=/PATH/TO/l5beauty/storage/logs/supervisord.log
redirect_stderr=true
numprocs=1
</code></pre>

<p>You&rsquo;ll need to replace the&nbsp;<code>/PATH/TO/</code>&nbsp;to match your local install. Likewise, the&nbsp;<code>user</code>&nbsp;setting will be unique to your installation.</p>

<h3>Using a Scheduled Command</h3>

<p>Another option for low volume sites is to schedule&nbsp;<code>queue:work</code>&nbsp;to run every minute. Or even every 5 minutes. This is best done using Laravel 5.1&rsquo;s command scheduler.</p>

<p>Edit&nbsp;<code>app/Console/Kernel.php</code>&nbsp;and make the changes below.</p>

<p>Editing Console Kernel</p>

<pre>
<code>// Replace the following method
  /**
   * Define the application's command schedule.
   *
   * @param  Schedule  $schedule
   * @return void
   */
  protected function schedule(Schedule $schedule)
  {
    // Run once a minute
    $schedule-&gt;command('queue:work')-&gt;cron('* * * * * *');
  }
</code></pre>

<p>This will run the&nbsp;<code>queue:work</code>&nbsp;command once a minute. You can change this frequency in many ways.</p>

<p>Various Run Frequencies in Console Kernel</p>

<pre>
<code>// Run every 5 minutes
$schedule-&gt;command('queue:work')-&gt;everyFiveMinutes();

// Run once a day
$schedule-&gt;command('queue:work')-&gt;daily();

// Run Mondays at 8:15am
$schedule-&gt;command('queue:work')-&gt;weeklyOn(1, '8:15');
</code></pre>

<p>To see more options view the&nbsp;<a href="http://laravel.com/docs/5.0/artisan#scheduling-artisan-commands">documentation</a>.</p>

<p>The second step in setting up the scheduled command is to modify your machine&rsquo;s crontab. Edit crontab and add the following line.</p>

<p>Crontab Line for Artisan Scheduler</p>

<pre>
<code>* * * * * php /path/to/artisan schedule:run 1&gt;&gt; /dev/null 2&gt;&amp;1
</code></pre>

<p>This will call artisan to run anything currently scheduled, sending any output to the null device.</p>

<h2>Queing Jobs</h2>

<p>Another great use for queues are asynchronous jobs. These are jobs you execute as normal with&nbsp;<code>$this-&gt;dispatch(new JobName)</code>&nbsp;from your controller, but they&rsquo;ll simply be placed in the queue to be run later by&nbsp;<code>queue:work</code>&nbsp;or whatever method is processing queue items in your application.</p>

<p>Here&rsquo;s how to do it.</p>

<p>First, when creating the job class, use the&nbsp;<code>--queued</code>&nbsp;option.</p>

<p>Example of a Queued Job</p>

<pre>
<code>~/Projects/newbeauty$ php artisan make:job --queued TestJob
Job created successfully.
</code></pre>

<p>Now, if you examine the template Laravel 5.1 created for&nbsp;<code>TestJob</code>&nbsp;you&rsquo;ll notice few small changes at the top.</p>

<p>Difference in Queued Jobs</p>

<pre>
<code>// These three use statements are new
use Illuminate\Queue\SerializesModels;
use Illuminate\Queue\InteractsWithQueue;
use Illuminate\Contracts\Queue\ShouldQueue;

// The class will also implement ShouldQueue
class TestJob extends Job implements SelfHandling, ShouldQueue
{

// And the class uses two traits
    use InteractsWithQueue, SerializesModels;
</code></pre>

<p><code>ShouldQueue</code></p>

<p>By having the&nbsp;<code>TestJob</code>class implement&nbsp;<code>ShouldQueue</code>, the&nbsp;<code>handle()</code>&nbsp;method won&rsquo;t be called. Instead,&nbsp;<code>TestJob</code>&nbsp;will be constructed and the instance will be pushed onto the queue. When the item is processed from the queue, then the&nbsp;<code>handle()</code>&nbsp;method will be called..</p>

<p><code>InteractsWithQueue</code></p>

<p>This will make several queue interaction methods available such as&nbsp;<code>$this-&gt;delete()</code>&nbsp;to delete the item from the queue or&nbsp;<code>$this-&gt;release()</code>&nbsp;to release the item back onto the queue. Normally you won&rsquo;t need these methods.</p>

<p><code>SerializesModels</code></p>

<p>When the job is serialized to be placed on the queue, this Trait will look for properties of the Job that are models and serialize them correctly.</p>

<p><strong>Queued Jobs are an excellent way to run time consuming processes which you don&rsquo;t want the user to have to wait for.</strong></p>

<h2>Recap</h2>

<p>The main thing accomplished in this chapter was adding a&nbsp;<strong>Contact</strong>&nbsp;form to the blog, but we covered several interesting topics to do it. We talked about sending mail with Mailgun and testing mail with Tinker. Several alternative routing methods were presented. And we discussed queues, set up a database queue, and sent any contact emails through the queue.</p>
