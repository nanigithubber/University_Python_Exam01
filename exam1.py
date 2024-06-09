# 1. Creating lists to be used in the formatting of the receit and its corresponding values.
foodName              = ["pizza(s)", "salad(s)", "drink(s)"]
foodPrice             = [85,         65,         20        ]
orderQuantityPersonal = [0,          0,          0         ]
orderQuantityTotal    = [0,          0,          0         ]
orderPriceTotal       = [0,          0,          0,        ]

# 2. Creating a function that toggles betweeen 0 and 1, used for toggling adding and removing items from an order.
def toggleAmount(orderType):
    if orderQuantityPersonal[orderType] == 0: 
        orderQuantityPersonal[orderType] = 1
    else:
        orderQuantityPersonal[orderType] = 0

# 3. Creating a function for updating the total amount and price of orders correspoding to the food itemsafter a person has made an order.
def calcOrderQuantityTotal():
    for x in range (len(orderQuantityTotal)):
        orderQuantityTotal[x] = orderQuantityTotal[x] + orderQuantityPersonal[x]
        orderPriceTotal[x] = orderPriceTotal[x] + orderQuantityPersonal[x] * foodPrice[x]
        orderQuantityPersonal[x]=0

# 4. Creating a function for the receit making process.
def printReceit():
    if all ([x == 0 for x in orderQuantityTotal]):
        print('No order')
    else:
        print (f'------------------------------\n         Your order:\n------------------------------')
        for x in range (len(orderQuantityTotal)):
            if orderQuantityTotal[x] >= 1:
                print (f'{orderQuantityTotal[x]} {foodName[x]} x {foodPrice[x]} kr:{orderPriceTotal[x]:>8.2f} kr')
            else:
                continue
        vatPriceReceit = ( float(orderPriceTotal[0]) + float(orderPriceTotal[1]) + float(orderPriceTotal[2]) ) * 0.12
        deliveryPriceReceit = 50
        print (f'\nVAT (12%)         :{vatPriceReceit:>8.2f} kr')
        print (f'Delivery          :{deliveryPriceReceit:>8.2f} kr')
        totalPriceReceit = orderPriceTotal[0] + orderPriceTotal[1] + orderPriceTotal[2] + vatPriceReceit + deliveryPriceReceit
        print (f'\nTotal price       :{totalPriceReceit:>8.2f} kr')

# 5. Prompting the user to enter the amount of customers
titleOrder = ('What food to order')
print(f'------------------------------\n{titleOrder:^30}\n------------------------------\n')
orderQuantity = int(input(f'\nHow many persons are there? '))

# 6. Processing the orders from said customers 
if orderQuantity == 0:
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