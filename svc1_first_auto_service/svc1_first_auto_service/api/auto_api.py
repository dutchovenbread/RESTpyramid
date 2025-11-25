from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config
from svc1_first_auto_service.data.repository import Repository


@view_config(route_name='autos_api',
             request_method='GET', 
             renderer='json')
def all_autos(_):
    cars = Repository.all_cars(limit=25)
    return cars

@view_config(route_name='auto_api',
             request_method='GET', 
             renderer='json')
def single_auto(request : Request):
    car_id = request.matchdict.get('car_id')
    car = Repository.car_by_id(car_id)
    if not car:
      msg = f"Car with id {car_id} not found"
      return Response(status=404, json_body={'error': msg})
    return car

@view_config(route_name='autos_api',
             request_method='POST', 
             renderer='json')
def create_auto(request : Request):
  try:
    car_data = request.json_body
  except:
    return Response(status=400, body="Could not parse your post as JSON.")
  # TODO: Validate
  try:
    car_data = Repository.add_car(car_data)
    return Response(json_body=car_data, status=201)
  except:
    return Response(status=400, body="Could not save car.")

@view_config(route_name='auto_api',
             request_method='PUT')
def update_auto(request : Request):
  car_id = request.matchdict.get('car_id')
  car = Repository.car_by_id(car_id)
  if not car:
    msg = f"Car with id {car_id} not found"
    return Response(status=404, json_body={'error': msg})
  
  try:
    car_data = request.json_body
  except:
    return Response(status=400, body="Could not parse your post as JSON.")
  # TODO: Validate
  try:
    car_data = Repository.update_car(car_id, car_data)
    return Response(status=204, body="Car updated successfully.")
  except:
    return Response(status=400, body="Could not update car.")

@view_config(route_name='auto_api',
             request_method='DELETE')
def delete_auto(request : Request):
  car_id = request.matchdict.get('car_id')
  car = Repository.car_by_id(car_id)
  if not car:
    msg = f"Car with id {car_id} not found"
    return Response(status=404, json_body={'error': msg})
  
  
  # TODO: Validate
  try:
    Repository.delete_car(car_id)
    return Response(status=204, body="Car deleted successfully.")
  except:
    return Response(status=400, body="Could not delete car.")