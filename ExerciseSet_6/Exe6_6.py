import sys

def pizza_price(pizza_diameter, unit_price):

    area_pizza = 3.143 * (pizza_diameter/2)**2
    single = unit_price/ area_pizza
    return single


size_rosapizza = int(input("Enter the diameter size of Rosa pizza:..."))
size_hutpizza = int(input("Enter the diameter size of Hut pizza:..."))
price_rosapizza = float(input("Enter the price of the Rosa pizza option:..."))
price_hutpizza = float(input("Enter the price of the Hut pizza option:..."))

rosapizza = pizza_price(size_rosapizza, price_rosapizza)
hutpizza = pizza_price(size_hutpizza, price_hutpizza)

print(f"{rosapizza:.2f} euro per m2")
print(f"{hutpizza:.2f} euro per m2")

if rosapizza < hutpizza:
    print("Rosa Pizza has a much lower unit price")
else:
    print("Hut Pizza has a much lower unit price")



sys.exit(0)