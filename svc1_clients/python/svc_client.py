import requests
from pprint import pprint

def main():
  cars = list_cars()
  show_cars(cars)
  car_id = input("What car do you want to see? (car id):")
  show_car_details(car_id)

def list_cars():
  url = 'http://localhost:6543/api/autos'

  resp = requests.get(url)
  if resp.status_code != 200:
    print("Error connecting to server.")
    print (f"Error: {resp.status_code}")
    return
  print (resp.status_code)
  cars = resp.json()
  return[
    (car.get('id'), car.get('name')) for car in cars.get('autos', [])
  ]
def get_car(car_id):
  url = f'http://localhost:6543/api/autos/{car_id}'
  print(f'Url[{url}]')
  resp = requests.get(url)
  if resp.status_code != 200:
    print("Error connecting to server.")
    print (f"Error: {resp.status_code}")
    return
  print (resp.status_code)
  car = resp.json()
  return car

def show_cars(cars):
  print("Cars for sale: ")
  for c in cars:
    print(f"{c[0]} : {c[1]}")

def show_car_details(car_id):
  car = get_car(car_id)
  if not car:
    print("Car not found.")
    return
  print("Car details:")
  pprint(car)



if __name__ == '__main__':
  main()