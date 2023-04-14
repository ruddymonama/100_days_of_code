# 14 April 2023
# By Ruddy Starr 
# Day 2 of 100 Days of Coding & Day 2 of 30 Days of Python
# Program to simulate simple POS

#Create POS function
def POS():
	
	#Greeting to system; Create the POS greeting. Ask for date, name of store, cashier & customer name
	date = input("Please enter today's date: ")
	store = input("Please enter store name: ")
	cashier = input("Please enter cashier name: ")
	customer = input ("Enter name of customer: ")
	#System greeting to cashier
	greeting0 = "\n\n! ! ! Welcome to {0} POS ! ! !\nDate: {1}\n".format(store, date)
	#System greeting to customer
	greeting1 = "################ INVOICE ###############\n"
	greeting2 = "! ! ! Welcome to {0} POS ! ! !\nDate: {1}\nCurrently being assisted by: {2}\n".format(store, date, cashier)
	print(greeting0)
	
	#ask for number of items to scan
	till = int(input("Please enter number of items to scan: "))
	
    #create empty lists of item names and item prices. 
	item = []
	price = []
	
    #Create total counter
	total = 0

	#Loop through basket list and ask for item name and item price. 
	for i in range(till):
		i_tem = input("Please enter name of item: ")
		p_rice = eval(input("Please enter price of item: R "))
        # Add item name to item list and price to price list
		item.append(i_tem)
		price.append(p_rice)
		print("Item scanned !\n")
	
	#print invoice to customer
	print(greeting1)
	print(greeting2)
	print("Invoice for {0}:\n".format(customer))
	#print item together with price in numbered list
	for j in range(till):
		itemdex = item[j]
		pricedex = price[j]
		print("{0}. {1} \t : \tR {2}\n".format(j+1, itemdex, pricedex))
		total += price[j]
		
	#print total to customer and ask for cash to pay and calculate change
	print("Your invoice total: R %.2f"%(total))
	cash = eval(input("Please pay cash: R "))
	change = cash-total #change is invoice total subtracted from cash paid
	print("Cash paid: R %.2f \nYour change: R %.2f"%(cash, change))
	print("\n! ! ! Thank you for using {0} POS ! ! !\n".format(store))

#Start POS	
POS()