"""Generate sales report showing total melons each salesperson sold."""

salespeople = []  #Created an empty list for salesperson
melons_sold = [] #Created an empty list for melons sold
melons_price = [] #created an empty list for melon's price

f = open('sales-report.txt')

for line in f:
    line = line.rstrip()
    entries = line.split('|')

    salesperson = entries[0]
    melons = int(entries[2])
    price = float(entries[1])

    if salesperson in salespeople:
        position = salespeople.index(salesperson)

        melons_sold[position] += melons
        melons_price[position]+= price
        
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)
        melons_price.append(price)


for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons for ${melons_price[i]:.2f}')
