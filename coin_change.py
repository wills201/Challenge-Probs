def coin_change(amt, coin_lst):
    coin_comb = 0
    if sum(coin_lst) == amt:
        coin_comb += 1
    for coins in range(len(coin_lst)):
        coin = coin_lst[coins]
        # if  == 0:
        coin_comb += 1
            # coin_change(amt, coin_lst)
    return print(coin_comb)
coin_change(6,[1,5])