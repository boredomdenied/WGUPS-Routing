# map locations to addresses
from data import MyHash


# Big-O time complexity of O(n)
def map(truck):
    for i in truck.package_list:
        if MyHash.get(i).package_id == "1":
            MyHash.get(i).package_address_id = 5
            truck.location_list.add(5)
        elif MyHash.get(i).package_id == "2":
            MyHash.get(i).package_address_id = 9
            truck.location_list.add(9)
        elif MyHash.get(i).package_id == "3":
            MyHash.get(i).package_address_id = 8
            truck.location_list.add(8)
        elif MyHash.get(i).package_id == "4":
            MyHash.get(i).package_address_id = 18
            truck.location_list.add(18)
        elif MyHash.get(i).package_id == "5":
            MyHash.get(i).package_address_id = 19
            truck.location_list.add(19)
        elif MyHash.get(i).package_id == "6":
            MyHash.get(i).package_address_id = 13
            truck.location_list.add(13)
        elif MyHash.get(i).package_id == "7":
            MyHash.get(i).package_address_id = 2
            truck.location_list.add(2)
        elif MyHash.get(i).package_id == "8":
            MyHash.get(i).package_address_id = 12
            truck.location_list.add(12)
        elif MyHash.get(i).package_id == "9":
            MyHash.get(i).package_address_id = 12
            truck.location_list.add(12)
        elif MyHash.get(i).package_id == "10":
            MyHash.get(i).package_address_id = 25
            truck.location_list.add(25)
        elif MyHash.get(i).package_id == "11":
            MyHash.get(i).package_address_id = 10
            truck.location_list.add(10)
        elif MyHash.get(i).package_id == "12":
            MyHash.get(i).package_address_id = 16
            truck.location_list.add(16)
        elif MyHash.get(i).package_id == "13":
            MyHash.get(i).package_address_id = 6
            truck.location_list.add(6)
        elif MyHash.get(i).package_id == "14":
            MyHash.get(i).package_address_id = 20
            truck.location_list.add(20)
        elif MyHash.get(i).package_id == "15":
            MyHash.get(i).package_address_id = 21
            truck.location_list.add(21)
        elif MyHash.get(i).package_id == "16":
            MyHash.get(i).package_address_id = 21
            truck.location_list.add(21)
        elif MyHash.get(i).package_id == "17":
            MyHash.get(i).package_address_id = 14
            truck.location_list.add(14)
        elif MyHash.get(i).package_id == "18":
            MyHash.get(i).package_address_id = 3
            truck.location_list.add(3)
        elif MyHash.get(i).package_id == "19":
            MyHash.get(i).package_address_id = 4
            truck.location_list.add(4)
        elif MyHash.get(i).package_id == "20":
            MyHash.get(i).package_address_id = 17
            truck.location_list.add(17)
        elif MyHash.get(i).package_id == "21":
            MyHash.get(i).package_address_id = 17
            truck.location_list.add(17)
        elif MyHash.get(i).package_id == "22":
            MyHash.get(i).package_address_id = 26
            truck.location_list.add(26)
        elif MyHash.get(i).package_id == "23":
            MyHash.get(i).package_address_id = 23
            truck.location_list.add(23)
        elif MyHash.get(i).package_id == "24":
            MyHash.get(i).package_address_id = 22
            truck.location_list.add(22)
        elif MyHash.get(i).package_id == "25":
            MyHash.get(i).package_address_id = 24
            truck.location_list.add(24)
        elif MyHash.get(i).package_id == "26":
            MyHash.get(i).package_address_id = 24
            truck.location_list.add(24)
        elif MyHash.get(i).package_id == "27":
            MyHash.get(i).package_address_id = 1
            truck.location_list.add(1)
        elif MyHash.get(i).package_id == "28":
            MyHash.get(i).package_address_id = 11
            truck.location_list.add(11)
        elif MyHash.get(i).package_id == "29":
            MyHash.get(i).package_address_id = 2
            truck.location_list.add(2)
        elif MyHash.get(i).package_id == "30":
            MyHash.get(i).package_address_id = 12
            truck.location_list.add(12)
        elif MyHash.get(i).package_id == "31":
            MyHash.get(i).package_address_id = 15
            truck.location_list.add(15)
        elif MyHash.get(i).package_id == "32":
            MyHash.get(i).package_address_id = 15
            truck.location_list.add(15)
        elif MyHash.get(i).package_id == "33":
            MyHash.get(i).package_address_id = 9
            truck.location_list.add(9)
        elif MyHash.get(i).package_id == "34":
            MyHash.get(i).package_address_id = 21
            truck.location_list.add(21)
        elif MyHash.get(i).package_id == "35":
            MyHash.get(i).package_address_id = 1
            truck.location_list.add(1)
        elif MyHash.get(i).package_id == "36":
            MyHash.get(i).package_address_id = 7
            truck.location_list.add(7)
        elif MyHash.get(i).package_id == "37":
            MyHash.get(i).package_address_id = 19
            truck.location_list.add(19)
        elif MyHash.get(i).package_id == "38":
            MyHash.get(i).package_address_id = 19
            truck.location_list.add(19)
        elif MyHash.get(i).package_id == "39":
            MyHash.get(i).package_address_id = 6
            truck.location_list.add(6)
        elif MyHash.get(i).package_id == "40":
            MyHash.get(i).package_address_id = 18
            truck.location_list.add(18)

