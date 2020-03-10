def digital_root(n):
    n = str(n)
    sumlst = []
    for i in n:
        sumlst.append(int(i))
    x = sum(sumlst)
    if len(str(x))>1:
        return digital_root(x)
    return x


print(digital_root(335))
