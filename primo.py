def is_prime(a):
    
    divisores=0
    mitadE=a//2
    for i in range(1, mitadE):
        if a%i==0:
            divisores=divisores+1
            if divisores==3:
                break


    if divisores<=1:
        print("Is a prime number")
    else:
        print("Is NOT a prime number") 


x=int(input("El numero a probar es: "))
is_prime(x)