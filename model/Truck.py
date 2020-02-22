class Truck:
    def __init__(self, truck_id, package_list, departure_time):
        self.truck_id = truck_id
        self.departure_time = departure_time
        self.package_list = package_list
        self.location_list = set()
