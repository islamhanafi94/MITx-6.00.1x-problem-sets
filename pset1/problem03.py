"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. For example, if s = 'azcbobobegghakl', 
then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. 

For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc         
"""
s = 'abcdefghijklmnopqrstuvwxyz'
savedRecords = []
startIndex = 0
count = 0

for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        count += 1 
    else:
        savedRecords.append(s[startIndex:startIndex+count+1])
        startIndex = i+1
        count = 0

# appending last record
savedRecords.append(s[startIndex:startIndex+count+1])

print('Longest substring in alphabetical order is: ', max(savedRecords,key=len))

