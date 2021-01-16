#simple sorting trick of python



a={3,2,4,5,3,4,5,6}
c=[]

for i in range(len(a)):
  ss=min(a)
  a.remove(ss)
  c.append(ss)

print(c)
  
  





    
    