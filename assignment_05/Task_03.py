# 3. File Reader Utility
# Write a Python program that asks the user for a filename and reads its contents.
# Requirements:
#  Handle FileNotFoundError if file does not exist.
#  Handle PermissionError if access is denied.
#  Use finally block to print: "File operation completed."
#  Count and display:
# o number of lines
# o number of words
# o number of characters


import os

# "When you use open(), Python automatically checks for errors like 'File Not Found'. 
# If the file is missing, the code jumps directly to the except block and never reaches your manual raise line.
#  So, if you want your own custom message for every error, you must catch the system's error first and then show your own text.

try:
    file_name = input("Enter the file name: ")
    
    try:
        with open(f"{file_name}.txt", "r") as file:
            content = file.read()
            
            if not content:
                raise Exception("file is empty")
                
            print("File Content:", content)

    except FileNotFoundError:
        raise Exception("file not found") 

except Exception as e:
    print(f"Kuch aur gadbad hai: {e}")



  
  


