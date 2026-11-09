#!/usr/bin/env python3
import sys
import csv

for linea in sys.stdin:
    try:
        fila = next(csv.reader([linea]))

        if not fila or fila[0] == "instant":
            continue

        hora = int(fila[5])
        alquileres = int(fila[16])

        if 0 <= hora <= 23 and alquileres >= 0:
            print(f"{hora:02d}\t{alquileres}")

    except (ValueError, IndexError, StopIteration):
        continue

