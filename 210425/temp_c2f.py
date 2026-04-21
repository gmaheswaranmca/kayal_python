# convert temp in celcius to forenheit 
celcius = float(input('Temp in celcius:'))

forenheit = (celcius * (9 / 5)) + 32
print(f'Temp:{celcius}c')
print(f'Temp:{forenheit:0.1f}f')