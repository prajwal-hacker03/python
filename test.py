USN=input("Enter usn")
name=input("Enter name:")
print("Enter the marks of 3 subjcts")
marks=[321]
m=int(input("Enter the marks:"))
marks.append((m))
print(marks)
total=sum(marks)
per=int(100*total)/300
print(USN,name,total)
           