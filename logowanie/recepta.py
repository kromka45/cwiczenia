import requests
import json



skladniki = input('podaj skladnk')
querystr = input("co chcesz wyszukac ?")
response = requests.get(f'http://www.recipepuppy.com/api/?i={skladniki}&q={querystr}')
if (response.status_code != requests.codes.ok):
    print('cos nie tak')
else:
    print(json.dumps(response.json(),indent=4))