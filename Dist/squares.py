squares = {x : x*x for x in range(1,6)}
print(squares)

#Nested Dict 

programing = {
        "python" : {"name":"python","used_case" :["ai","ml","data science"]},
        "java" : {"name":"java","used_case" :["apple web"]}
        
}

print(programing)


#find keys and value 

for keys in programing.values():
    print(keys)