import psutil
import time

# Identificar todas las interfaces de red y sus estadísticas
print("Available network interfaces and their stats:")
interfaces = psutil.net_if_addrs()
for iface, stats in interfaces.items():
    print(f"Interface: {iface}")
    for s in stats:
        print(f"  {s}")

# Monitorear una interfaz específica (por ejemplo: 'eth0')
INTERFACE_NAME = "eth0"  # Cambia esto por el nombre de tu interfaz activa

try:
    while True:
        # Obtener estadísticas de la interfaz específica
        counters = psutil.net_io_counters(pernic=True)
        if INTERFACE_NAME not in counters:
            print(f"Error: Interface '{INTERFACE_NAME}' not found. Available interfaces: {list(counters.keys())}")
            break

        stats = counters[INTERFACE_NAME]
        bytes_received = stats.bytes_recv
        bytes_sent = stats.bytes_sent

        # Convertir bytes a KB para mayor claridad
        kb_received = bytes_received / 1024 / 1024
        kb_sent = bytes_sent / 1024 / 1024

        # Imprimir tráfico actual de la interfaz
        print(f"Interface '{INTERFACE_NAME}': {kb_received:.2f} MB received, {kb_sent:.2f} MB sent")

        time.sleep(1)

except KeyboardInterrupt:
    print("\nMonitoring stopped.")
