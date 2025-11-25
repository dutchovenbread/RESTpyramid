import csv
import os
import uuid

from svc1_first_auto_service.data.car import Car

class Repository:
  __car_data = {}

  @classmethod
  def all_cars(cls, limit=None):
    cls.__load_data()
    cars = list(cls.__car_data.values())
    if limit:
      cars = cars[:limit]
    return cars
  
  @classmethod
  def car_by_id(cls, car_id):
    cls.__load_data()
    return cls.__car_data.get(car_id)
  
  @classmethod
  def add_car(cls, car):
    key = str(uuid.uuid4())
    car.id = key
    cls.__car_data[key] = car
    return car
  
  @classmethod
  def update_car(cls, car):
    key = car.id
    cls.__car_data[key] = car
    return car
  
  @classmethod
  def __load_data(cls):
    if cls.__car_data:
      return
    file = os.path.join(
      os.path.dirname(__file__),
      'opel.csv'
    )
    with open(file, 'r', encoding='utf-8') as fin:
      reader = csv.DictReader(fin)
      for row in reader:
        key = str(uuid.uuid4())
        row['id'] = key
        cls.__car_data[key] = Car(**row)
  @classmethod
  def delete_car(cls, car_id):
    del cls.__car_data[car_id]