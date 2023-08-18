nombreUsuario=input("Digita tu nombre: ")
edadUsuario=int(input("Digita tu edad: "))

if   edadUsuario>= 0 and edadUsuario <=15:
    print(f"Querido {nombreUsuario}, Usted es un niño")
elif edadUsuario >15 and edadUsuario <=28:
    print(f"Querido {nombreUsuario}, Usted es un joven")
elif edadUsuario >28 and edadUsuario <=60:
    print(f"Querido {nombreUsuario}, Usted es adulto")
elif edadUsuario>60 and edadUsuario<10:
    print(f"Querido {nombreUsuario}, Usted es un adulto mayor")
else:
    print("edad invalidad")