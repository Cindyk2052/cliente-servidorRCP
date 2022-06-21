from xmlrpc.server import SimpleXMLRPCServer

import logging
import os

import datetime
import xmlrpc.client

logging.basicConfig(level=logging.INFO)

server=SimpleXMLRPCServer(
    ('localhost',8000),
    logRequests=True
)

def list_contents(dir_name):
    logging.info('list_contents(%s)', dir_name)
    return os.listdir(dir_name)

server.register_function(list_contents)

def today():
    today = datetime.datetime.today()
    return xmlrpc.client.DateTime(today)

print("Listening on port 8000...")
server.register_function(today, "today")


try:    
    print('presione Ctrl+C para salir')
    server.serve_forever()
except KeyboardInterrupt:
    print('saliendo')

