from pyramid.config import Configurator
from pyramid.events import NewRequest


def main(global_config, **settings):
  """ This function returns a Pyramid WSGI application.
  """
  with Configurator(settings=settings) as config:
    allow_cors(config)
    config.include('pyramid_chameleon')
    config.include('.routes')
    config.scan()
  return config.make_wsgi_app()

def allow_cors(config):
  def add_cors_headers_response_callback(event):
    def cors_headers(request, response):
      response.headers.update({
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
        'Access-Control-Allow-Headers': 'Origin,Content-Type, Authorization',
        'Access-Control-Allow-Credentials': 'true',
        'Access-Control-Max-Age': '3600',
      })
    event.request.add_response_callback(cors_headers)
  config.add_subscriber(add_cors_headers_response_callback, NewRequest)