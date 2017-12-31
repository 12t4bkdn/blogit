<p><strong><code>Promise</code></strong>&nbsp;l&agrave; một đối tượng đặc biệt d&ugrave;ng cho c&aacute;c xử l&yacute; bất đồng bộ. N&oacute; đại diện&nbsp;cho một xử l&yacute; bất đồng bộ v&agrave; chứa kết quả cũng như c&aacute;c lỗi xảy ra&nbsp;từ xử l&yacute; bất đồng bộ đ&oacute;.</p>

<h2>C&uacute; ph&aacute;p</h2>

<pre>
new Promise(executor);
new Promise(function(resolve, reject) { ... } );</pre>

<h3>Tham số đầu v&agrave;o</h3>

<p>executor</p>

<p>Một h&agrave;m c&oacute; 2 tham số đầu v&agrave;o l&agrave;&nbsp;2 h&agrave;m phản hồi&nbsp;<code>resolve</code>&nbsp;v&agrave;&nbsp;<code>reject</code>. H&agrave;m&nbsp;<code>resolve&nbsp;</code>sẽ được gọi khi xử l&yacute; th&agrave;nh c&ocirc;ng, c&ograve;n&nbsp;<code>reject</code>&nbsp;sẽ được gọi khi xử l&yacute; thất bại.&nbsp;</p>

<p>* Ch&uacute; &yacute;: 2 h&agrave;m phản hồi n&agrave;y rất dễ bị nhầm lẫn với phong c&aacute;ch của h&agrave;m phản hồi của Node.js. Với Node.js h&agrave;m phản hồi lỗi thường l&agrave; tham số đầu ti&ecirc;n, c&ograve;n Promise th&igrave; ngược lại.</p>

<p>H&agrave;m&nbsp;<code>executor</code>&nbsp;sẽ được gọi ngay khi Promise được gọi tới, tức l&agrave; n&oacute; c&ograve;n được chạy trước cả h&agrave;m khởi tạo trả ra kết quả&nbsp;của Promise. Sau khi xử l&yacute; kết th&uacute;c t&ugrave;y theo t&igrave;nh huống m&agrave; h&agrave;m phản hồi&nbsp;<code>resolve</code>&nbsp;hoặc&nbsp;<code>reject</code>&nbsp;sẽ được gọi tới. Trường hợp xử l&yacute; th&agrave;nh c&ocirc;ng th&igrave; h&agrave;m&nbsp;<code>resolve</code>&nbsp;sẽ được gọi tới để trả ra kết quả. C&ograve;n trường hợp thất bại th&igrave; h&agrave;m&nbsp;<code>reject</code>&nbsp;sẽ được gọi tới để trả ra m&atilde; lỗi thực thi.</p>

<h2>M&ocirc; tả</h2>

<p>Một&nbsp;<code><strong>Promise</strong></code>&nbsp;c&oacute; thể như một proxy đại diện cho một gi&aacute; trị m&agrave; ta kh&ocirc;ng cần phải biết ngay khi khởi tạo. Bằng c&aacute;c sử dụng&nbsp;<code><strong>Promise</strong></code>&nbsp; ta c&oacute; thể kết hợp với c&aacute;c h&agrave;m xử l&yacute; kh&aacute;c để sử dụng kết quả sau khi thực thi xử l&yacute; bất đồng bộ m&agrave; n&oacute; đang đại diện. V&igrave; vậy m&agrave; ta c&oacute; thể lập tr&igrave;nh bất đồng bộ gần giống với kiểu lập tr&igrave;nh đồng bộ - tức l&agrave; đợi xử l&yacute; bất đồng bộ xong mới thực thi c&aacute;c thao t&aacute;c m&agrave; cần sử dụng tới kết quả của xử l&yacute; đ&oacute;. Để c&oacute; thể l&agrave;m được việc đ&oacute; thay v&igrave; trả ra kết quả của việc xử l&yacute; đồng bộ,&nbsp;<code><strong>Promise</strong></code>&nbsp; sẽ trả ra một&nbsp;<em>promise</em>kh&aacute;c. Bằng promise mới n&agrave;y ta lại c&oacute; thể lặp lại việc sử dụng kết quả của thao t&aacute;c xử l&yacute; l&uacute;c trước để l&agrave;m đầu v&agrave;o cho c&aacute;c thao t&aacute;c xử l&yacute; l&uacute;c sau.</p>

<p>Tại mỗi thời điểm&nbsp;<code>Promise</code>&nbsp;sẽ c&oacute; thể ở một trong c&aacute;c trạng th&aacute;i sau:</p>

<ul>
	<li><em>pending</em>: Trạng th&aacute;i chờ xử l&yacute; kết th&uacute;c. Trạng th&aacute;i n&agrave;y ch&iacute;nh l&agrave; trạng th&aacute;i ban đầu của Promise, n&oacute; thể hiện rằng thao t&aacute;c xử l&yacute; của ta chưa kết th&uacute;c.</li>
	<li><em>fulfilled</em>: Trạng th&aacute;i xử l&yacute; th&agrave;nh c&ocirc;ng. Trạng th&aacute;i n&agrave;y thể hiện rằng thao t&aacute;c xử l&yacute; của ta đ&atilde; kết th&uacute;c v&agrave; th&agrave;nh c&ocirc;ng.</li>
	<li><em>rejected</em>: Trạng th&aacute;i xử l&yacute; thất bại. Trạng th&aacute;i n&agrave;y thể hiện thao t&aacute;c xử l&yacute; đ&atilde; kết th&uacute;c v&agrave; thất bại.</li>
</ul>

<p>Như vậy một Promise khi ở trạng th&aacute;i pending sẽ được chuyển th&agrave;nh trạng th&aacute;i&nbsp;<em>fulfilled</em>&nbsp;với kết quả th&agrave;nh c&ocirc;ng hoặc trạng th&aacute;i&nbsp;<em>rejected</em>&nbsp;k&egrave;m với m&atilde; lỗi xảy ra khi xử l&yacute; kết th&uacute;c. Sau khi xử l&yacute; kết th&uacute;c, bất kể trạng th&aacute;i được chuyển th&agrave;nh l&agrave; th&agrave;nh c&ocirc;ng hay thất bại th&igrave; c&aacute;c h&agrave;m xử l&yacute; được đ&iacute;nh k&egrave;m sẽ được gọi thực thi. Để đ&iacute;nh k&egrave;m một h&agrave;m cho Promise, ta c&oacute; thể sử dụng&nbsp;<code><a href="https://developer.mozilla.org/vi/docs/Web/JavaScript/Reference/Global_Objects/Promise/then"><code>Promise.prototype.then()</code></a></code>&nbsp;cho trường hợp th&agrave;nh c&ocirc;ng v&agrave;&nbsp;<code><a href="https://developer.mozilla.org/vi/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch"><code>Promise.prototype.catch()</code></a>&nbsp;cho trường hợp xử l&yacute; thất bại.</code></p>

<p><code>H&agrave;m đ&iacute;nh k&egrave;m xử l&yacute;&nbsp;<a href="https://developer.mozilla.org/vi/docs/Web/JavaScript/Reference/Global_Objects/Promise/then"><code>Promise.prototype.then()</code></a></code>&nbsp;v&agrave;&nbsp;<code><a href="https://developer.mozilla.org/vi/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch"><code>Promise.prototype.catch()</code></a></code>&nbsp;sẽ trả ra một promise kh&aacute;c n&ecirc;n thao t&aacute;c hậu xử l&yacute; bằng h&agrave;m đ&iacute;nh k&egrave;m c&oacute; thể được chuyển tiếp kiểu xử l&yacute; chuỗi (chained). Cụ thể hơn ta c&oacute; thể xem h&igrave;nh dưới đ&acirc;y.</p>

<p><img alt="" src="https://mdn.mozillademos.org/files/8633/promises.png" style="height:auto !important; margin:0px" /></p>

<p>Như h&igrave;nh minh họa hoạt động của Promise tr&ecirc;n, ta c&oacute; thể thấy khi khởi tạo Promise sẽ c&oacute; trạng th&aacute;i l&agrave; pending. Sau khi xử l&yacute; kết th&uacute;c, t&ugrave;y theo kết quả xử l&yacute; m&agrave; trạng th&aacute;i sẽ l&agrave; fullfil hoặc reject. L&uacute;c đ&oacute; c&aacute;c h&agrave;m đ&iacute;nh k&egrave;m sẽ được thực thi th&ocirc;ng qua h&agrave;m&nbsp;<code><a href="https://developer.mozilla.org/vi/docs/Web/JavaScript/Reference/Global_Objects/Promise/then"><code>Promise.prototype.then()</code></a></code>&nbsp;hoặc&nbsp;<code><a href="https://developer.mozilla.org/vi/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch"><code>Promise.prototype.catch()</code></a></code>. Ch&iacute;nh c&aacute;c h&agrave;m n&agrave;y lại trả ra một Promise kh&aacute;c n&ecirc;n ta c&oacute; thể xử l&yacute; một loạt c&aacute;c thao t&aacute;c ph&iacute;a sau một c&aacute;ch chuyển tiếp.</p>

<p>&nbsp;</p>

<p><strong>Đừng nhầm lẫn với:</strong>&nbsp;một số ng&ocirc;n ngữ kh&aacute;c như Scheme&nbsp;cũng c&oacute; kh&aacute;i niệm&nbsp;&ldquo;promises&rdquo; - nhưng kh&aacute;i niệm n&agrave;y để chỉ thị một thao t&aacute;c được gọi thực thi sau. C&ograve;n, Promises trong JavaScript biểu diễn c&aacute;c thao t&aacute;c bất đồng bộ m&agrave; đ&atilde; được thực thi (thao t&aacute;c bất đồng bộ n&agrave;y được gọi ngay khi ta gọi Promise - ngay cả trước khi h&agrave;m khởi tạo của Promise được gọi tới)&nbsp;v&agrave; c&oacute; thể đ&iacute;nh k&egrave;m c&aacute;c h&agrave;m hậu xử l&yacute; sau khi xử l&yacute; bất đồng bộ m&agrave; n&oacute; biểu diễn kết th&uacute;c. Nếu bạn muốn d&ugrave;ng c&aacute;c thao t&aacute;c kiểu thi sau như vậy th&igrave; c&oacute; thể sử dụng h&agrave;m mũi t&ecirc;n (<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions">arrow function</a>) kh&ocirc;ng c&oacute; tham số đầu v&agrave;o, như:&nbsp;<code>f = () =&gt;&nbsp;<em>expression</em></code>&nbsp;để tạo một h&agrave;m được gọi sau, v&agrave; sử dụng&nbsp;<code>f()</code>&nbsp;để thực thi n&oacute;.</p>

<p><strong>Lưu &yacute;</strong>: Promise được gọi kết th&uacute;c (<em>settled)&nbsp;</em>khi v&agrave; chỉ khi n&oacute; ở trạng th&aacute;i&nbsp;fulfilled (th&agrave;nh c&ocirc;ng) hoặc&nbsp;rejected (thất bại). Đ&ocirc;i l&uacute;c c&oacute; thể bạn thấy đ&acirc;u đ&oacute; n&oacute;i rằng Promise được giải quyết xong&nbsp;(<em>resolved)</em>&nbsp;để &aacute;m chỉ rằng Promise được kết th&uacute;c, l&uacute;c đ&oacute; đừng nhầm lẫn l&agrave; n&oacute; được kết th&uacute;c th&agrave;nh c&ocirc;ng v&igrave; n&oacute; chỉ đơn giản l&agrave; n&oacute;i tới Promise đ&atilde; được kết th&uacute;c m&agrave; th&ocirc;i. Để biết r&otilde; hơn về c&aacute;c thuật ngữ li&ecirc;n quan tới Promise, bạn c&oacute; thể tham khảo b&agrave;i viết n&agrave;y:&nbsp;<a href="https://github.com/domenic/promises-unwrapping/blob/master/docs/states-and-fates.md">States and fates</a>.</p>

<h2>Thuộc t&iacute;nh</h2>

<p><code>Promise.length</code></p>

<p>Thuộc t&iacute;nh length n&agrave;y lu&ocirc;n c&oacute; gi&aacute; trị l&agrave; 1&nbsp;(số lượng của tham số khởi tạo).</p>

<p><a href="https://developer.mozilla.org/vi/docs/Web/JavaScript/Reference/Global_Objects/Promise/prototype"><code>Promise.prototype</code></a></p>

<p>Biểu diễn prototype cho h&agrave;m khởi tạo&nbsp;<code>Promise</code>.</p>

<h2>Phương thức</h2>

<p><a href="https://developer.mozilla.org/vi/docs/Web/JavaScript/Reference/Global_Objects/Promise/all"><code>Promise.all(iterable)</code></a></p>

<p>Phương thức n&agrave;y được sử dụng khi ta cần đợi một tập c&aacute;c Promise kết th&uacute;c. Trả ra một promise đại diện cho tất cả c&aacute;c kết quả thu được từ c&aacute;c promise nằm trong iterable sau khi tất cả c&aacute;c promise n&agrave;y kết th&uacute;c xử l&yacute; th&agrave;nh c&ocirc;ng. Hoặc, trả ra một promise đại diện cho lỗi thực thi ngay khi một promise n&agrave;o đ&oacute; kết th&uacute;c lỗi, khi đ&oacute; promise được trả ra cũng sẽ ở trạng th&aacute;i lỗi.&nbsp;Khi tất cả c&aacute;c promise trong iterable kết th&uacute;c th&agrave;nh c&ocirc;ng th&igrave; promise trả ra cũng ở trạng th&aacute;i th&agrave;nh c&ocirc;ng với kết quả l&agrave; một mảng chứa tất cả c&aacute;c kết quả của c&aacute;c promise đ&atilde; thực thi theo đ&uacute;ng thứ tự trong iterable. C&ograve;n khi một promise n&agrave;o đ&oacute; xảy ra lỗi th&igrave; promise được trả ra cũng sẽ ở trạng th&aacute;i lỗi v&agrave; chứa m&atilde; lỗi của promise đầu ti&ecirc;n g&acirc;y lỗi đ&oacute;.</p>

<p><a href="https://developer.mozilla.org/vi/docs/Web/JavaScript/Reference/Global_Objects/Promise/race"><code>Promise.race(iterable)</code></a></p>

<p>Trả ra một promise ngay sau khi một trong c&aacute;c promise trong iterable kết th&uacute;c xử l&yacute;. Tức l&agrave; d&ugrave; kết quả thu được l&agrave; lỗi hay th&agrave;nh c&ocirc;ng th&igrave; ta cũng sẽ trả ngay ra một promise mới v&agrave; promise mới n&agrave;y sẽ chứa kết quả của promise được kết th&uacute;c đầu ti&ecirc;n.</p>

<p><a href="https://developer.mozilla.org/vi/docs/Web/JavaScript/Reference/Global_Objects/Promise/reject"><code>Promise.reject(reason)</code></a></p>

<p>Trả ra một promise trạng th&aacute;i lỗi với m&atilde; lỗi m&agrave; h&agrave;m xử l&yacute; trả ra. H&agrave;m n&agrave;y sẽ được gọi tới khi h&agrave;m xử l&yacute; của ta bị lỗi (thất bại).</p>

<p><a href="https://developer.mozilla.org/vi/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve"><code>Promise.resolve(value)</code></a></p>

<p>Trả ra một promise th&agrave;nh c&ocirc;ng với kết quả m&agrave; h&agrave;m xử l&yacute; trả ra.&nbsp;</p>

<h2>Nguy&ecirc;n mẫu&nbsp;<code>Promise</code></h2>

<h3>Thuộc t&iacute;nh</h3>

<p><code>Promise.prototype.constructor</code></p>

<p>Returns the function that created an instance&#39;s prototype. This is the&nbsp;<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise"><code>Promise</code></a>&nbsp;function by default.</p>

<h3>Phương thức</h3>

<p><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch"><code>Promise.prototype.catch(onRejected)</code></a></p>

<p>Appends a rejection handler callback to the promise, and returns a new promise resolving to the return value of the callback if it is called, or to its original fulfillment value if the promise is instead fulfilled.</p>

<p><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then"><code>Promise.prototype.then(onFulfilled, onRejected)</code></a></p>

<p>Appends fulfillment and rejection handlers to the promise, and returns a new promise resolving to the return value of the called handler, or to its original settled value if the promise was not handled (i.e. if the relevant handler&nbsp;<code>onFulfilled</code>&nbsp;or&nbsp;<code>onRejected</code>&nbsp;is not a function).</p>

<p><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally"><code>Promise.prototype.finally(onFinally)</code></a></p>

<p>Appends a handler to the promise, and returns a new promise which is resolved when the original promise is resolved. The handler is called when the promise is settled, whether fulfilled or rejected.</p>
