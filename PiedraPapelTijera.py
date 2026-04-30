"""
PIEDRA, PAPEL O TIJERA - VERSIÓN PROFESIONAL
Autor: Asistente IA
Descripción: Juego completo con validaciones, puntuación y opción de múltiples rondas.
"""

import random
import os

def limpiar_pantalla():
    """Limpia la consola para una mejor experiencia visual."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_titulo():
    """Muestra el título del juego con diseño."""
    print("=" * 50)
    print("   🎮  PIEDRA, PAPEL O TIJERA  🎮".center(50))
    print("=" * 50)
    print("   🪨  Piedra  |  📄  Papel  |  ✂️  Tijera")
    print("=" * 50)
    print()

def obtener_opcion_usuario():
    """
    Solicita y valida la opción del usuario.
    Retorna: str - 'piedra', 'papel' o 'tijera'
    """
    while True:
        opcion = input("👉 Elige: [piedra, papel, tijera] → ").strip().lower()
        if opcion in ['piedra', 'papel', 'tijera']:
            return opcion
        else:
            print("❌ Opción no válida. Por favor, elige piedra, papel o tijera.\n")

def obtener_opcion_computadora():
    """Genera la opción aleatoria de la computadora."""
    return random.choice(['piedra', 'papel', 'tijera'])

def determinar_ganador(usuario, computadora):
    """
    Determina el resultado de la ronda.
    Retorna: str - 'usuario', 'computadora' o 'empate'
    """
    if usuario == computadora:
        return 'empate'
    
    # Reglas de victoria para el usuario
    if (usuario == 'piedra' and computadora == 'tijera') or \
       (usuario == 'papel' and computadora == 'piedra') or \
       (usuario == 'tijera' and computadora == 'papel'):
        return 'usuario'
    else:
        return 'computadora'

def mostrar_resultado_ronda(usuario, computadora, ganador):
    """Muestra el resultado detallado de la ronda."""
    emoji = {
        'piedra': '🪨', 
        'papel': '📄', 
        'tijera': '✂️'
    }
    
    print("\n" + "-" * 40)
    print(f"🧑 Tú: {emoji[usuario]} {usuario.upper()}")
    print(f"🤖 Computadora: {emoji[computadora]} {computadora.upper()}")
    print("-" * 40)
    
    if ganador == 'usuario':
        print("✅ ¡Ganaste esta ronda!\n")
    elif ganador == 'computadora':
        print("❌ Perdiste esta ronda.\n")
    else:
        print("🤝 ¡Empate!\n")

def mostrar_puntaje(puntaje_usuario, puntaje_computadora):
    """Muestra el marcador actual."""
    print("=" * 40)
    print(f"🏆 PUNTAJE: Tú {puntaje_usuario}  -  {puntaje_computadora} Computadora")
    print("=" * 40)

def preguntar_continuar():
    """Pregunta si se desea jugar otra ronda."""
    while True:
        respuesta = input("¿Jugar otra ronda? [s/n]: ").strip().lower()
        if respuesta == 's':
            return True
        elif respuesta == 'n':
            return False
        else:
            print("Responde con 's' para sí o 'n' para no.\n")

def main():
    """Función principal del juego."""
    puntaje_usuario = 0
    puntaje_computadora = 0
    ronda = 1
    
    while True:
        limpiar_pantalla()
        mostrar_titulo()
        mostrar_puntaje(puntaje_usuario, puntaje_computadora)
        print(f"🎲 Ronda {ronda}\n")
        
        # Obtener opciones
        usuario = obtener_opcion_usuario()
        computadora = obtener_opcion_computadora()
        
        # Determinar ganador
        ganador = determinar_ganador(usuario, computadora)
        
        # Actualizar puntaje
        if ganador == 'usuario':
            puntaje_usuario += 1
        elif ganador == 'computadora':
            puntaje_computadora += 1
        
        # Mostrar resultado
        mostrar_resultado_ronda(usuario, computadora, ganador)
        mostrar_puntaje(puntaje_usuario, puntaje_computadora)
        
        # Preguntar si continuar
        if not preguntar_continuar():
            break
        
        ronda += 1
    
    # Mensaje final
    limpiar_pantalla()
    mostrar_titulo()
    print("🎬 JUEGO TERMINADO".center(50))
    print(f"\n📊 RESULTADO FINAL:")
    print(f"   Rondas jugadas: {ronda}")
    print(f"   Tu puntaje: {puntaje_usuario}")
    print(f"   Computadora: {puntaje_computadora}")
    
    if puntaje_usuario > puntaje_computadora:
        print("\n🏆 ¡FELICIDADES! ¡Ganaste el juego! 🏆")
    elif puntaje_computadora > puntaje_usuario:
        print("\n💻 La computadora ganó esta vez. ¡Mejor suerte la próxima!")
    else:
        print("\n🤝 ¡Empate general!")
    
    print("\n" + "=" * 50)
    print("¡Gracias por jugar! 🎉")

if __name__ == "__main__":
    main()
