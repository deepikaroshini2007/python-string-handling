s=input(&quot;Enter a pattern :&quot;)
res=&quot;&quot;
for i in range(0,len(s),2):
char = s[i]
num = int(s[i+1])
res=res+char*num
print(&quot;Output:&quot;,res)
