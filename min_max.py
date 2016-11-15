import sys

doit=True

a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]


lst=[]
lst.append(a)
lst.append(b)
lst.append(c)
lst.append(d)
lst.append(e)

lst.sort()

for i in range(0,len(lst)):
    if lst[i]<1 or lst[i]>10**9:
        print ("out of range")
        doit=False
if doit:
    min=lst[0]+lst[1]+lst[2]+lst[3]
    max=lst[1]+lst[2]+lst[3]+lst[4]
    print (min,max)