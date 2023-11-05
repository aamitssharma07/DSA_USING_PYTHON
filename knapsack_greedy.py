
def max_profit(profit_array, weight_array, knapsack_size):
    profit = 0
    # Zip function is used to take combine two lists and create new lists with tuple pairs
    profit_weight_ratio = {x/y:y for (x,y) in zip(profit_array,weight_array)}
    print(profit_weight_ratio)
    #Sort profit/weight in non decreasing order
    profit_weight_ratio_ordered = {x:profit_weight_ratio[x]  for x in sorted(profit_weight_ratio, reverse=True)}
    profit_weight_ratio = profit_weight_ratio_ordered
    print(profit_weight_ratio)
    # loop for filling the knapsack in the decreasing order of the profit
    while(knapsack_size !=0):
        for profit_weight in profit_weight_ratio:
            if(knapsack_size >= profit_weight_ratio[profit_weight]):
                knapsack_size = knapsack_size - profit_weight_ratio[profit_weight]
                profit = profit + profit_weight * profit_weight_ratio[profit_weight]
            else:
                profit = profit + knapsack_size *  profit_weight
                knapsack_size = 0
        return  profit
#Main Program

profit_array = [ 2, 40,300]
weight_array = [10, 20,30]

knapsack_size = 50

max_profit = max_profit(profit_array, weight_array, knapsack_size )
print(max_profit)