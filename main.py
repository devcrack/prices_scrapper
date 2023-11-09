# stdlib
from time import sleep
import csv
from io import StringIO
# 3rd-party 
import pandas as pd
from bardapi import Bard

name_file = 'prices.csv'
token = 'cwjtEUYZyHRE9qf-NTZaloN1LSGjyWmaDUcnWQ8szKFK_TlYsz9EAKrWMapFugEjGeygeA.'
bard = Bard(token=token)


def create_input_prompt(product_to_search):
    ans = bard.get_answer(
        f'Precios de: {product_to_search} en Peru. Un maximo de 4 resultados '
        f'en lista en la forma: producto-proveedor-precio.')['content']
    sleep(1)
    print(ans)
    return str(ans)


def get_rows(raw_data):
    data = []
    for element in raw_data:
        data.append(
            [k for k in element.split('|') if k]
        )
    return data

def get_product_prices():
    list_products = ['SOGA DE NAILON 1/4 IN X 100 M',
                     'PLASTICO POLIETILENO 12 µM X 1.50 M X 100 M COLOR AZUL',
                     'SOGA DE NAILON 5/8 IN X 30 M',
                     'PABILO N° 20 X 500 G',
                     'SOGA DE NAILON 3/4 IN X 100 M',
                     'PABILO N° 20 X 1 kg',
                     'SOGA DE NAILON 1/2 IN X 100 M',
                     'RAFIA PLANA X 3 kg',
                     'BOLSA DE PAPEL KRAFT 25 cm X 35 cm APROX.',
                     'BOLSA DE POLIETILENO DE 1.20 m X 60 cm',
                     'BOLSA DE POLIETILENO 20 cm X 35 cm APROX.',
                     'PELICULA EXTENSIBLE PARA EMBALAJE (FILM STRECH) DE 50 cm X 255 m',
                     'BOLSA DE BIOPLÁSTICO 52 µM X 36 IN X 42 IN',
                     'SACO DE POLIPROPILENO 60.96 CM X 1.01 M (24 IN X 40 IN) APROX',
                     'DRIZA 3/4 IN',
                     'BOLSA DE BIOPLÁSTICO 52 µM X 36 IN X 42 IN',
                     'PABILO 10 HEBRAS X 250 G APROX.',
                     'SACO DE POLIPROPILENO 90 cm X 55 cm APROX.',
                     'SOGA DE NAILON 1/4 IN X 100 M',
                     'SOGA DE NAILON 5/8 IN X 30 M',
                     'PABILO N° 20 X 500 G',
                     'PLASTICO POLIETILENO 12 µM X 1.50 M X 100 M COLOR AZUL',
                     'CARTON CORRUGADO PLASTIFICADO 3 mm X 1 m X 2 m',
                     'BOLSA DE POLIETILENO CON FUELLE DE 40 in X 36 in COLOR NEGRO',
                     'PARIHUELA DE MADERA 10 cm X 1.00 m X 1.20 m APROX.',
                     'SACO DE POLIPROPILENO 51 CM X 76 CM',
                     'PELÍCULA EXTENSIBLE PARA EMBALAJE (FILM STRECH) 18 IN X 264 M APROX.']


    with open(name_file, 'w', newline='', encoding='utf-8') as a_file:
        write = csv.writer(a_file)

        for product in list_products:
            ans = create_input_prompt(product)
            table_lines = ans.split('\n')
            raw_data = [k for k in table_lines if '|' in k]
            data = [[k for k in j.split('|') if k] for j in raw_data]
            # data = get_rows(raw_data)
            for fila in data:
                write.writerow(fila)
            sleep(8)


if __name__ == '__main__':
    get_product_prices()
