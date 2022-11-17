# Chukwumeka Agu
# 1871765

import datetime
import csv

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

# Part A
# Open file for writing
full_handle = open('FullInventory.csv', 'w')
ff = csv.writer(full_handle)

# Iterate through each item and write into file
for key in dataDictionary.keys():
    ff.writerow(dataDictionary[key].tostring())

full_handle.close()


# Part B

product_list = []

# Store each device type in a list
for key in dataDictionary.keys():
    if dataDictionary[key].product in product_list:
        continue
    else:
        product_list.append(dataDictionary[key].product)

# iterate through items
for key in dataDictionary.keys():
    # match item to a device type and then append item's details to file
    if dataDictionary[key].product == product_list[0]:
        file_name = f'{product_list[0]}Inventory.csv'
        append_handle = open(file_name, 'a')
        ah = csv.writer(append_handle)
        ah.writerow(dataDictionary[key].product_to_string())

    if dataDictionary[key].product == product_list[1]:
        file_name = f'{product_list[1]}Inventory.csv'
        append_handle = open(file_name, 'a')
        ah = csv.writer(append_handle)
        ah.writerow(dataDictionary[key].product_to_string())

    if dataDictionary[key].product == product_list[2]:
        file_name = f'{product_list[2]}Inventory.csv'
        append_handle = open(file_name, 'a')
        ah = csv.writer(append_handle)
        ah.writerow(dataDictionary[key].product_to_string())

# Part C
past_handle = open('PastServiceDateInventory.csv', 'w')
pf = csv.writer(past_handle)

# Iterate through each item, check if date is less than today, if so write item's details to file
for key in dataDictionary.keys():
    if dataDictionary[key].date < datetime.datetime.now():
        pf.writerow(dataDictionary[key].past_to_string())


past_handle.close()

# Part D
damage_handle = open('DamagedInventory.csv', 'w')
df = csv.writer(damage_handle)

# Iterate through each item, if it is damaged, write its details to a file
for key in dataDictionary.keys():
    if dataDictionary[key].damaged == "damaged":
        df.writerow(dataDictionary[key].damaged_to_string())

damage_handle.close()
