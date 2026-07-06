#problema8
#leeunatemperaturaenCeeimprimeelestadodelagua
temp = float(input("Ingresa la temperatura en grados Celsius: "))
if temp <= 0:
    print("estado:sólido(hielo)")
elif 0 < temp < 100:
    print("líquido(agua)")
else:
    print("gaseoso(vapor)")