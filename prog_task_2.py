my_file=open("added crime.csv")
line=my_file.readline()
each_line=line.split()
for word in each_line:
 Assault_count=0 
 Robbery_count=0 
 if word= "Assault":
    Assault_ count+=1
 
 else :
 if word= "Robbery": 
   Robbery_ count+=1
   
print( "Asault " , 1430 , Assault_count)
print( "Robbery " , 2142 ,Robbery _count)

