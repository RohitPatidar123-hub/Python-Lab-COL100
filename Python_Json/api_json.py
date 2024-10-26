# import json
# from urllib.request import urlopen

# with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
#     source = response.read()

# print(source)    
import json
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=INR&apikey=YOUR_API_KEY"


with urlopen(url) as response :
     print("Actual response :",response)
     source =response.read()
     print(" Response After reading format:",source)
#print(source)     
data =json.loads(source)

#print("after loading inoto :",data)

print(json.dumps(data ,indent =2))
print(data["Realtime Currency Exchange Rate"])
