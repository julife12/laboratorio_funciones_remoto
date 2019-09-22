def is_prime(a):
    
    divisores=0
    mitadE=a//2
    for i in range(1, mitadE+1):
        if a%i==0:
            divisores=divisores+1
            if divisores==3:
                break


    if divisores<2:
        return 1
    else:
        return 0 


while True:
    try:
        x=int(input("El numero a probar es: "))
    except ValueError:
        x=0
        print(0)

    if x<=0:
        break
    if x!=0:   
        valor=is_prime(x)
        print(valor)
