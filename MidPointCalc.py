price_paid_a = float(input("What is the price paid at point A? "))
price_paid_b = float(input("What is the price paid at point B? "))
price_rec_a = float(input("What is the price recieved at point A? "))
price_rec_b = float(input("What is the price recieved at point B? "))
quantity_demanded_a = float(input("What is the quantity demanded at point A? "))
quantity_demanded_b = float(input("What is the quantity demanded at point B? "))
quantity_supplied_a = float(input("What is the quantity supplied at point A? "))
quantity_supplied_b = float(input("What is the quantity supplied at point B? "))

# Calculate percent changes using the midpoint formula
pct_change_price_paid = (price_paid_a - price_paid_b) / ((price_paid_a + price_paid_b) / 2)
pct_change_price_rec = (price_rec_a - price_rec_b) / ((price_rec_a + price_rec_b) / 2)

pct_change_qd = (quantity_demanded_a - quantity_demanded_b) / ((quantity_demanded_a + quantity_demanded_b) / 2)
price_elasticity_of_demand = pct_change_qd / pct_change_price_paid

pct_change_qs = (quantity_supplied_a - quantity_supplied_b) / ((quantity_supplied_a + quantity_supplied_b) / 2)
price_elasticity_of_supply = pct_change_qs / pct_change_price_rec

print(f"Price elasticity of demand is {price_elasticity_of_demand}")
print(f"Price elasticity of supply is {price_elasticity_of_supply}")