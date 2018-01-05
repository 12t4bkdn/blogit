<pre>
<code class="language-python">#Nhap vao mot chuoi chua ngay thang nam sinh
#Kiem tra neu nguoi do duoi hay tren hay du 18 tuoi( Chinh xac den ngay)

from datetime import datetime

now = datetime.now()
birthday_str = "05/01/2000"
birthday = datetime.strptime(birthday_str, '%d/%m/%Y')
current_day = (now.year, now.month, now.day)
birth_day = (birthday.year + 18, birthday.month, birthday.day)

if current_day &gt; birth_day :
    print "Em tren 18"
elif current_day &lt; birth_day:
    print "Em chua 18"
else: 
    print "Em du 18"</code></pre>

<p>&nbsp;</p>
