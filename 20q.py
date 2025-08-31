
import json
# Abrir json
with open("dataset.json", "r", encoding="utf-8") as archivo:
    arbol=json.load(archivo)


def jugar (nodo):
    if "resultado" in nodo:
        print(f"Resultado: {nodo['resultado']}")
        return
    
    # Pregunta
    respuesta = input(f"{nodo['pregunta']} (s/n): ").lower()
    if respuesta.startswith("s"):
        jugar(nodo["si"])
    else:
        jugar(nodo["no"])

jugar(arbol)



