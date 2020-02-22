# Brandon Chapman SID: 001268864
# Please see report.txt file for rubric specific documentation

from controller import MenuController
from init import Packages, AddressId
from data import Matrix
from model.Truck import Truck


# build packages
Packages.build()


# build initial matrix with distance data
arr = Matrix.build()


# Big-O time complexity of O(1)
# Load trucks with packages
# Truck 1 packages
# 14, 15, 16, 19, 20 must be delivered together
truck1 = Truck(1, [14, 15, 16, 19, 20, 17, 12, 7, 29, 1, 27, 35, 2, 33], 800)


# Big-O time complexity of O(1)
# Truck 2 packages
# Packages must go on truck2: 3, 18, 36, 38
truck2 = Truck(2, [30, 3, 18, 36, 38, 22, 4, 40, 21, 24, 10], 800)


# Big-O time complexity of O(1)
# Truck 3 packages
# Packages delayed until 905, truck sits until then: 6, 25, 28, 32
truck3 = Truck(3, [13, 31, 6, 25, 28, 32, 34, 39, 26, 11, 23, 37, 5, 9, 8], 910)


# Big-O time complexity of O(1)
# make list of trucks for convenience
truck_list = [truck1, truck2, truck3]

# Big-O time complexity of O(n)
# build truck route from package_list
# Map address_id to packages
for truck in truck_list:
    AddressId.map(truck)
    # uncomment following line to view package size of each vehicle
    # print("Package size of Truck", truck.truck_id,  "is:", len(truck.package_list))


# test deliveries at given time
# G1 test simulates state of packages at 9:05AM
# MenuController.lookup_all("905", truck_list, arr)

# G2 test simulates state of packages at 10:00AM
# MenuController.lookup_all("1000", truck_list, arr)

# G3 test simulates state of packages at 12:00AM
# MenuController.lookup_all("1200", truck_list, arr)

MenuController.init(truck_list, arr)

