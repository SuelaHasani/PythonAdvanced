"""file = open("example","r")

content = file.read()

print(content)

file.close()

"""


import os
with open("example2.txt","r") as file:
    content = file.read()
    print(content)

#with open("example2.txt","w") as file:
    #file.write("\n hello donjeta")

with open("example2.txt","a") as file:
    file.write("\n hello donjeta")

if os.path.exists("gg.txt"):
    print("file ekziston")
else:
    print("file nuk ekziston")
