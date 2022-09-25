s = ' hello '
print(s[:]) #substing through brancket notation but we still get leading and trailing spaces.
print(s[1:-1]) # We could use start and stop
print(s.strip())

s1 = '###farhad###'
print(s1.strip('#'))
s2 = 'www.example.com'
print(s2.strip('wcom.')) # Removing every single occurance of each character supplied to strip() method.

s3 = '\n \t welcome \n \t'
print(s3.strip('\n'))

s4 = 'Name : Netherlands'.lstrip('Name :')
print(s4)
#s5 = 'Name : England'.removeprefix('Name :')
#print(s5)
#s6 = 'Name : England'.removesuffix('Name :')
#print(s6)
s7 = 'string methods in python'.replace(' ', '-')
print(s7)
s8 = 'string      methods in python'.replace(' ', '-')
print(s7)

s8 = 'string methods in python'.split()
print(s8)
# We could is comma as split separator
s9 = 'string, methods in python'.split(',')
print(s9)
s10 = 'string methods in python'.split(' ', maxsplit=1)
print(s10)