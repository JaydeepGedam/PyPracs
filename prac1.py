id1 = id("Jaydeep")
id2 = id(404)
mylist = ["Jay", "JD", "Jaydeep","Jay"]
id3 = id(mylist[0])
id4 = id(mylist[2])
id5 = id(mylist[3])

# Displaying result  
print("\nJaydeep  :",id1)  
print("404      :",id2)  
print("listobj1 :",id3)  
print("listobj2 :",id4)  
print(id3==id4)  
print(id3==id5,"\n")  

type1 = type("Jaydeep")
type2 = type(404)
mylist = ["Jay", "JD", "Jaydeep"]
type3 = type(mylist[0])
type4 = type(mylist[2])

# Displaying result  
print("\nJaydeep  :",type1)  
print("404      :",type2)  
print("listobj1 :",type3)  
print("listobj2 :",type4,"\n")  