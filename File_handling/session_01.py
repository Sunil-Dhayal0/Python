# file handling
#  it is the purpose of creating , opening, reading, writing and closing files.
#  store the data permanently.
#  RAM -> Disk
#  need:
#       -ex student data, employee records, log ,reports,configaration files, . . . data is required to store.
#         - different types of file : txt,csv,json,sql,......

# opening a file:

# file_object = open("filename","mode")



#1.  Read : r
# file must be existing
# default mode
# ex
# f = open("abc.txt","r")
# print(f.read())
# f.close()
# --------
#2. write : w
#  open file for writing
#  create file doesn't exist and write
#  if file exist, delete old content
# ----------
# f = open("abc.txt","w")
# f.write(input('enter the data you want to write in file'))
# print(f.read())
# f.close()
# ----------
#3. Append : a
# f = open("abc.txt","a")
# f.write("new content append")
# f = open("abc.txt","r")
# print(f.read())
# f.close()
# -------
#4. exclusive create mode : x
# f = open("abcc.txt","x")
# f.write("\n implement")
# f.close()


######-------- Binary mode: Non-text file
# image , pdf, audiio, etc...
#  "b" is addes in the mode
# -r: rb,-w:wb,-a:ab
#  combined file mode:
#  read : r+
#      -read and write
#      -file must exist
#      - pointer starts at the befining of 1st character


# -write : w+
#        -REad and write
#        -overrides existing content
#        -Creates file if it is not existing


# -append : a+
#           -read and append
#           -create file if not exist
#           -

# f = open("abc.txt","r")
# data = f.read()
# print(data)
# f.close()
# f.close()

# f = open("new.txt",'w')
# f.write('new file is created')
# f.close()
# f = open('new.txt','r')
# print(f.read(5))
# f.close()



# file pointer/cursor postion:
# 1. tell(): return current position of cursor
# 2. seek(): moves pointer toa specifiic position

with open("abc.txt","r") as f:
    print(f.tell())   
    print(f.read(5))
    print(f.tell())  # position after 5 char
    f.seek(0)
    print(f.tell()) 
    print(f.read(5))
    print(f.name)
    print(f.mode)
    print(f.closed)

import os

if os.path.exists("abc.txt"):
    print("file exist")
else:
    print("file not exist")
 