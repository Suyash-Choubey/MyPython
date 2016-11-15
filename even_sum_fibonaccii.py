#!/bin/python3

import sys


tsum=[]
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a=1
    b=2
    lst = [1, 2]
    i = 0
    sum=0
    while i<n:

        c=a+b
        i=c
        lst.append(c)
        a=b
        b=c
    lst.remove(lst[len(lst)-1])
    for k in lst:
        if k%2==0:
            sum=sum+k
    tsum.append(sum)

for j in tsum:
    print (j)

