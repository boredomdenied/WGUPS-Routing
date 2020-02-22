class Package:
    def __init__(self, package):
        self.package_id = package[0]
        self.package_address_id = 0
        self.package_address = package[1]
        self.package_city = package[2]
        self.package_state = package[3]
        self.package_zipcode = package[4]
        self.package_deadline = package[5]
        self.package_weight = package[6]
        self.package_special_notes = package[7]
        self.package_delivery_status = "Not delivered"
        self.package_delivery_time = 0
