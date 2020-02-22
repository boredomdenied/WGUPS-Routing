from algo import NearestNeighbor
from controller import Interface
from init import AddressId
from view import MainMenu, GetTime, GetPackage


# Big-O time complexity of O(1)
def init(truck_list, arr):
    while True:
        Interface.reset()
        main_menu_input = MainMenu.view()
        if main_menu_input == "1":
            user_time = GetTime.view()
            lookup_all(user_time, truck_list, arr)
        elif main_menu_input == "2":
            user_time = GetTime.view()
            user_package = GetPackage.view()
            lookup_package(user_time, truck_list, user_package, arr)
        elif main_menu_input == "3":
            verify("1700", truck_list, arr)
        elif main_menu_input == "4":
            break
        else:
            print("Invalid choice, please choose numerical values 1 - 5 on the keyboard")
            init(truck_list, arr)


# Big-O time complexity of O(n)
def lookup_all(current_time, truck_list, arr):
    for truck in truck_list:
        check_time(current_time, truck, arr)
    Interface.find_all()


# Big-O time complexity of O(n)
def lookup_package(current_time, truck_list, current_package, arr):
    for truck in truck_list:
        if int(current_package) in truck.package_list:
            check_time(current_time, truck, arr)
            break
    Interface.find_package(current_package)


# Big-O time complexity of O(n)
def verify(current_time, truck_list, arr):
    final_total = 0
    for truck in truck_list:
        final_path, total = check_time(current_time, truck, arr)
        print("Path for truck ", truck.truck_id, final_path)
        print("Total distance traveled for", truck.truck_id, "is: ", total)
        final_total += total
    Interface.verify()
    print("total mileage is:", final_total)


# Big-O time complexity of O(n)
def check_time(current_time, truck, arr):
    # need to remap address Id for truck due to multiple menu selections
    if len(truck.location_list) == 0:
        AddressId.map(truck)
    if int(current_time) > 100 & int(current_time) < 2360:
        distance = 0
        time_difference = int(current_time) - int(truck.departure_time)
        while time_difference >= 100:
            distance += 18
            time_difference -= 100
        distance += time_difference * .3
        final_path, total = NearestNeighbor.run(arr, truck.location_list, truck.departure_time, distance)
    else:
        print("Please enter a correct time in HHMM format")
        response = GetTime.view()
        lookup_all(response, truck, arr)
    return final_path, total
