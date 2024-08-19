# -*- coding: utf-8 -*-
"""
Created on Fri May 19 10:29:36 2023

@author: Santi
"""

import csv

def parse_csv_row(row):
    # Parse a single row of the CSV file and return a dictionary
    if len(row) != 2:
        raise ValueError("Invalid row format: Each row should have exactly two elements")
    key = row[0]
    value = float(row[1])
    return (key, value)

def leer_precios(arch):
    precios = []
    try:
        with open(arch, 'rt', encoding='utf8') as f:
            reader = csv.reader(f)
            for row in reader:
                try:
                    price_entry = parse_csv_row(row)
                    precios.append(price_entry)
                except (ValueError, TypeError) as e:
                    print(f"Skipping invalid row: {row}. Error: {e}")
    except IOError as e:
        print(f"Error opening file: {e}")
    precios = dict(precios)
    return precios


def process_line(line, line_number):
    if len(line) != 3:
        raise ValueError(f"Invalid number of columns in line {line_number}")
    try:
        return {
            'nombre': line[0],
            'cajones': int(line[1]),
            'precio': float(line[2])
        }
    except (ValueError, TypeError):
        raise ValueError(f"Invalid data in line {line_number}")


def leer_camion(arch):
    camion = []
    try:
        with open(arch, 'rt', encoding='utf8') as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header line
            for i, line in enumerate(reader, start=2): ## usa el start desde 2 para contabilizar desde dos las lineas (1 son los encabezados)
                try:
                    item = process_line(line, i)
                    camion.append(item)
                except ValueError as e:
                    print(e)
    except (FileNotFoundError, IOError) as e:
        print(f"Error opening or reading file: {e}")
    return camion