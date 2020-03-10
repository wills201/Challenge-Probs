def productrange(range1, range2):
    numberlst = [i for i in range(range2)]
    resultlst = []
    for num in range(range2 - 1):
        if numberlst[num] * numberlst[num+1] in range(range1, range2 + 1):
            resultlst.append((numberlst[num],numberlst[num+1]))
    return len(resultlst)
print(productrange(9,100))