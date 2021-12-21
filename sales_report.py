"""Generate sales report showing total melons each salesperson sold."""

salespeople = []  #Created an empty list for salesperson
melons_sold = [] #Created an empty list for melons sold
melons_price = [] #created an empty list for melon's price

f = open('sales-report.txt') #opens the existing sales-repport files 

for line in f: #reading the file line by line 
    line = line.rstrip() #it removes the white spaces at the end of the string
    entries = line.split('|') # splits each word in the list in string

    salesperson = entries[0] #each word/string of index 0 is saved in salesperson 
    melons = int(entries[2]) #int converst the string to integers and saves each number of index 2 in melons
    price = float(entries[1]) #int converst the string to float datatype and saves each number of index1 in price

    if salesperson in salespeople:#conditions to be checked and if the condition is true
        position = salespeople.index(salesperson)#assign each salesperson on index 0 from salespepole to position

        melons_sold[position] += melons#the melons sold for that position by that salesperson is then added and assigned to melons_sold
        melons_price[position]+= price #the price for the  melon types sold for that position by that salesperson is then added and assigned to melons_price
        
    else: #if the condition does not match
        salespeople.append(salesperson)#add salesperson
        melons_sold.append(melons)#add melons sold
        melons_price.append(price)#add melon's price

# print(range(len(salespeople)))
for i in range(len(salespeople)):#iterates through grouped salespeople 
    print(f'{salespeople[i]} sold {melons_sold[i]} melons for ${melons_price[i]:.2f}')
