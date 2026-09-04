import json

# PARTE 1 — Lectura y estructuras de agrupacion

with open("C:/Users/juanc/OneDrive/Escritorio/CAMPUSLANDS/PYTHON FOLDER/RAW/ventas.json", "r") as archivo:
    ventas = json.load(archivo)

montos_por_vendedor = {}

unidades_por_producto = {}

archivo_alertas = open("C:/Users/juanc/OneDrive/Escritorio/CAMPUSLANDS/PYTHON FOLDER/PROCCESED/alertas_ventas.txt", "a")

for venta in ventas:
    monto = venta["cantidad"] * venta["precio_unitario"]

    vendedor = venta["vendedor"]
    if vendedor not in montos_por_vendedor:
        montos_por_vendedor[vendedor] = []
    montos_por_vendedor[vendedor].append(monto)

    producto = venta["producto"]
    if producto not in unidades_por_producto:
        unidades_por_producto[producto] = 0
    unidades_por_producto[producto] = unidades_por_producto[producto] + venta["cantidad"]

    if monto > 700000:
        linea = "Vendedor: " + vendedor + " | Tienda: " + venta["tienda"]
        linea = linea + " | Producto: " + producto + " | Monto: $" + str(monto) + "\n"
        archivo_alertas.write(linea)

archivo_alertas.close()


# PARTE 2 — Calculos estadisticos

estadisticas_vendedores = {}

for vendedor in montos_por_vendedor:
    montos = montos_por_vendedor[vendedor]
    total = sum(montos)
    promedio = total / len(montos)
    venta_max = max(montos)
    venta_min = min(montos)
    estadisticas_vendedores[vendedor] = {
        "total": total,
        "promedio": promedio,
        "venta_max": venta_max,
        "venta_min": venta_min
    }

# Vendedor del mes
vendedor_del_mes = ""
mayor_total = 0

for vendedor in estadisticas_vendedores:
    total = estadisticas_vendedores[vendedor]["total"]
    if total > mayor_total:
        mayor_total = total
        vendedor_del_mes = vendedor

# Producto mas y menos vendido
producto_estrella = ""
max_unidades = 0
producto_menos_vendido = ""
min_unidades = 999999999

for producto in unidades_por_producto:
    unidades = unidades_por_producto[producto]
    if unidades > max_unidades:
        max_unidades = unidades
        producto_estrella = producto
    if unidades < min_unidades:
        min_unidades = unidades
        producto_menos_vendido = producto

# Total general y promedio general
total_general = 0
for vendedor in montos_por_vendedor:
    total_general = total_general + sum(montos_por_vendedor[vendedor])

promedio_general = total_general / len(ventas)


# PARTE 3 — Ranking de vendedores

ranking = []
for vendedor in estadisticas_vendedores:
    tupla = (vendedor, estadisticas_vendedores[vendedor]["total"])
    ranking.append(tupla)

for i in range(len(ranking)):
    for j in range(len(ranking) - 1):
        if ranking[j][1] < ranking[j + 1][1]:
            temp = ranking[j]
            ranking[j] = ranking[j + 1]
            ranking[j + 1] = temp

print("=======================================================")
print("        PODIO DEL MES")
print("=======================================================")
print("  1er lugar: " + ranking[0][0] + " - $" + str(ranking[0][1]))
print("  2do lugar: " + ranking[1][0] + " - $" + str(ranking[1][1]))
print("  3er lugar: " + ranking[2][0] + " - $" + str(ranking[2][1]))
print("=======================================================")


# PARTE 4 — Reportes

with open("C:/Users/juanc/OneDrive/Escritorio/CAMPUSLANDS/PYTHON FOLDER/PROCCESED/resumen_ventas.txt", "w") as archivo_resumen:
    archivo_resumen.write("=======================================================\n")
    archivo_resumen.write("   RESUMEN DE VENTAS DEL MES - JULIO 2026\n")
    archivo_resumen.write("=======================================================\n\n")

    archivo_resumen.write("Total general vendido:      $" + str(total_general) + "\n")
    archivo_resumen.write("Promedio general por venta: $" + str(round(promedio_general)) + "\n\n")

    archivo_resumen.write("Producto estrella:      " + producto_estrella + " (" + str(max_unidades) + " unidades)\n")
    archivo_resumen.write("Producto menos vendido: " + producto_menos_vendido + " (" + str(min_unidades) + " unidades)\n\n")

    archivo_resumen.write("-------------------------------------------------------\n")
    archivo_resumen.write("   RANKING COMPLETO DE VENDEDORES\n")
    archivo_resumen.write("-------------------------------------------------------\n\n")

    posicion = 1
    for tupla in ranking:
        vendedor = tupla[0]
        stats = estadisticas_vendedores[vendedor]
        archivo_resumen.write("  " + str(posicion) + ". " + vendedor + "\n")
        archivo_resumen.write("     Total vendido:  $" + str(stats["total"]) + "\n")
        archivo_resumen.write("     Promedio/venta: $" + str(round(stats["promedio"])) + "\n")
        archivo_resumen.write("     Venta mas alta: $" + str(stats["venta_max"]) + "\n")
        archivo_resumen.write("     Venta mas baja: $" + str(stats["venta_min"]) + "\n\n")
        posicion = posicion + 1

    archivo_resumen.write("=======================================================\n")
    archivo_resumen.write("  Vendedor del mes: " + vendedor_del_mes + "\n")
    archivo_resumen.write("=======================================================\n")

print("\nArchivos generados:")
print("  - resumen_ventas.txt")
print("  - alertas_ventas.txt")