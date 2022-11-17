import datetime
import csv

manu = open('ManufacturerList.csv', 'r+')
manu_list = manu.readlines()

price = open('PriceList.csv', 'r+')
price_list = price.readlines()

service = open('ServiceDatesList.csv', 'r+')
service_list = service.readlines()

dataDictionary = dict()


class ProductData:
    ID = 0
    manufacturer = ""
    product = ""
    price = 0
    date = datetime.date.min
    damaged = ""

    def tostring(self):
        return self.ID, self.manufacturer, self.product, self.price, self.date.strftime("%Y/%m/%d"), self.damaged


# Getting manufacturer data
for line in manu_list:
    # Remove /n in each line and change each line to a list of strings
    # rows
    dataList = line.replace('\n', '').split(',')
    # first object
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
    # adding data's value into a dictionary
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
    # creates object
    data = ProductData()
    if ID in dataDictionary.keys():
        data = dataDictionary.get(ID)
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
    data.date = date

write_handle = open('FullInventory.csv', 'w')
wf = csv.writer(write_handle)

for key in dataDictionary.keys():
    wf.writerow(dataDictionary[key].tostring())

write_handle.close()
