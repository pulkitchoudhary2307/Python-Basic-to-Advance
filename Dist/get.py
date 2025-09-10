"""profile_1 = {
    'name' : "pulkit" , 'sirname' : "choudhary" , 'age': 21
}

find = profile_1.get("age")
print(find)

profile_2 = {
    'name' : "pulkit" , 'sirname' : "choudhary" , 'age': 21
}

find = profile_2.get("Umer","NOT FOUND")
print(find)



#Only Key are find
profile_3 = {
    'name' : "pulkit" , 'sirname' : "choudhary" , 'age': 21
}

keys_1  = profile_3.keys()
print(list(keys_1))



#Only values are find
profile_3 = {
    'name' : "pulkit" , 'sirname' : "choudhary" , 'age': 21
}

keys_1  = profile_3.values()
print(list(keys_1))


#Only values and keys are find
profile_3 = {
    'name' : "pulkit" , 'sirname' : "choudhary" , 'age': 21
}

keys_1  = profile_3.items()
print(list(keys_1))
"""

#clear all dict
profile_4 = {
    'name' : "pulkit" , 'sirname' : "choudhary" , 'age': 21
}

print(profile_4)
cleared = profile_4.clear()
print(cleared)
print(profile_4)