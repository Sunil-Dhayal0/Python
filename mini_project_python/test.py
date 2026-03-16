Flower_info  =  {'rose':{'Price':50,'Quantity':20,'Category':'decorative'},
                'tulip':{'Price':100,'Quantity':30,'Category':'seasonal'},
                'lily':{'Price':150,'Quantity':40,'Category':'seasonal'}
                }

max_price = 0
flower_name =''
for flower in Flower_info:
    curr_Price = Flower_info[flower]['Price']
    if curr_Price > max_price:
        max_price = curr_Price
        flower_name = flower
  
print(flower_name)
    