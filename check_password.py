def check_password(password):
    c=0
    if len(password)>=8:
        c+=1
    if len(set(password))>len(set(password.upper())):
        c+=1
    a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for i in range(10):
        if str(a[i]) in password:
            c+=1
            break
    if c==3:
        return True
    else:
        return False
