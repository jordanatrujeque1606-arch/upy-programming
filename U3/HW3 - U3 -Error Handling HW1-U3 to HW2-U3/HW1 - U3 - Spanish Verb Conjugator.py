try:
    # Solicitar al usuario un verbo regular en español que termine en -ar, -er o -ir.
    verbo = input("Ingrese verbo: ").strip().lower()

    # Estructuras de datos requeridas (adaptadas a español latinoamericano: excluyendo 'vosotros')
    pronombres = ['yo', 'tu', 'el', 'nosotros', 'ustedes', 'ellos']
    terminaciones = {
        'ar': ['o', 'as', 'a', 'amos', 'an', 'an'],
        'er': ['o', 'es', 'e', 'emos', 'en', 'en'],
        'ir': ['o', 'es', 'e', 'imos', 'en', 'en']
    }

    # Validar que el verbo tenga al menos 3 caracteres para evitar errores de slicing
    if len(verbo) < 3:
        raise ValueError("El verbo ingresado es demasiado corto.")

    # Obtener la raíz (el verbo sin las últimas 2 letras) y el sufijo (las últimas 2 letras)
    raiz = verbo[:-2]
    sufijo = verbo[-2:]

    # Validar que el sufijo sea válido (-ar, -er, -ir)
    if sufijo not in terminaciones:
        raise KeyError(f"El sufijo '-{sufijo}' no es válido. Debe terminar en -ar, -er o -ir.")

    # Buscar la lista de terminaciones correspondiente en el diccionario
    lista_terminaciones = terminaciones[sufijo]

    # Iterar a través de los pronombres e imprimir cada conjugación correspondiente usando concordancia de índices
    for i in range(len(pronombres)):
        conjugacion = raiz + lista_terminaciones[i]
        print(f"{pronombres[i]} {conjugacion}")

except ValueError as e:
    print(f"Error de valor: {e}")

except KeyError as e:
    print(f"Error de formato: {e}")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

finally:
    print("Ejecución del programa finalizada.")