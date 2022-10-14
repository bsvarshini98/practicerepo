def CheckOddwords(strlist):
    x = len([i for i in strlist])
    output = 0
    for eachdata in strlist:
        j = 0
        for i in eachdata:
            j = j + 1
        if (j % 2 == 1):
            output = output + 1
    if len(strlist):
        return output
    else:
        return -1

n = int(input("Enter number of elements : "))
for i in range(0, n):
    element = str(input("enter elemenst {} \n".format(i)))
    l1.append(element)
print("number of odd lenght words in string are =",CheckOddwords(l1))
