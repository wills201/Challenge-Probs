
def longest_number(num): 
    new_str = str(num)
    num_lst = []
    for char in new_str:
        num_lst.append(int(char))
    counter = 0
    counter_lst = []
    for i in range(len(num_lst)-1):
        idx1 = i
        idx2 = i+1
        if num_lst[idx1] > num_lst[idx2]:
            counter = 0
        elif num_lst[idx1] < num_lst[idx2]:
            counter += 1
            counter_lst.append(counter)
        
    return max(counter_lst) + 1

print(longest_number(94585898))