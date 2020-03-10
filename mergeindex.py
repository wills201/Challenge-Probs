l1 = [1,7,3,4,9,3,8,6,8,9]
l2 = [0,3,8,6,8,4,7,6,8,9]

def mergeindex(l1,l2):
    idx = 0
    while idx < len(l1):
        idx += 1
        if l1[idx:] == l2[idx:]:
            return idx

def mergeindex2(l1,l2):
    idx = 0
    while idx < len(l1):
        idx += 1
        if l1[idx] == l2[idx]:
            if l1[-1] == l2[-1]:
                return idx

def mergeindex3(l1,l2):
    idx = len(l1) - 1
    while idx >= 0:
        idx -= 1
        if l1[idx] != l2[idx]:
            return idx + 1
        
print(mergeindex3(l1,l2))
