#empty dictionary without elements
#key can't be changed
#to access elemets in list you need index value

person = {}  
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

# print(person)

# print(person["children"]) #get back list; can use "type" to figure that out

# print(person["children"][1])

# print(person["pets"]["cat"])

for i in person["children"]:
    print(i)

# for x in person["pets"]:
#     print(person["pets"][x])

# for x in person["pets"]:
#     print(person(["pets"]["dog"])

