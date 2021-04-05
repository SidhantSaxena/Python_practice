c = 1
def fact(num):
    global c
    if num>0 and num!=1:
        c = c * num
        fact(num-1) 
    if num==1:
       print(c)
       
n = int(input("Enter the number : "))
fact(n)