import time
import sys

def limpiar_pantalla():
    """Limpia las dos líneas anteriores de la consola"""
    sys.stdout.write("\033[F\033[K")  # Sube una línea y la limpia
    sys.stdout.write("\033[F\033[K")  # Sube otra línea y la limpia

def barra_progreso(progreso, total, longitud=50, etiqueta=""):
    porcentaje = min(progreso / total, 1.0)
    barras_llenas = int(longitud * porcentaje)
    barra = "|" + "█" * barras_llenas + "-" * (longitud - barras_llenas) + "|"
    return f"{etiqueta} {barra} {porcentaje * 100:.1f}%"

if len(sys.argv) < 2:
    print("Uso: python tiempo.py <minutos>")
    sys.exit(1)

try:
    min_totales = int(sys.argv[1])
except ValueError:
    print("Error: El argumento debe ser un número entero.")
    sys.exit(1)

seg_totales = min_totales * 60
seg_transcurridos = 0
seg_en_minuto_actual = 0

print(f"Iniciando temporizador de {min_totales} minutos...\n")
print("Progreso:\n")
print()  # Espacio para la primera barra
print()  # Espacio para la segunda barra

try:
    while seg_transcurridos < seg_totales:
        time.sleep(1)
        seg_transcurridos += 1
        seg_en_minuto_actual += 1

        # Preparamos las dos barras
        barra_total = barra_progreso(seg_transcurridos, seg_totales, 50, "Total:")
        barra_minuto = barra_progreso(seg_en_minuto_actual, 60, 50, "Minuto:")
        
        # Actualizamos las dos líneas
        limpiar_pantalla()
        print(barra_total + f"| {seg_transcurridos/60:.1f}mins.")
        print(barra_minuto + f"| {seg_en_minuto_actual} segs.")

        # Reiniciamos el minuto actual si es necesario
        if seg_en_minuto_actual >= 60:
            seg_en_minuto_actual = 0

    print("\n######################")
    print("¡Tiempo completado!")
    print("######################")

except KeyboardInterrupt:
    print("\nTemporizador detenido manualmente.")