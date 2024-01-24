s='!'
t='~'
j=0
for i in range(ord(s),ord(t)+1):
    hx=hex(i)
    j=j+1
    print(hx,end=' ')
    if(j%5==0):
        print()
        