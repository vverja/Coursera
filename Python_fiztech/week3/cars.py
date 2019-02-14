import csv
from os import path


class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        return path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name,carrying, passenger_seats_count):
        super().__init__('car', brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__('truck', brand, photo_file_name, carrying)
        self.body_length = 0
        self.body_width = 0
        self.body_height = 0

        self.body_definition(body_whl)

    def body_definition(self, body_whl):
        if body_whl:
            self.body_length, self.body_width, self.body_height = map(lambda x: float(x), body_whl.split('x'))

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__('spec_machine', brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    try:
        with open(csv_filename) as csv_fd:
            reader = csv.DictReader(csv_fd, delimiter=';')
            for row in reader:
                car = create_car_instance(row)
                if car:
                    car_list.append(car)
            return car_list
    except IOError:
        print('Wrong filename!')
        return None


def create_car_instance(row):
    car_type = row['car_type']
    brand = row['brand']
    photo_file_name = row['photo_file_name']
    carrying = float(row['carrying'] or 0)

    if car_type == 'car':
        passenger = int(row['passenger_seats_count'] or 0)
        return Car(brand, photo_file_name, carrying, passenger)
    elif car_type == 'truck':
        return Truck(brand, photo_file_name, carrying, row['body_whl'])
    elif car_type == 'spec_machine':
        return SpecMachine(brand, photo_file_name, carrying, row['extra'])
    else:
        return None
