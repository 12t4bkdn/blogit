<ul>
	<li>Arrow function</li>
</ul>

<pre>
<code class="language-javascript">var domain = ["freetuts.net", 'qa.freetuts.net', 'demo.freetuts.net'];
 
domain.map((val, key) =&gt; {
    console.log(val.toUpperCase());
});</code></pre>

<ul>
	<li>Variables, loops</li>
</ul>

<pre>
<code class="language-javascript">// Array
let date = [10, 03, 2016]
 
// Chuyển ba giá trị vào ba biến d, m, y
let [d, m, y] = date;
 
// In kết quả
console.log("Day: " + d);   // Day: 10
console.log("Month: " + m); // Month: 03
console.log("Year: " + y);  // Year : 2016
</code></pre>

<p>&nbsp;</p>

<pre>
<code class="language-javascript">var domains = [
    'abc.net',
    'google.com',
    'facebook.com'
];
 
for (domain of domains){
    const message = "Domain " + domain;
    console.log(message);
}</code></pre>

<ul>
	<li>Set</li>
</ul>

<pre>
<code>let numbers = new Set([1, 2, 3, 4]);
 
let arr_numbers = [...numbers];
 
// Lúc này  biến arr_numbers sẽ là một mảng gồm 4 phần tử 
// [1, 2, 3, 4]
</code></pre>

<p>&nbsp;</p>

<pre>
<code>let set = new Set([1, 2, 3]);
let arr = [...set].map(function(x){
    return x * 2;
});
 
console.log(set); // Set(1, 2, 3)
console.log(arr); // [2, 4, 6]</code></pre>

<p>&nbsp;</p>

<pre>
<code>let set = new Set([1, 2, 3]);
 
// Lấy các số chẵn
let arr = [...set].filter(function(x){
    return (x % 2) == 0;
});
 
console.log(set); // Set(1, 2, 3)
console.log(arr); // [2]
</code></pre>

<ul>
	<li>Map</li>
</ul>

<pre>
<code>// Tạo một map gồm 3 thông tin
 let map = new Map([
     ["Name", "Nguyen Van Cuong"],
     ["Email", "thehalfheart@gmail.com"],
     ["Website", "freetuts.net"]
]);
 
console.log(map);
// Map {"Name" =&gt; "Nguyen Van Cuong", "Email" =&gt; "thehalfheart@gmail.com", "Website" =&gt; "freetuts.net"}
</code></pre>

<p>&nbsp;</p>

<pre>
<code>let map = new Map();
  
map.set('Name', 'Nguyen Van Cuong');
 
console.log(map);
// Map {"Name" =&gt; "Nguyen Van Cuong"}
 
map.delete("Name");
 
console.log(map);
// Map {}

console.log(map.has('domain')); // False
//console.log(map.has('Name')); // True
</code></pre>

<p>&nbsp;</p>

<pre>
<code>// Xử lý
for (var key of map.keys())
{
    console.log(key);
}

// Xử lý
for (var value of map.values())
{
    console.log(value);
}

// Xử lý
for (var entry of map.entries())
{
    console.log(entry[0] + ' - ' + entry[1]);
}

// Xử lý
for (var [key, value] of map)
{
    console.log(key + ' - ' + value);
}
 
// Xử lý
map.forEach((value, key) =&gt; {
    console.log(key + ' - ' + value);
});</code></pre>

<p>&nbsp;</p>

<pre>
<code>// Giá trị ban đầu
let map = new Map()
    .set(1, 'a')
    .set(2, 'b')
    .set(3, 'c')
    .set(4, 'd')
    .set(5, 'e');
     
// Chuyển đổi
let map1 = new Map(
        [...map].map(
            ([key, value]) =&gt; [key, key + '-' + value]
        )
);
 
console.log(map1); 
// Kết quả: Map {1 =&gt; "1-a", 2 =&gt; "2-b", 3 =&gt; "3-c", 4 =&gt; "4-d", 5 =&gt; "5-e"}
</code></pre>

<p>&nbsp;</p>

<pre>
<code>// Giá trị ban đầu
let map = new Map()
    .set(1, 'a')
    .set(2, 'b')
    .set(3, 'c')
    .set(4, 'd')
    .set(5, 'e');
     
// Chuyển đổi
let map1 = new Map(
        [...map].filter(
            ([key, value]) =&gt; key % 2 == 0
        )
);
 
console.log(map1); 
// Kết quả: Map {2 =&gt; "b", 4 =&gt; "d"}</code></pre>

<ul>
	<li>WeakMap</li>
</ul>

<pre>
<code>// Khởi tạo
var weak = new WeakMap();
 
// Danh sách key 
var key1 = {};
var key2 = {};
 
// Thêm phần tử
weak.set(key1, "Giá trị 01");
weak.set(key2, "Giá trị 02");
 
// Lấy giá trị
console.log(weak.get(key1)); // Giá trị 01
console.log(weak.get(key2)); // Giá trị 02
 
// Kiểm tra tồn tại
var other_key = {};
console.log(weak.has(key1)); // true
console.log(weak.has(other_key)); // false
 
// Xóa phần tử
weak.delete(key1);
console.log(weak.get(key1)); // Undefined</code></pre>

<ul>
	<li>Promise</li>
</ul>

<pre>
<code>var promise = new Promise(function(resolve, reject){
    reject('Error!');
    resolve('Success!');
});
 
 
promise.then(
    function(success){
        console.log(success);
    },
    function(error){
        console.log(error);
    }
);</code></pre>

<ul>
	<li>Iterator</li>
</ul>

<pre>
<code>let arr = ['a', 'b', 'c'];
 
var iterator = arr[Symbol.iterator]();
 
console.log(iterator.next());   // a
console.log(iterator.next());   // b
console.log(iterator.next());   // c
console.log(iterator.next());   // undefined</code></pre>

<ul>
	<li>async/await
	<ul>
		<li>callback</li>
		<li>promise</li>
		<li>sync/await</li>
	</ul>
	</li>
</ul>

<pre>
<code>function wait(ms, cb) {
   setTimeout(cb, ms)
}

function main() {
   console.log('sắp rồi...')
   wait(2007, () =&gt; {
     console.log('chờ tí...')
     wait(2012, () =&gt; {
       console.log('thêm chút nữa thôi...')
       wait(2016, () =&gt; {
         console.log('xong rồi đấy!')
       })
     })
   })
}</code></pre>

<pre>
<code>function wait(ms) {
   return new Promise(r =&gt; setTimeout(r, ms))  
}

function main() {
   console.log('sắp rồi...')
   wait(2007).then(() =&gt; {
     console.log('chờ tí...')
     return wait(2007)
   }).then(() =&gt; {
     console.log('thêm chút nữa thôi...')
     return wait(2012)
   }).then(() =&gt; {
      console.log('thêm chút nữa thôi...')
     return wait(2016)
   }).then(() =&gt; {
     console.log('xong rồi đấy!')
   })
}</code></pre>

<pre>
<code>function wait(ms) {
   return new Promise(r =&gt; setTimeout(r, ms))  
}

async function main() {
   console.log('sắp rồi...')
   await wait(2007)
   console.log('chờ tí...')
   await wait(2012)
   console.log('thêm chút nữa thôi...')
   await wait(2016)
   console.log('xong rồi đấy!')
}</code></pre>

<pre>
<code>function wait(ms) {
   if (ms &gt; 2000) throw new Error(ms)
   return new Promise(r =&gt; setTimeout(r, ms))
}

async function main() {
   const dur = [1000, 2000, 3000, 4000]
   let all = dur.map(ms =&gt; wait(ms))
   try {
     await Promise.all(all)
     console.log('Promise.all - done')
   } catch (e) {
     console.error('Promise.all:', e)  
   }

   let each = dur.map(ms =&gt; wait(ms))
   each.forEach(async (func, index) =&gt; {
     try {
       await func
       console.log('each - done:', dur[index])
     } catch (e) {
       console.error('each:', e)  
     }
   })
}</code></pre>

<p>&nbsp;</p>
