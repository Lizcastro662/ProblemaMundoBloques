# Definir las cajas y sus propiedades
cajas = {
    1: {"peso": 10, "tamaño": "Pequeño"},
    2: {"peso": 15, "tamaño": "Mediano"},
    3: {"peso": 20, "tamaño": "Grande"},
    4: {"peso": 8, "tamaño": "Pequeño"},
    5: {"peso": 12, "tamaño": "Mediano"}
}

# Definir las estanterías y sus capacidades de peso
estanterias = {
    1: {"capacidad": 30},
    2: {"capacidad": 40}
}

# Función para organizar las cajas en las estanterías
def organizar_cajas(cajas, estanterias):
    estanteria_actual = 1
    cajas_organizadas = {}

    for num_caja, caja in cajas.items():
        if caja["peso"] <= estanterias[estanteria_actual]["capacidad"]:
            if estanteria_actual not in cajas_organizadas:
                cajas_organizadas[estanteria_actual] = []
            cajas_organizadas[estanteria_actual].append(num_caja)
            estanterias[estanteria_actual]["capacidad"] -= caja["peso"]
        else:
            estanteria_actual += 1
            if estanteria_actual > len(estanterias):
                print("No hay suficientes estanterías para organizar todas las cajas.")
                return
            cajas_organizadas[estanteria_actual] = [num_caja]
            estanterias[estanteria_actual]["capacidad"] -= caja["peso"]

    return cajas_organizadas

# Ejecutar la función y mostrar el resultado
resultado = organizar_cajas(cajas, estanterias)
print("Cajas existentes: ")
print(resultado)
if resultado:
    print("Cajas Organizadas por Estantería:")
    for estanteria, cajas_en_estanteria in resultado.items():
        print(f"Estantería {estanteria}: Cajas {cajas_en_estanteria}")

