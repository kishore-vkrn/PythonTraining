def addProductSales():
	db = {}
	while True:
		product = raw_input("Enter Product: ")
		if not product:
			break
		sales = int(raw_input("Sales: "))
		price = int(raw_input("Price: "))
		db[product] = {'sales':sales, 'price':price}
	return db

#To print db items
def printReport(db):
	revenue = 0
	for k,v in db.items():
		print 'Product: ',k,v['sales'],v['price']
		revenue += v['sales']*v['price']
	print revenue
		
db1 = addProductSales()
printReport(db1)