# Chukwumeka Agu
# 1871765

import datetime

# Opening file handles
manu = open('ManufacturerList.csv', 'r+')
manu_list = manu.readlines()

price = open('PriceList.csv', 'r+')
price_list = price.readlines()

service = open('ServiceDatesList.csv', 'r+')
service_list = service.readlines()

dataDictionary = dict()


# Creating object


class ProductData:
    ID = 0
    manufacturer = ""
    product = ""
    price = 0
    date = datetime.date.min
    damaged = ""

    # method for returning full inventory
    def tostring(self):
        return self.ID, self.manufacturer, self.product, self.price, self.date.strftime("%#m/%#d/%Y"), self.damaged

    # method for returning damaged inventory
    def damaged_to_string(self):
        return self.ID, self.manufacturer, self.product, self.price, self.date.strftime("%#m/%#d/%Y")

    # method for returning past service date inventory
    def past_to_string(self):
        return self.ID, self.manufacturer, self.product, self.price, self.date.strftime("%#m/%#d/%Y")

    # method for returning inventory by product type
    def product_to_string(self):
        return self.ID, self.manufacturer, self.price, self.date.strftime("%#m/%#d/%Y"), self.damaged


# Getting manufacturer data
for line in manu_list:
    # Remove /n in each line and change each line to a list of strings
    dataList = line.replace('\n', '').split(',')
    data = ProductData()
    for i in range(4):
        dataString = dataList[i].rstrip()
        if i == 0:
            data.ID = int(dataString)
        elif i == 1:
            data.manufacturer = dataString
        elif i == 2:
            data.product = dataString
        elif i == 3 and dataString == 'damaged':
            data.damaged = "damaged"
    # adding data's value into a dictionary so, it can be used outside of loop
    dataDictionary.update({data.ID: data})

for line in price_list:
    dataList = line.replace('\n', '').split(',')
    ID = 0
    price = 0
    for i in range(2):
        dataString = dataList[i].rstrip()
        if i == 0:
            ID = int(dataString)
        elif i == 1:
            price = int(dataString)

    data = ProductData()
    if ID in dataDictionary.keys():
        data = dataDictionary.get(ID)
    # Updating the Data object and thus the dictionary with the price
    data.price = price

for line in service_list:
    dataList = line.replace('\n', '').split(',')
    ID = 0
    date = datetime.date.min
    for i in range(2):
        dataString = dataList[i].rstrip()
        if i == 0:
            ID = int(dataString)
        elif i == 1:
            date = datetime.datetime.strptime(dataString, '%m/%d/%Y')
    data = ProductData()
    if ID in dataDictionary.keys():
        data = dataDictionary.get(ID)
    # adding data's value into a dictionary, so it can be used outside of loop
    data.date = date

# All previous code was copied from part 1
# -------------------------------------------------------------------------------------------------------------------

# New dictionary
second_dict = dict()

# Copy data from old dictionary to new
for key in dataDictionary.keys():
    second_dict.update({key:
                            {'ID': dataDictionary[key].ID,
                             'manufacturer': dataDictionary[key].manufacturer,
                             'type': dataDictionary[key].product,
                             'price': dataDictionary[key].price,
                             'date': dataDictionary[key].date,
                             'damage': dataDictionary[key].damaged
                             }
                        })

# Get input
manu_and_type = input("Give a manufacturer and type: ").split()
print()

# Use exceptions for error handling
while manu_and_type[0] != 'q':
    try:
        inputed_manu = ''

        inputed_type = ''

# match input with items in inventory
        for word in manu_and_type:
            for key in second_dict.keys():
                if word == second_dict[key]['manufacturer']:
                    inputed_manu = word
                if word == second_dict[key]['type']:
                    inputed_type = word

# Incase inputed information doesn't match inventory raise error
        if inputed_manu == '' or inputed_type == '':
            raise ValueError("No such item in inventory")

# Print out full information of the inputed item
        used_item = 0

        for key in second_dict.keys():
            if second_dict[key]['manufacturer'] == inputed_manu and second_dict[key]['type'] == inputed_type:
                if second_dict[key]['date'] < datetime.datetime.now() or second_dict[key]['damage'] == 'damaged':
                    break
                else:
                    print(f'Your item is: {key}, {second_dict[key]["manufacturer"]}, {second_dict[key]["type"]}, {second_dict[key]["price"]}')
                    print()
                    used_item = key
                    break

# Find items of the same type in inventory and add them to a new dictionary
        price_dict = dict()
        for key in second_dict.keys():
            if inputed_type == second_dict[key]['type']:
                if second_dict[key]['date'] >= datetime.datetime.now() and second_dict[key]['damage'] != 'damaged':
                    price_dict.update({key: second_dict[key]["price"]})

# Find the closest price out Of the values in the new dictionary
        closest_item = 0
        closest_value = 10000000
        for key in price_dict.keys():
            if abs(price_dict[key] - price_dict[used_item]) < closest_value and key != used_item:
                closest_item = key
                closest_value = abs(price_dict[key] - price_dict[used_item])

#  Print the full value of the closest item
        print(f'You may also consider: {closest_item}, {second_dict[closest_item]["manufacturer"]}, {second_dict[closest_item]["type"]}, {second_dict[closest_item]["price"]}')
        print()

    except ValueError as ex:
        print(ex)
    except:
        print("No such item in inventory")

# Restart query
    manu_and_type = input("Give a manufacturer and type or write 'q' to quit: ").split()