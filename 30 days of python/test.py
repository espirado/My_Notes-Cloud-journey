stock_prices = []
with open("stock_prices", 'r') as f:
    for line in f:
        token = line.split(",")
        day = token[0]
        price = float(token[1])
        stock_prices.append([day,prices])

        #time-complexity operation o(n)
#retrieve element
        
        for element in stock_prices:
            if element[0] == 'march9':
             print(element[1])


stock_prices = {}
with open("stock_prices", 'r') as f:
    for line in f:
        token = line.split(",")
        day = token[0]
        price = float(token[1])
        stock_prices[day] = prices

        #operation order o(1)