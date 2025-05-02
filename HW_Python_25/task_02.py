# Напишите программу, которая будет считывать данные о продуктах из файла и
# использовать аннотации типов для аргументов и возвращаемых значений функций.
# Создайте текстовый файл "products.txt", в котором каждая строка будет содержать
# информацию о продукте в формате "название, цена, количество". Например:
# Apple, 1.50, 10
# Banana, 0.75, 15
# В программе определите функцию calculate_total_price, которая будет принимать список
# продуктов и возвращать общую стоимость. Продумайте, какая аннотация должна быть у
# аргумента! Считайте данные из файла, разделите строки на составляющие и создайте
# список продуктов. Затем вызовите функцию calculate_total_price с этим списком и выведите
# результат.

from typing import List, Tuple

def read_product_from_file(filename: str) -> List[Tuple[str,float,int]]:
    products = []
    with open(filename,'r',encoding='utf-8') as file:
        for line in file:
            name, price, quantity = line.strip().split(', ')
            products.append((name,float(price),int(quantity)))
    return products

def calculate_total_price(products: List[Tuple[str, float, int]]) -> float:
    total: float = 0.0
    for name, price, quantity in products:
        total += price * quantity
    return total


if __name__ == "__main__":
    my_products = read_product_from_file("products.txt")
    total_price = calculate_total_price(my_products)
    print(f"Общая сумма всех продуктов: {total_price:.2f}")



