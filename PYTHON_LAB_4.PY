n=input("Enter number:") 
num =int(n) 
print("Digit\t occurence") 
for i in range(0,10): 
   count=0 
   temp=num 
   while(temp>0): 
      a=temp%10 
      if a==i: 
         count=count+1 
      temp=temp//10 
   if count>0: 
      print(i,"\t",count)