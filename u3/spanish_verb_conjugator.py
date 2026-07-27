def conjugar_verbo(verbo, pronombre, modo):
    # PROCESS
    verbo = verbo.lower().strip()
    pronombre = pronombre.lower().strip()
    
    # Raíz y terminación del verbo (ar, er, ir)
    raiz = verbo[:-2]
    terminacion = verbo[-2:]
    
    resultado = ""
    
    # Lógica de conjugación según el modo (Indicativo, Subjuntivo, Imperativo) y terminación
    if modo == "indicativo":
        if terminacion == "ar":
            if pronombre == "yo": resultado = raiz + "o"
            elif pronombre == "tú": resultado = raiz + "as"
            elif pronombre in ["él", "ella", "usted"]: resultado = raiz + "a"
            elif pronombre == "nosotros": resultado = raiz + "amos"
            elif pronombre == "ellos": resultado = raiz + "an"
        elif terminacion == "er":
            if pronombre == "yo": resultado = raiz + "o"
            elif pronombre == "tú": resultado = raiz + "es"
            elif pronombre in ["él", "ella", "usted"]: resultado = raiz + "e"
            elif pronombre == "nosotros": resultado = raiz + "emos"
            elif pronombre == "ellos": resultado = raiz + "en"
        elif terminacion == "ir":
            if pronombre == "yo": resultado = raiz + "o"
            elif pronombre == "tú": resultado = raiz + "es"
            elif pronombre in ["él", "ella", "usted"]: resultado = raiz + "e"
            elif pronombre == "nosotros": resultado = raiz + "imos"
            elif pronombre == "ellos": resultado = raiz + "en"
            
    elif modo == "subjuntivo":
        if terminacion == "ar":
            if pronombre == "yo": resultado = raiz + "e"
            elif pronombre == "tú": resultado = raiz + "es"
            elif pronombre in ["él", "ella", "usted"]: resultado = raiz + "e"
            elif pronombre == "nosotros": resultado = raiz + "emos"
            elif pronombre == "ellos": resultado = raiz + "en"
        elif terminacion in ["er", "ir"]:
            if pronombre == "yo": resultado = raiz + "a"
            elif pronombre == "tú": resultado = raiz + "as"
            elif pronombre in ["él", "ella", "usted"]: resultado = raiz + "a"
            elif pronombre == "nosotros": resultado = raiz + "amos"
            elif pronombre == "ellos": resultado = raiz + "an"
            
    elif modo == "imperativo":
        if pronombre == "tú":
            if terminacion == "ar": resultado = raiz + "a"
            else: resultado = raiz + "e"
        else:
            resultado = "Imperativo no soportado para este pronombre en este ejemplo básico"
    
    if not resultado:
        resultado = "No se pudo realizar la conjugación con los datos provistos."
        
    return resultado

# INPUT
print("--- CONJUGADOR DE VERBOS EN ESPAÑOL ---")
verbo_usuario = input("Ingresa un verbo en infinitivo (terminado en -ar, -er, -ir): ")
pronombre_usuario = input("Ingresa el pronombre (yo, tú, él, nosotros, ellos): ")
modo_usuario = input("Ingresa el modo (indicativo, subjuntivo, imperativo): ")

# PROCESS
conjugacion_final = conjugar_verbo(verbo_usuario, pronombre_usuario, modo_usuario)

# OUTPUT
print("\n--- RESULTADO ---")
print(f"Verbo: {verbo_usuario}")
print(f"Pronombre: {pronombre_usuario}")
print(f"Modo: {modo_usuario}")
print(f"Conjugación: {conjugacion_final}")
