# Chukwuemeka Agu
# 1871765

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print ("Car wash -- $7")
print("Car wax -- $12")
print()

first_service = input("Select first service:\n")
second_service = input("Select second service:\n")
print()

dict_services = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12}

print("Davy's auto shop invoice")
print()
if first_service == '-':
    print("Service 1: No service")
else:
    print(f'Service 1: {first_service}, ${dict_services[first_service]}')

if second_service == '-':
    print("Service 2: No service")
else:
    print(f'Service 2: {second_service}, ${dict_services[second_service]}')
print()

total = 0
if first_service == '-':
   if second_service == '-':
        print("Total: $0")
   else:
       print(f'Total: ${dict_services[second_service]}')
else:
    if second_service == '-':
        print(f'Total: ${dict_services[first_service]}')
    else:
        print(f'Total: ${dict_services[first_service] + dict_services[second_service]}')

