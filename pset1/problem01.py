"""
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:
"""

count = 0
s = 'azcbobobegghakl'
for char in s:
    if char in ['a', 'e', 'u', 'o', 'i']:
        count+= 1

print("Number of vowels: ",count)
