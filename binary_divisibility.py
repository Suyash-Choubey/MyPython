def negative(num):
    if num<0:
        return True
    
def not_binary(num):
    while num>0:
        rem=num%10
        num=num//10
        
        if rem!=0 and rem!=1:
            return True
    
def divisible(n,d):
    rev=rem=0
    
    n=n*10+1
    
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    
    rem2=0
    
    while rev>1:
        a=rev%10
        rev=rev//10
        
        if a==0:
            rem2=rem2*2
            
        else:
            rem2=rem2*2+1
        if rem2>=d:
            rem2=rem2-d
            
    if rem2==0:
        return True
    else:
        return False
    
bnum=int(input("enter a binary number:"))
div=int(input("enter divisor:"))

if negative(bnum):
    print ("Do not use negative sign.")
elif not_binary(bnum):
    print (bnum,"is not a binary number")
else:
    if divisible(bnum,div):
        print (bnum,"is divisible by",div)
    else:
        print (bnum,"is not divisible by",div)