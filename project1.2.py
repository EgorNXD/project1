print('Enter gasoline volume in gallons:')
gas_gallons = float(input())
gas_liters = gas_gallons*3.785
oil_barrels = gas_gallons/19.5
co2_pounds = gas_gallons*20
gas_energy = gas_gallons*115000
ethanol_energy = 75700
gas_price = gas_gallons*3
print('Gas in liters:')
print(gas_liters)
print('Oil in barrels:')
print(oil_barrels)
print('CO2 in pounds:')
print(co2_pounds)
print('Equivalent of ethanol in gallons:')
print(gas_energy/ethanol_energy)
print('Gas price in USD')
print(gas_price)

average_cons = 100
novosibirsk_cons = round(average_cons*1567000/30)
russia_cons = average_cons*143400000*12
print('Average gas consumption per month in liters:')
print(average_cons)
print('Novosibirsk gas consumption per day in liters:')
print(novosibirsk_cons)
print('Russia gas consumption per year in liters:')
print(russia_cons)
