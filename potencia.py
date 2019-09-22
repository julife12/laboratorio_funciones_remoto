contador=1
contador_errores=0
contador_pares=0
contador_impares=0
def a_power_b(a,b):  
    cuadrado=1
        
    for j in range(1, b+1):
        cuadrado=cuadrado*a

    
    return cuadrado


while True:


    while True:
        
        try:
            n1=int(input("digite el numero: "))
            break
        except ValueError:
            print("debe digitar un numero valido, intente de nuevo")
            contador_errores=contador_errores+1

    if n1==0:
        break
    while True:
        try:
            p1=int(input("digite la potencia: "))
            break
        except ValueError:
            print("debe digitar un numero valido, intente de nuevo")
            contador_errores=contador_errores+1
    
            

    nm1=a_power_b(n1, p1)
    print("elnumero elevado es igual a: ",nm1)
    contador=contador+1
    if nm1%2==0:
        print("y es par")
        contador_pares=contador_pares+1
    else:
        print("y es impar")
        contador_impares=contador_impares+1
    
print("la cantidad de veces que se hayo la potencia fue: ", contador-1)
print("la cantidad de errores fue: ", contador_errores)
print("la cantidad de pares fue: ", contador_pares, " y la cantidad de impares fue: ", contador_impares)
    
