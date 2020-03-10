# nums = [4,2,5,4,6,3]
nums2 = [3,2,4]
target = 6
# def twosum(numbers, target):

#     for i in range(len(numbers)):
#         firstnum = numbers[i]
#         l = numbers.copy()
#         x = l.pop(i)
#         secondidx = l
#         for n in range(len(secondidx)):
#             new_target = firstnum + secondidx[n]
#             if new_target == target:

#                 # return [i, n+i+1]
#                 if i == 0:
#                     return [i, n+i+1]
#                 else:
#                     return [i, n+i]

# def twosum2(numbers, targets):
#     for i in range(len(numbers)):
#         firstnum = numbers[i]
#         second_num = target - firstnum
#         if second_num in numbers:
#             return [numbers.index(firstnum), numbers.index(second_num)]

# print(twosum2(nums2, target))

# >>> x = ['a', 'b', 'c']
# >>> d = dict(enumerate(x))
# >>> {v:k for k,v in d.items()}
# {'a': 0, 'c': 2, 'b': 1}

d = dict(enumerate(nums2))


def twosum3(nums,target):
    for el in enumerate(nums):

    
    
twosum3(nums2, target)