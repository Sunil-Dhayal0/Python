import functions

# ========= Flower Shop Management =========
print("========= Flower Shop Management =======")

choice = 0  

while choice<=20 and choice>=0:

          print("############---enter your choice----##################")
          print("Enter 1 to add Flower:")
          print("Enter 2 to Update Price or Quantity:")
          print("Enter 3 to Delete Flower:")
          print("Enter 4 to Search By Flower:")
          print("Enter 5 to Show Formatted Table:")
          print("Enter 6 to All Flower Name:")
          print("Enter 7 to Show & Prices:")
          print("Enter 8 to Check Flower Existence:")
          print("Enter 9 to Count Flower Categories:")
          print("Enter 10 to Find Most Expensive Flower:")
          print("Enter 11 to Find least Expensive Flower:")
          print("Enter 12 to Get Stock Value:")
          print("Enter 13 to Get Low Quantity Flower:")
          print("Enter 14 to Get Stock Value:")
          print("Enter 15 to Sort By Flower Name:")
          print("Enter 16 to Sell Flower:")
          print("Enter 17 to Restock Flower:")
          print("Enter 18 to Expensive Flowers:")
          print("Enter 19 to Clear Stock:")
          print("Enter 20 to Exit:" ,end="")
          print()
          choice =  int(input('enter the choice: '))  
          match choice:
                  case 1:     
                      # 1. Add Flower
                      functions.addFlower()
                  case 2:
                      # 2. Update Flower
                      functions.updateFlower()
                  case 3:
                      # 3. Delete Flower
                      functions.deleteFlower()
                  case 4:
                      # 4. Search Flower
                      functions.searchFlower()
                  case 5:
                      # 5. Display All Flowers
                      functions.displayAllFlower()
                  case 6:
                      # 6. Display Flower Names
                      functions.displayFlowerNames()
                  case 7:
                      # 7. Display Flower Details
                      functions.displayFlowerDetails()
                  case 8:   
                     # 8. Check Flower Availability
                      functions.checkFloweravailablility()
                  case 9:    
                      # 9. Count Total Flower Types
                      functions.totalFlowerTypes()
                  case 10:
                      # 10. Find Most Expensive Flower
                      functions.mostExpensiveFlower()
                  case 11:    
                      # 11. Find Cheapest Flower
                      functions.cheapestFlower()
                  case 12:    
                      # 12. Calculate Total Stock Value
                      functions.totalStockValue()
                  case 13:
                      # 13. Display Low Stock Flowers
                      functions.lowStockFlowers()
                  case 14:    
                      # 14. Sort Flowers by Name
                      functions.sortFlowersByName()
                  case 15:
                      # 15. Sort Flowers by Price
                      functions.sortFlowerByPrice()
                  case 16:
                      # 16. Sell Flower
                      functions.sellFlower()
                  case 17:
                      # 17. Restock Flower
                      functions.restockFlower()
                  case 18:      
                      # 18. Show Expensive Flowers
                      functions.showExpensiveFlowers()
                  case 19:
                       # 19. Clear All Records
                      functions.clearAllRecords()
                  case 20:
                        break    
                      # 20. Exit
        
                       









