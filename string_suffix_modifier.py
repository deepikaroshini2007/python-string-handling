s=input(&quot;Enter a string :&quot;)
if len(s)&gt;=3:
if s.endswith(&quot;ing&quot;):
s=s+&quot;ly&quot;
else:
s=s+&quot;ing&quot;
print(&quot;Result :&quot;,s)
