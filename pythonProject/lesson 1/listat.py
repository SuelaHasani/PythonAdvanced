studentat =["Suela","Rudina","Liza","Dua","Ylli","YlliC","Eldon","Unik","Trim"]

print(studentat)

print(studentat[0])
print(studentat[1])
print(studentat[2])

#studentat.reverse()

studentat.append("Donjeta")
studentat.insert(5,"Donjeta")

print(studentat.count("Donjeta"))
studentat.remove("Trim")


lista2 = studentat.copy()
lista2.clear()
print(lista2)
print("ylli eshte ne pozicionin e : " ,studentat.index("Ylli"))

print(studentat)
