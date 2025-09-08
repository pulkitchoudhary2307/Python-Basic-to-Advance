start = int(input('enter start = '))
stop = int(input('enter stop = '))
skip = int(input('enter skip = '))

if stop<=skip :
    print ("this is invalid no")

elif start>stop :
    print ("Start No. is greater than Stop")

else :
    for i in range(start, stop):
        if i == skip :
            continue
        print(i)
