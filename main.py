import requests

print('requests version number {0}'.format(requests.__version__))

response = requests.get('http://www.google.com')

print(response)
