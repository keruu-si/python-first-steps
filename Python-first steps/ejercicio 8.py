persona = {
    "nombre": "samuel",
    "edad": 20, 
    "ciudad": "valledupar"
}

print(persona["nombre"])
persona["edad"] = 21
persona["profesion"] = "estudiante"
for clave, valor in persona.items():
    print(f"{clave}: {valor}")