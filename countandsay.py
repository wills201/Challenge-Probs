def countandsay(n):
    new_str = "1"
    if n == 1:
        return str(n)
    new_str = new_str + "1"
    if ("1") in new_str > 1:
        new_str = new_str.replace("1","2")
        
    return new_str
print(countandsay(2))