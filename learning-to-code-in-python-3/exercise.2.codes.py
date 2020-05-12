#!/usr/bin/env python3

product_code = input("What is the product code?: ")
country, product, batch = product_code.split('-')

print("Country Code: ", country)
print("Product Code: ", product)
print("Batch Number: ", batch)