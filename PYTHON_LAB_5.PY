file=open("sample.txt") #mention location of file  
text=file.read() 
print(text) 
words=text.split() 
frequency={} 
for word in words: 
    if word not in frequency: 
      frequency[word]=1 
    else: 
      frequency[word]+=1 
most_frequency=dict(sorted(frequency.items(),key=lambda 
elem:elem[1],reverse=True)) 
out=dict(list(most_frequency.items())[0:10]) 
print("1st 10 most frequent words are"+str(out))