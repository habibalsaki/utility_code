def reverse_string(string):
    myList = []
    for i in range(len(string)-1,-1,-1):
        myList.append(string[i])

    return "".join(myList)

def reverse_string2(string):
    return string[::-1]

print(reverse_string('habib'))
print(reverse_string2('saki'))