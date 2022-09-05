#creating a dictionary
college = {
"name": "gcoea",

"grade": "a++",

"id": 1001

}

print(college)

#adding items to dictionary

college["location"] = "amt"

print(college)

#changing values of a key

college["location"] = "Amravati"

print(college)

#to remove items use pop() 
college.pop("grade") 
print(college)

#know the length using len() 
print("length of college is:",len(college)) 

#to copy the same dictionary use copy() 
mycollege= college.copy() 
print(mycollege)
