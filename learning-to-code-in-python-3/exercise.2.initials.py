#!/usr/bin/env python3

first_name = input("What is your first name?: ")
middle_name = input("What is your middle name?: ")
last_name = input("What is your last name?: ")

print( f"Your initials are {first_name[0]}.{middle_name[0]}.{last_name[0]}" )

product_code = input("What is the product code?: ")
country, product, batch = product_code.split('-')

print("Country Code: ", country)
print("Product Code: ", product)
print("Batch Number: ", batch)