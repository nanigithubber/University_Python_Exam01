# 1. Creating lists for 
foodName              = ["pizza(s)", "salad(s)", "drink(s)"]
foodPrice             = [85,         65,         20        ]
orderQuantityPersonal = [0,          0,          0         ]
orderQuantityTotal    = [0,          0,          0         ]
orderPriceTotal       = [0,          0,          0,        ]

# 2. Creating a function that toggles betweeen 0 and 1.
def toggleAmount(orderType):
    if orderQuantityPersonal[orderType] == 0: 
        orderQuantityPersonal[orderType] = 1
    else:
        orderQuantityPersonal[orderType] = 0

# 3. Creating a function for updating the total amount of orders after a person has made an order.
def calcOrderQuantityTotal():
    for x in range (len(orderQuantityTotal)):
        orderQuantityTotal[x] = orderQuantityTotal[x] + orderQuantityPersonal[x]
        orderPriceTotal[x] = orderPriceTotal[x] + orderQuantityPersonal[x] * foodPrice[x]
        orderQuantityPersonal[x]=0

# 4. Creating a function to create the receit
def printReceit():
    if all ([v == 0 for v in orderQuantityTotal]):
        print('No order')
        exit(0)
    else:
        # 4.1 Title
        print (f'------------------------------\n         Your order:\n------------------------------')
        # 4.2 Pizza, salad and Drink
        for x in range (len(orderQuantityTotal)):
            if orderQuantityTotal[x] >= 1:
                print (f'{orderQuantityTotal[x]} {foodName[x]} x {foodPrice[x]} kr:{orderPriceTotal[x]:>8.2f} kr')
            else:
                continue
    # 4.3 VAT and Delievery
    vatPriceReceit = ( float(orderPriceTotal[0]) + float(orderPriceTotal[1]) + float(orderPriceTotal[2]) ) * 0.12
    delieveryPriceReceit = 50
    print (f'\nVAT (12%)         :{vatPriceReceit:>8.2f} kr')
    print (f'Delievery         :{delieveryPriceReceit:>8.2f} kr')
    # 4.4 Total price
    totalPriceReceit = orderPriceTotal[0] + orderPriceTotal[1] + orderPriceTotal[2] + vatPriceReceit + delieveryPriceReceit
    print (f'\nTotal price       :{totalPriceReceit:>8.2f} kr')

# 5. Welcome message 
titleOrder = ('What food to order')
print(f'------------------------------\n{titleOrder:^30}\n------------------------------\n')
orderQuantity = int(input('How many persons are there? '))

# 6. Process
if orderQuantity <= 0:
    print('No order')
    exit(0)
else:
    for x in range(orderQuantity):
        print(f'--------\nPerson {x+1}\n--------')
        orderRemoveAdd = 0
        while orderRemoveAdd != 4:
            orderRemoveAdd = int(input(f'1. Add/remove pizza ({orderQuantityPersonal[0]} selected)\n2. Add/remove salad ({orderQuantityPersonal[1]} selected)\n3. Add/remove drink ({orderQuantityPersonal[2]} selected)\n4. Finish\nChoose: '))
            if orderRemoveAdd == 1:
                toggleAmount(0)
            elif orderRemoveAdd == 2:
                toggleAmount(1)
            elif orderRemoveAdd == 3:
                toggleAmount(2)
            else:
                break
        calcOrderQuantityTotal()
    printReceit()