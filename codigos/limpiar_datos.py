import csv

entrada = "hour.csv"
salida = "hour_limpio.csv"

procesados = 0
eliminados = 0

with open(entrada, newline="", encoding="utf-8") as origen, \
     open(salida, "w", newline="", encoding="utf-8") as destino:

    lector = csv.DictReader(origen)
    columnas = lector.fieldnames
    escritor = csv.DictWriter(destino, fieldnames=columnas)

    escritor.writeheader()

    for fila in lector:
        procesados += 1

        try:
            hora = int(fila["hr"])
            alquileres = int(fila["cnt"])

            campos_completos = all(
                valor is not None and valor.strip() != ""
                for valor in fila.values()
            )

            if not campos_completos:
                eliminados += 1
                continue

            if not 0 <= hora <= 23 or alquileres < 0:
                eliminados += 1
                continue

            escritor.writerow(fila)

        except (ValueError, TypeError):
            eliminados += 1

print("Registros revisados:", procesados)
print("Registros eliminados:", eliminados)
print("Registros conservados:", procesados - eliminados)
print("Archivo generado:", salida)
