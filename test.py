def f(n):
    if n<2:
        return False
    x=2
    while x<n:
        if n%x==0:
            return False
        x=x+1
    return True


for i in range(20):
    print(str(i)+" "+str(f(i)))