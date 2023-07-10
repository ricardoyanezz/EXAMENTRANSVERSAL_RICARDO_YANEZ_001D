#Prueba Transversal
import numpy as np
print("Bienvenido al sistema de ventas de Creativos.cl")
asiento = np.zeros((10, 10), dtype=int)

#ENTRADA
def comprar_entrada():
 fila = int(input("Ingrese el número de fila de asiento que quiera:  "))
 columna = int(input("Ingrese el número de columna del asiento que quiera: "))
 if fila[fila-1][columna-1] != 0:
        print("Asiento no disponible")
 else:
      run = int(input("Ingrese Rut:"))

      if 1 <= columna <= 20:
            asiento[fila- 1][columna-1] = run
            print("Asiento comprado exitosamente - Ubicación Platinum")
      elif 21 <= columna <= 50:
            asiento[fila-1][columna-1] = run
            print("Asiento comprado exitosamente - Ubicación Gold")
      elif 51 <= columna <= 100:
            asiento[fila-1][columna-1] = run
            print("Asiento comprado exitosamente - Ubicación silver")
      else:
            print("Número ingresado invalido")


#UBICACIONES
def ubicaciones():
    print("Ubicaciones disponibles")
    for fila in range(10):
        for columna in range(10):
            if asiento[fila][columna] != 0:
                print("X", end="\t")
            else:
                print(f"{fila*10+columna+1}", end="\t")
        print()

#ASISTENTES
def listado():
    asistentes = []
    for fila in range(10):
        for columna in range(10):
            if asiento[fila][columna] != 0:
                asistentes.append(asiento[fila][columna])

    asistentes.sort()
    print("Listado de asistentes:")
    for asistente in asistentes:
        print(asistente)

#GANANCIAS
def ganancias():
    tarifas = {
        "Ubicación Platinum": 120000,
        "Ubicación Gold": 80000,
        "Ubicación Silver": 50000
    }
    total = 0
    for fila in range(10):
        for columna in range(4):
            if 1 <= columna+1 <= 20:
                total += tarifas["Ubicación Platinum"] if asiento[fila][columna] != 0 else 0
            elif 21 <= columna+1 <= 50:
                total += tarifas["Ubicación Gold"] if asiento[fila][columna] != 0 else 0
            elif 51 <= columna+1 <= 100:
                total += tarifas["Ubicación Silver"] if asiento[fila][columna] != 0 else 0

    print(f"Ganancias totales: ${total}")

#MENÚ
while True:
 print("------------Bienvenido al menú------------")
 print("1. Comprar entradas")
 print("2. Mostrar ubicaciones disponibles")
 print("3. Ver listado de asistentes")
 print("4. Mostrar ganacias totales")
 print("5. Salir")
 opcion = int(input("Selecciona una opción: "))
 if opcion == 1:
        comprar_entrada()
 elif opcion == 2:
        ubicaciones()
 elif opcion == 3:
        listado()
 elif opcion == 4:
        ganancias()
 elif opcion == 5:
        print("¡Hasta luego!, Ricardo Yañez, 10/07/2023")
        break
 else:
        print("Por favor, ingrese una opción válida")
