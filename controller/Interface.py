from data import MyHash


# Big-O time complexity of O(n)
def reset():
    for i in range(40):
        MyHash.get(i).package_delivery_status = "Not delivered"
        MyHash.get(i).package_delivery_time = 0


# Big-O time complexity of O(n^2)
def update(departure_time, distance, current_node):
    total_departure_time = ""
    for i in range(40):
        total = 0
        if MyHash.get(i).package_address_id == current_node:
            MyHash.get(i).package_delivery_status = "Delivered"
            while distance / .3 > 60:
                total += 100
                distance -= 18
            total += distance / .3
            if (total + departure_time) % 100 > 60:
                total += 40
            total_departure_time = int(total + departure_time)
            delivery_time = str(total_departure_time)[:-2] + ":" + str(total_departure_time)[-2:]
            MyHash.get(i).package_delivery_time = delivery_time


# Big-O time complexity of O(n)
# lookup function for single package corresponding to menu option [2]:
def find_package(package_id):
    for i in range(40):
        if int(MyHash.get(i).package_id) == int(package_id):
            print("\nPackage %s was %s to:\n%s\n%s, %s\nWith package weight of %skg at %s with deadline of %s" % (
                MyHash.get(i).package_id,
                MyHash.get(i).package_delivery_status,
                MyHash.get(i).package_address,
                MyHash.get(i).package_city,
                MyHash.get(i).package_zipcode,
                MyHash.get(i).package_weight,
                MyHash.get(i).package_delivery_time,
                MyHash.get(i).package_deadline))


# Big-O time complexity of O(n)
# lookup function for all packages corresponding to menu option [1]:
def find_all():
    for i in range(40):
        # uncomment following line to test only packages not delivered by time
        # if "Not" in MyHash.get(i).package_delivery_status:
        print("\nPackage %s was %s to:\n%s\n%s, %s\nWith package weight of %skg at %s with deadline of %s" % (
            MyHash.get(i).package_id,
            MyHash.get(i).package_delivery_status,
            MyHash.get(i).package_address,
            MyHash.get(i).package_city,
            MyHash.get(i).package_zipcode,
            MyHash.get(i).package_weight,
            MyHash.get(i).package_delivery_time,
            MyHash.get(i).package_deadline))


# Big-O time complexity of O(n)
# rubric I2: Verification of Algorithm
def verify():
    not_delivered = True
    for i in range(40):
        if "Not" in MyHash.get(i).package_delivery_status:
            print("\nPackage %s was %s to:\n%s\n%s, %s\nWith package weight of %s at %s with deadline of %s" % (
            MyHash.get(i).package_id,
            MyHash.get(i).package_delivery_status,
            MyHash.get(i).package_address,
            MyHash.get(i).package_city,
            MyHash.get(i).package_zipcode,
            MyHash.get(i).package_weight,
            MyHash.get(i).package_delivery_time,
            MyHash.get(i).package_deadline))
            not_delivered = False
    if not_delivered:
        print("All packages delivered on time")
