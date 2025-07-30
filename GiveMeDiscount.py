def discount(price, disc):
    discounted_price = price - (price*disc)/100
    return discounted_price

price = float(input("Enter price: "))
disc = float(input("Enter discount: "))

print(discount(price,disc))