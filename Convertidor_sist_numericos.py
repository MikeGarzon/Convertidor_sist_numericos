#CREANDO METODOS
#Pasando desde decimales, usamos su representacion en memoria, python nos permite esto con el format
def decTobin(a):
    s=int(a)
    print("El numero convertido a binario es","{0:b}".format(s))

def decTooct(a):
    s = int(a)
    print("El numero convertido a Octal es","{0:o}".format(s))

def decTohex(a):
    s = int(a)
    print("El numero convertido a Hexadecimal es","{0:x}".format(s))

#Pasando desde otros sistemas a decimal
def binTodec(a):
    a=int(a)
    binary1 = a
    decimal, i, n = 0, 0, 0
    while (a != 0):
        dec = a % 10
        decimal = decimal + dec * pow(2, i)
        a = a // 10
        i += 1
    print("El numero convertido a decimal es",decimal)

def hexTodec():
    i = int(a,16)
    print("El numero convertido a decimal es",i)

def octTodec():
    i = int(a,8)
    print("El numero convertido a decimal es",i)


#Pasando a otros sitemas numericos
def octTohex(a):
    i = int(a,8)
    print("El numero convertido a Hexadecimal es",hex(i))

def octTobin(a):
    i = int(a, 8)
    print("El numero convertido a binario es","{0:b}".format(i))

def hexTobin(a):
    i = int(a, 16)
    print("El numero convertido a binario es", "{0:b}".format(i))

##CORRIENDO CODIGO
print("**Convertidor de bases numereicas**")
mensaje= ("Seleccione una opcion:\n" 
           "1 para decimal a binario\n"
           "2 para decimal a octal\n"
           "3 para decimal a hexadecimal\n"
           "4 para binario a decimal\n"
           "5 para octal a decimal \n"
           "6 para hexadecimal a decimal\n"
           "7 para octal a hexadecimal\n"
           "8 para octal a binario\n"
           "9 para hexadecimal a binario\n"
           "0 para salir\n")

op = input(mensaje)
while op != "0":
    a = input("Ingrese el número a convertir ")
    if op =="1":
        decTobin(a)
    elif op =="2":
        decTooct(a)
    elif op =="3":
        decTohex(a)
    elif op=="4":
        binTodec(a)
    elif op=="5":
        octTodec()
    elif op=="6":
        hexTodec()
    elif op =="7":
        octTohex(a)
    elif op =="8":
        octTobin(a)
    elif op =="9":
        hexTobin(a)
    input("Presione enter para continuar...")
    op = input(mensaje)
print("Gracias")

#CODIGO CONSTRUIDO POR MAICOL GARZON