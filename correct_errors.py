def capitalize(s):
    l=[]
    s=s.strip()
    for i in s:
        l.append(i)
    l[0]=l[0].upper()
    for j in range(len(l)-2):
        if l[j]=='.' or l[j]=='!' or l[j]=='?':
            l[j+2]=l[j+2].upper()
    return ''.join(l)
