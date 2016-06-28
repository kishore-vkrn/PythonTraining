s = raw_input()
#print s
length = len(s)
#print length
half = length/2
#print half
first = s[:half]
#print first
second = s[half:]
#print second
result = first+second.upper()
print result
