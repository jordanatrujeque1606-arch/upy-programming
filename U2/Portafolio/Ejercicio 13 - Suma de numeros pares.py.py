#13suma de numeros pares
#suma número pares hasta la numero Ñ

n=int(input("ingresa un número:"))
res=0
for i in range(2,n + 1,2):
    res=res+i
print("suma de pares",res)
    