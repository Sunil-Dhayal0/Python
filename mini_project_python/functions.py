########----------- blue print of data store in dictionary

# flowers    =   {'rose':{'price':50,'Quantity':20,'Category':'decorative'},
#                 'tulip':{'price':100,'Quantity':30,'Category':'seasonal'},
#                 'lily':{'Price':150},'Quantity':40,'Category':'seasonal'
#                 }

Flower_info  =  {'rose':{'Price':50,'Quantity':20,'Category':'decorative'},
                'tulip':{'Price':100,'Quantity':30,'Category':'seasonal'},
                'lily':{'Price':150,'Quantity':40,'Category':'seasonal'}
                }


##1--- addFlower function

def addFlower():
    F_name = input('enter the number of flower')
    Flower_names = list(Flower_info)

    if F_name in Flower_names:
        print('this flower is already added')
    else:
        F_price    = int(input('enter the price of flower     : '))
        F_quantity = int(input('enter the quantitiy of flower : '))
        F_category = input('enter  the  category of flower    : ')

        Flower_info[F_name] = {'Price':F_price,
                               'Quantity':F_quantity,
                               'Category':F_category
                               }

##2--- updateFlower function

def updateFlower():
    F_name =  input('enter the name of flower you want to update that: ')

    Flower_names = list(Flower_info)

    if F_name in Flower_names:
        F_price    = int(input(f'enter the new price of flower {F_name} : '))
        F_quantity = int(input(f'enter the new quantitiy number of flower {F_name} : '))
        F_category = input(f'enter the new category of flower {F_name} : ')        

        Flower_info[F_name] = {'Price':F_price,
                               'Quantity':F_quantity,
                               'Category':F_category
                               }
    else:
        print("flower no found in shop")


##3--- Delete Flower 
def deleteFlower():
    F_name = input('enter the name of flower : ')
    Flower_names = list(Flower_info)
    if F_name in Flower_names:
        Flower_info.pop(F_name)
    else:
        print('flower not found in the shop ')


##4-- Search Flower

def searchFlower():

    F_name = input('enter the name of flower : ')
    for flower in Flower_info:
        if flower == F_name:
            print('your flower is founded :')
            print(f' flower price is {Flower_info[flower]['Price']}')
            print(f' flower quantity is {Flower_info[flower]['Quantity']}') 
            print(f' flower category is {Flower_info[flower]['Category']}')
            


##5--- Display All Flowers function

def displayAllFlower():

    for flower in Flower_info:

        print(f'flower   name      is: {flower}')
        print(f'flower   price     is:  {Flower_info[flower]['Price']}')
        print(f'quantity of flower is: {Flower_info[flower]['Quantity']}')
        print(f'category of flower is: {Flower_info[flower]['Category']}')
        print('\n \n')        

##6-- Display Flower Names

def displayFlowerNames():
    for flower in Flower_info:
        print(f'flower   name      is: {flower}')

#7-- Display Flower Details

def displayFlowerDetails():

    F_name = input('enter the name of flower : ')
    for flower in Flower_info:
        if flower == F_name:
            print('your flower detials :--------')
            print(f' flower price is {Flower_info[flower]['Price']}')
            print(f' flower quantity is {Flower_info[flower]['Quantity']}') 
            print(f' flower category is {Flower_info[flower]['Category']}')

# 8. Check Flower Availability
def checkFloweravailablility():
    F_name = input('enter the name of flower : ')
    for flower in Flower_info:
        if flower == F_name:
            print(' This flower is available and details of this flower is below :--------')
            print(f' flower price is {Flower_info[flower]['Price']}')
            print(f' flower quantity is {Flower_info[flower]['Quantity']}') 
            print(f' flower category is {Flower_info[flower]['Category']}')           

# 9. Count Total Flower Types
def totalFlowerTypes():
    F_name = input('enter the name of flower : ')
    number_of_type_of_flower = len(Flower_info)
    print(f'in shop {number_of_type_of_flower} type of flower')


# 10. Find Most Expensive Flower
def mostExpensiveFlower():
    max_price = 0
    Flower = ''
    for flower in Flower_info:
        current_price = Flower_info[flower]['Price']
        if current_price > max_price:
            max_price > current_price
            Flower =  flower
    print(f'The most expensive flower is: {Flower}') 
    

# 11. Find Cheapest Flower
def cheapestFlower():
     min_price = 0
     Flower = ''
     for flower in Flower_info:
         current_price = Flower_info[flower]['Price']
         if current_price < min_price:
             min_price = current_price
             Flower = flower
     print(f'The cheapest flower is: {Flower}')
             
# 12. Calculate Total Stock Value
def totalStockValue():
    total_flower = 0
    for flower in Flower_info:
        total_flower+=Flower_info[flower]['Quantity']
    print(f'totalstockvalue is: {total_flower}')
    
# 13. Display Low Stock Flowers
def lowStockFlowers():
    low_stock_flower = ''
    min_stock = 0
    for flower in Flower_info:
        curr_stock = Flower_info[flower]['Quantity']
        if curr_stock < min_stock:
            min_stock = curr_stock
            low_stock_flower = flower
    print(f'{low_stock_flower} is low stack flower') 

# 14. Sort Flowers by Name
def sortFlowersByName():
    sorted_flower =  sorted(Flower_info,reverse=False)
    for flower in sorted_flower:
      print('flower are sorted by name ')
      print(f'flower   name      is: {flower}')
      print(f'flower   price     is:  {sorted_flower[flower]['Price']}')
      print(f'quantity of flower is: {sorted_flower[flower]['Quantity']}')
      print(f'category of flower is: {sorted_flower[flower]['Category']}')    

       


# 15. Sort Flowers by Price
def sortFlowerByPrice():
     sorted_flower = sorted(Flower_info,key= lambda x:Flower_info[x]['Price'],reverse=False)
     for flower in sorted_flower:
      print('flower are sorted by price')
      print(f'flower   name      is: {flower}')
      print(f'flower   price     is:  {sorted_flower[flower]['Price']}')
      print(f'quantity of flower is: {sorted_flower[flower]['Quantity']}')
      print(f'category of flower is: {sorted_flower[flower]['Category']}')  

# 16. Sell Flower
def sellFlower():
    F_name = input('enter the name of flower : ')
    Flower_names = list(Flower_info)
    if F_name in Flower_names:
        Flower_info.pop(F_name)
        print('flower is sold')
    else:
        print('flower not found in the shop ')

# 17. Restock Flower

def restockFlower():
    F_name = input('enter the number of flower')
    Flower_names = list(Flower_info)

    if F_name in Flower_names:
        print('this flower is already added')
    else:
        F_price    = int(input('enter the price of flower     : '))
        F_quantity = int(input('enter the quantitiy of flower : '))
        F_category = input('enter  the  category of flower    : ')

        Flower_info[F_name] = {'Price':F_price,
                               'Quantity':F_quantity,
                               'Category':F_category
                               }
       

# 18. Show Expensive Flowers
def showExpensiveFlowers():
    for flower in Flower_info:
        if Flower_info[flower]['Price'] > 100:
          print(f'flower   name      is: {flower}')
          print(f'flower   price     is:  {Flower_info[flower]['Price']}')
          print(f'quantity of flower is: {Flower_info[flower]['Quantity']}')
          print(f'category of flower is: {Flower_info[flower]['Category']}')
          print('\n \n')  
      

# 19. Clear All Records

def clearAllRecords():
    del Flower_info