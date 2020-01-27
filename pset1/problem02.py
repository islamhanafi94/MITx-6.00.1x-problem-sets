"""
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
"""
count = 0
s = 'azcbobobegghakl'
for i in range(0,len(s)-3):
    str_bob = s[i]+s[i+1]+s[i+2]
    if "bob" == str_bob:
        count += 1

print("Number of times bob occurs is: ", count)

# Another Solution
count = 0
s = 'azcbobobegghakl'
sub_string = 'bob'
for i in range(len(s)):
    if s.startswith(sub_string,i):
        count+=1

print("Number of times bob occurs is: ", count)
