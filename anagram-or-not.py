s1=input("Enter first string:")
s2=input("Enter second string:")
s1=s1.lower()
s2=s2.lower()
if sorted(s1)==sorted(s2):
    print("Anagram string")
else:
    print("Not Anagram")

