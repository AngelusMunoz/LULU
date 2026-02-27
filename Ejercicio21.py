contrasena_correcta = "090501"

contrasena = input("Ingrese la contraseña de 6 digitos: ")

array1 = list(contrasena_correcta)
array2 = list(contrasena)

len(array1) == len(array2)

cont = 0
for i in range(len(array1)):
    print("Comparando el digito", array1[i], "con el digito", array2[i])
    if array1[i] == array2[i]:
        cont += 1
        print("El digito", array1[i], "es correcto")
        print("La cantidad de digitos correctos es:", cont)
    

if cont == len(array1):
    print("Contraseña correcta, acceso concedido")
else:
    print("Contraseña incorrecta, acceso denegado")
    

