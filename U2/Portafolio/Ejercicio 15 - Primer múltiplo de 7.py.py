#15 primer multiplo de 7 entre q rango/break y continuos/
#ingrese 2 números, A Y B.
a=int(input("ingresa un numero para empezar el rango:"))
b=int(input("ingresa un numero para finalizar el rango:"))
for n in range(a,b+1):
    if n%7==0:
        print("primer multiplo de 7:",n)
        break