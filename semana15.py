# Crear un diccionario llamado informacion_personal
informacion_personal = {
    "nombre": "Patrick Luna",
    "edad": 23,
    "ciudad": "Guayaquil",
    "profesion": "Ingeniero"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
print(f"Ciudad original: {informacion_personal['ciudad']}")  # Imprimir la ciudad original
informacion_personal["ciudad"] = "Quito"  # Cambiar la ciudad a Quito
print(f"Ciudad modificada: {informacion_personal['ciudad']}")  # Imprimir la ciudad modificada

# Agregar una nueva clave-valor al diccionario que represente la "profesion"
informacion_personal["profesion"] = "Estudiante"  # Modificar la profesión
print(f"Profesión actualizada: {informacion_personal['profesion']}")  # Imprimir la profesión actualizada

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:  # Si "telefono" no está en el diccionario
    informacion_personal["telefono"] = "0984311361"  # Agregar la clave "telefono" con un número
    print(f"Número de teléfono agregado: {informacion_personal['telefono']}")  # Imprimir el número de teléfono

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:  # Si "edad" está en el diccionario
    del informacion_personal["edad"]  # Eliminar la clave "edad"
    print("Clave 'edad' eliminada.")  # Confirmar eliminación

# Imprimir el diccionario resultante
print("Diccionario final:", informacion_personal)  # Imprimir el diccionario final
