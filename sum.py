import math

s = input()
l = []

while ('+' in s) or ('-' in s):
    if '+' in s:
        s = s.replace('+',' ',1)
        l.append('+')
    if '-' in s:
        s = s.replace('-',' ',1)
        l.append('-')

s = s.split()
for i in range(len(s)):
    s[i] = math.floor(float(s[i]))

while l != []:
    if l[0] == '-':
        s[0] = s[0] - s[1]
        l.pop(0)
        s.pop(1)
    else:
        s[0] = s[0] + s[1]
        l.pop(0)
        s.pop(1)

print(''.join(str(s[0])))







