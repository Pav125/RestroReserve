from RestroReserve.wsgi import application

def handler(environ, start_response):
    return application(environ, start_response)
