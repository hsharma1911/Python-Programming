n = eval(input(""))
a = list(eval(input("")))
for i in range(0,n):
    c=0
    for j in range(0,n):
        if a[i]==a[j]:
            c+=1
        if c==3:
            print(a[i])