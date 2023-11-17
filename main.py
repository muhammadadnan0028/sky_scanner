import requests

# Replace this URL with the correct one
# url = "https://www.skyscanner.dk/g/monthviewservice/DK/DKK/da-DK/calendar/CPH/THES/2023-09/2023-10/?profile=minimalmonthviewgridv2&apikey=6f4cb8367f544db99cd1e2ea86fb2627"  # Replace with your actual URL

# response = requests.get(url)
# data = response.json()
# print(data)
# exit(1)
import json

file = open('x.json','r')
data = json.loads(file.read())
file.close()

Price_Grid = data.get('PriceGrids',{})
r = []
for oneMonthGrid in Price_Grid.get('Grid'):
    for d in range(len(oneMonthGrid)):
        day = d + 1
        if oneMonthGrid[d].get('Direct'):
            price = oneMonthGrid[d].get('Direct').get('Price')
            pairs = oneMonthGrid[d].get('Direct').get('TraceRefs')
            r.append({'price': price,'dates': pairs})

for rr in r:
    print(rr)

# Traces = data.get('Traces')
# for key, value in Traces.items():
#     parts = value.split('*')
#     print(f"'{key}':{parts[4]}")