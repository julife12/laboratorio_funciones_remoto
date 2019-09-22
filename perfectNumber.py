def perfect_number(x):
    mitadE=x//2
    perfecto=0
    for i in range(1, mitadE+1):
        if x%i==0:
            perfecto=perfecto+i

    if perfecto==x:
        print("es un numero perfecto")

n=int(input("ingrese el numero para saber si es perfecto: "))
perfect_number(n)