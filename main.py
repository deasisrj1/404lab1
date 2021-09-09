import requests

print('requests version number {0}'.format(requests.__version__))

response = requests.get('http://www.google.com')

print(response)
print(response.content)

response = requests.get('https://raw.githubusercontent.com/deasisrj1/404lab1/master/main.py')

print(response)
print(response.content)
