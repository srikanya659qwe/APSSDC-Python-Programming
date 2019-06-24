#Function to check given no is prime or not

def ischeck(n):
    flag=1
    if n == 2:
        return True
    for i in range(2,n//2 + 1):
        if n % i== 0:
            flag= 0
            return False
    if flag == 1:
        return True



#Primefactors

def numberprimefactors(n):
    if ischeck(n):
        return 1
    count=0
    for i in range(2,n // 2+1):
        if ischeck(i) and n % i==0:
            count=count+1
    return count

