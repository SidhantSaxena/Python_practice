str1 = input()
str1.lower()
llist=["a","e","i","o","u"]
count1=[]
count2=[]
for i in str1:
    if i in llist:
       count1.append(i)
for j in llist:
   n = count1.count(j)
   count2.append(n)
print(sum(count2))   
   
    
    
        
