def displayWelcome():
    print('This program converts convert one length unit into another unit')
    print('Following are the available units: (mm), (cm), (m), (km), (inches), (ft), (yds), (miles)')

def getConvertfrom():
    return raw_input('Which unit would you like to convert from: ')

def getConvertto():
    return raw_input('Which unit would you like to convert to: ')


num1 = float(raw_input('Enter a value: '))

available_units = ('mm', 'cm', 'm', 'km', 'inches', 'ft', 'yds', 'miles')
conversions = (1, 10, 1000, 1e6, 25.4, 304.8, 914.4, 1.609344e6)

# Display program welcome
displayWelcome()

# Get which conversion
which1 = getConvertfrom()
which2 = getConvertto()

index = 0
for i in range (0, len(available_units)):
    print available_units[i], '==', str(which1)
    if available_units[i] == str(which1):
        num_in_mm = num1 * conversions[i]

for j in range (0, len(available_units)):
    if available_units[j] == str(which2):
        num2 = num_in_mm / conversions[j]

print(num1, which1, "is equal to", num2, which2)