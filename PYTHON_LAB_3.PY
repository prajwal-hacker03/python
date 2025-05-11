import math  
def mean(data): 
    n=len(data) 
    mean=sum(data)/n 
    return mean 
def variance(data): 
    n=len(data) 
    mean=sum(data)/n 
    deviations=[(x-mean)**2 for x in data] 
    variance=sum(deviations)/n 
    return variance 
def stdev(data): 
    var=variance(data) 
    std_dev=math.sqrt(var) 
    return std_dev 
listA=[] 
n=int(input("enter the number of elements:")) 
for i in range(0,n): 
    element=int(input()) 
    listA.append(element) 
print(listA) 
data=listA 
print("Mean of the sample is % s " % (mean(data))) 
print("variance of the sample is % s " % (variance(data)))  
print("Standard Deviation of the sample is % s "% (stdev(data)))