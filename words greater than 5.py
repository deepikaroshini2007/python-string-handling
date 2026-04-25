s=input(&quot;enter a sentence:&quot;)
words=s.split()
print(&quot;WORDS GREATER THAN 5&quot;)
for i in words:
if len(i)&gt;5:
print(i)
