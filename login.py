#password = "Pulkit8878"     #login succesful
password = input("Enter your Password: ")         #length is so short  

if len(password) < 8 :
    print("At least Eight Character")

elif password.isalnum():
    print("Add Somes Number")

elif password.isalpha():
    print("Add Somes Alphabetical Character")

else:
    print("Login Succesful")