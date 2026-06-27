def sayHello():
    global mesazhi

    mesazhi = "Hi there!"
    return mesazhi

sayHello()
print(mesazhi)



def fullName():
    global name
    global surname

    name="Suela"
    surname="Hasani"
    return name+surname

print(fullName())

print(name)