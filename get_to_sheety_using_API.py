import requests
import json
from dotenv import load_dotenv
import os

url = 'https://api.sheety.co/072d5d087972183dfc8e833e3ad4701c/productBasicDetailReetika/products'


load_dotenv()


api_key = os.getenv('API_KEY')
headers = {

    'Authorization': api_key
}

# body = {
#     "product": {
       
#         "Name": "reetika",
#         "price": 10.99,
#         "Short Description":"programmer",
#         "Website":"abc.com",
#         "Votes":"1000",
#         "Icon URL":"URLADDRESS",
#         "category":"person"
#     }
# }

response = requests.get(url,headers=headers)


if response.status_code == 200:
    data = response.json()
    
    print(data)
else:
    print(f'Error: {response.status_code}')