# given a list of 2 item lists the first index being the amount of time passed and the second index being the price of the stock
data = [[1,20],[2,30],[3,60],[4,80],[5,30],[6,300],[7,100],[8,80],[9,60],[10,50]]
data2 = [[1, 200],[2,75],[3,50], [4,200], [5,250], [6,300], [7,100], [8,750], [9, 500], [10, 300]]
data3 = [[1,80],[2,30],[3,20],[4,80],[5,30],[6,50],[7,100],[8,80],[9,60],[10,50]]


data4 = [(0,5), (1,10), (2,1), (3,15), (4,1)]
data5 = [[4, 200],[2,75],[3,500], [1,200], [5,50], [6,300], [7,100], [8,350], [9, 100], [10, 300]]

def stockp(data):
    data = [i[1] for i in data]
    profit = 0
    new_max = 0
    for i in range(len(data)):
        new_max = max(data[i:])
        new_profit = new_max - data[i]
        if new_profit > profit:
            profit = new_profit
    return profit
