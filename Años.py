# Aquí le pedimos al usuario que ingrese el año actual y luego que escoja un año de su preferencia, se guardan el as variables (tiempo) y (sea).
tiempo = int(input("¡Hola! Ingresa el año actual: "))
sea = int(input("Ingresa un año que sea, el de tu preferencia: "))

"""Ha qui las variables (v) y (r) son los resultados de tiempo que introduzca el usuario más o menos uno,
para futuras condiciones."""
v=tiempo-1
r=tiempo+1

"""Hacemos la primer condición si la variable (v) es igual al resultado que nos da el usuario 
que se almaceno en (sea), mostrando el siguiente mensaje"""
if v == sea :
    print("Desde el año "+ str(tiempo) + " ha pasado un 1 año")

#Aquí lo mismo en la variable (r), si es igual a lo que se almacena en la variable (sea), da el siguiente mensaje.
elif r == sea :
    print("Para llegar al año "+ str(sea) + " hace falta 1 año.")

#En esta parte si no son las condiciones anteriores entonces las variables (tiempo) es mayor que (sea), muestra el siguiente mensaje.
elif tiempo > sea :
    total = tiempo - sea
    print("Han pasado "+ str(total) + " años desde el año que has introducido.")

#Ahora bien si no fue lo anterior, entonces si (tiempo) es menor que (sea), entonces muestra otro mensaje.
elif tiempo < sea :
    total = sea - tiempo
    print("Faltan "+ str(total) + " años para llegar al año que has introducido.")

#De lo contrario mostrara el siguiente mensaje.
else :
    print("Has introducido el mismo año que el actual.")
