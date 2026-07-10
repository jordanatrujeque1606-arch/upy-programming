# Vocal o consonante
letra = input("Introduce una letra: ").lower()
if len(letra) == 1 and letra.isalpha():
    if letra in ['a', 'e', 'i', 'o', 'u']:
        print(f"'{letra}' es una VOCAL.")
    else:
        print(f"'{letra}' es una CONSONANTE.")
else:
    print("Por favor, introduce una única letra válida (sin números ni símbolos).")