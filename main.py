# stdlib
from time import sleep
import csv
# 3rd-party
from bardapi import Bard

name_file = 'prices.csv'
token = 'YOUR_TOKEN'
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
    list_products = []


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
