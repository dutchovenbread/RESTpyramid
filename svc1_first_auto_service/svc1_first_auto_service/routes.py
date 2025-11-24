def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=1)
    config.add_route('home', '/')
    config.add_route('autos_api', '/api/autos')
    config.add_route('auto_api', '/api/autos/{car_id}')
