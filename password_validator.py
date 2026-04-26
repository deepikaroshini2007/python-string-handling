password=input(&quot;Enter password:&quot;)

digit=0
lower= 0
upper= 0
special = 0
if len(password)&lt;8 or len(password)&gt;15:
print(&quot;invalid password&quot;)
elif &quot; &quot; in password:
print(&quot;Invalid password&quot;)
else:
for ch in password:
if ch.isdigit():
digit=1
elif ch.isupper():
upper=1
elif ch.islower():
lower=1
else:
special=1
if digit==1 and lower==1 and upper==1 and special==1:
print(&quot;Valid password&quot;)
else:
print(&quot;Invalid password&quot;)
