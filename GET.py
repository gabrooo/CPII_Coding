import requests

try:
    print("=======================")
    print("--> Usuario/{id}")
    print("--> Products/{id}")
    print("--> Pedidos/{id}")
    print("=======================")
    endpoint = input("Endpoint: ")

    response = requests.get(f'http://127.0.0.1:5000/{endpoint.lower()}')

    if response.status_code == 200:
        tasks = response.json()
        print(tasks)
    elif response.status_code == 404:
        print('Endpoint Not Found')

except Exception as error:
    print(error)
