import json

def leer_json():
    """Lee el JSON considerando el BOM de UTF-8"""
    try:
        # Usar utf-8-sig que maneja automáticamente el BOM
        with open("prueba.json", "r", encoding="utf-8-sig") as archivo:
            arbol = json.load(archivo)
            print("✅ JSON leído correctamente con utf-8-sig (maneja BOM)")
            return arbol
    except Exception as e:
        print(f"❌ Error al leer JSON: {e}")
        return None

# Función de jugar mejorada
def jugar(nodo):
    if not nodo:
        print("No hay más preguntas.")
        return
        
    if "resultado" in nodo:
        print(f"🎯 Resultado: {nodo['resultado']}")
        return
        
    if "pregunta" in nodo:
        while True:
            try:
                respuesta = input(f"❓ {nodo['pregunta']} (s/n): ").lower().strip()
                if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
                    if "si" in nodo:
                        jugar(nodo["si"])
                    else:
                        print("No hay opción para 'sí'")
                    break
                elif respuesta in ['n', 'no']:
                    if "no" in nodo:
                        jugar(nodo["no"])
                    else:
                        print("No hay opción para 'no'")
                    break
                else:
                    print("⚠️  Por favor, responde 's' para sí o 'n' para no")
            except KeyboardInterrupt:
                print("\n👋 ¡Hasta luego!")
                return
    else:
        print("❌ Nodo sin pregunta válida")

# Programa principal
if __name__ == "__main__":
    print("🎮 Bienvenido al juego de 20 preguntas!")
    print("🔍 Cargando preguntas...")
    
    arbol = leer_json()
    
    if arbol:
        print("✅ ¡Juego cargado correctamente!")
        print("💡 Responde 's' para sí o 'n' para no\n")
        try:
            jugar(arbol)
        except KeyboardInterrupt:
            print("\n👋 ¡Juego terminado!")
    else:
        print("❌ No se pudo iniciar el juego")
        
    input("\nPresiona Enter para salir...")
