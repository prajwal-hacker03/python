def factorial(z): 
   if z==1:
      return 1 
   else: 
       return z* factorial(z-1) 
def binomial_coefficient(n,k): 
   a= (factorial(n)) / (factorial(k) * factorial(n-k)) 
   return a 
n=int(input("enter the number")) 
k=int(input('enter the r value:')) 
print("The Factorial of a number is :",factorial(n)) 
print("The binomial coefficient is:",binomial_coefficient(n,k))   