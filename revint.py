    
def reverseint(x):
    x = str(x)
    revstr = x[::-1]
    
    if '-' in revstr:
        revstr = revstr.replace("-","")
        revstr = "-" + revstr
        intrev = int(revstr)
        return intrev
    else:
        intrev = int(revstr)
        if intrev < (-2**31) or intrev > (2**31-1):
            return 0
# print(reverseint(-123))
print(reverseint(1534236469))
