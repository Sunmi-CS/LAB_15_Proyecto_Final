#!/usr/bin/env python3
import sys

hora_actual = None
total = 0

for linea in sys.stdin:
    linea = linea.strip()

    if not linea:
        continue

    try:
        hora, alquileres = linea.split("\t")
        alquileres = int(alquileres)

    except ValueError:
        continue

    if hora_actual is not None and hora != hora_actual:
        print(f"{hora_actual}\t{total}")
        total = 0

    hora_actual = hora
    total += alquileres

if hora_actual is not None:
    print(f"{hora_actual}\t{total}")
