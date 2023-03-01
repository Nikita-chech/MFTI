def check_password(password):
    c=0
    if len(password)>=8:
        c+=1
    l2=[]
    l1=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(len(l1)):
        l2.append(str(i).upper())
    for i in range(len(l1)):
        if l1[i] in password:
            c+=1
            break
    for i in range(len(l1)):
        if l2[i] in password:
            c+=1
            break
    a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for i in range(10):
        if str(a[i]) in password:
            c+=1
            break
    if c==4:
        return True
    else:
        return False
