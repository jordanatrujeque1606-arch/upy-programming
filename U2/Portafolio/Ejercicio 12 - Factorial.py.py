#12factoriales

n=int(input("ingresa un número:"))
total=1
i=1

while i<=n:
    total=total*i
    i= i+1
print("factorial:",total)