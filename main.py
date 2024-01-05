import serial
import time

# Configura el puerto serial (ajusta el puerto según tu sistema operativo)
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

def leer_bits():
    # Lee 8 bits desde Arduino
    bits = []
    for _ in range(8):
        bits.append(ser.read().decode('utf-8'))
        time.sleep(1)  # Espera 1 segundo entre cada bit
    return bits

try:
    while True:
        # Lee 8 bits desde Arduino
        bits_leidos = leer_bits()

        # Muestra los bits leídos
        print("Bits leídos:", bits_leidos)

        # Convierte los bits a un número entero
        numero = int(''.join(bits_leidos), 2)
        print("Número:", numero)

        VoltajeA = numero * 9.6078e-3
        print("Voltaje A:", VoltajeA)

        E2 = -1*((VoltajeA / 1) - 2.5)
        print("Voltaje Sus:", E2)

        DR = 10e3  


except KeyboardInterrupt:
    print("Programa detenido por el usuario.")

finally:
    # Cierra el puerto serial al finalizar
    ser.close()
