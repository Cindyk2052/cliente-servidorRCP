import xmlrpc.client

import datetime

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

print(proxy.list_contents('d:'))


today = proxy.today()
# convert the ISO8601 string to a datetime object
converted = datetime.datetime.strptime(today.value, "%Y%m%dT%H:%M:%S")
print("Hoy día: %s" % converted.strftime("%d.%m.%Y, %H:%M"))