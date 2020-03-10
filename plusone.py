def plusone(digits):
    numberstr = ""
    for element in digits:
        element = str(element)
        numberstr += element
    numberint = int(numberstr) + 1
    numberstr2 = str(numberint)
    numberlst = [int(i) for i in numberstr2]
    return numberlst
print(plusone([1,2,3,4,5]))