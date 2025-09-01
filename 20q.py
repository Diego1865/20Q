
import json
# Abrir json
with open("dataset.json", "r", encoding="utf-8") as archivo:
    arbol=json.load(archivo)


def jugar(nodo):
    # 1) Si es hoja, imprime resultado y regresa
    if "resultado" in nodo:
        print("Resultado:", nodo["resultado"])
        return

    # 2) Validación básica
    if "pregunta" not in nodo:
        print("Nodo inválido (falta 'pregunta'):", nodo)
        return

    # 3) Pregunta y decide rama
    resp = input(nodo["pregunta"] + " (si/no): ").strip().lower()
    rama = "si" if resp.startswith("s") else "no"

    # 4) Baja solo por la rama elegida si existe
    if rama in nodo and isinstance(nodo[rama], dict):
        jugar(nodo[rama])
    else:
        # Fallback útil para depurar
        print(f"Falta la rama '{rama}' en: {nodo['pregunta']}")

jugar(arbol)



