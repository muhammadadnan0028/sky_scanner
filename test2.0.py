import requests
import json


file = open('city.json', 'r')
data = json.loads(file.read())
file.close()
country_destination = data.get("countryDestination")
results = country_destination.get("results")
sky_codes = []
city_names = []


for location in results:
    content = location.get("content")
    location_data = content.get("location")
    
    if location_data:
        sky_code = location_data.get("skyCode")
        sky_code = location_data.get("skyCode")
        city_name = location_data.get("name")
        if sky_code:
            sky_codes.append(sky_code)
        if sky_code:
            city_names.append(city_name)

for full_name in city_names:
    pass

for city in sky_codes:
    url = f"https://www.skyscanner.dk/g/monthviewservice/DK/DKK/da-DK/calendar/COPE/{city}/2023-09/2023-09/?profile=minimalmonthviewgridv2&apikey=6f4cb8367f544db99cd1e2ea86fb2627"

    response = requests.get(url)
    data = response.json()
    # print(data)

    Price_Grid = data.get('PriceGrids', {})
    r = []

    for oneMonthGrid in Price_Grid.get('Grid'):
        for d in range(len(oneMonthGrid)):
            day = d + 1
            if oneMonthGrid[d].get('Direct'):
                price = oneMonthGrid[d].get('Direct').get('Price')
                pairs = oneMonthGrid[d].get('Direct').get('TraceRefs')
                dates = [data['Traces'][pair].split('*')[-3] for pair in pairs]
                formatted_dates = [date[:4] + '-' + date[4:6] + '-' + date[6:] for date in dates]  
                r.append({'price': price, 'dates': formatted_dates})
    r_sorted = sorted(r, key=lambda x: x['price'])

    print(f"Top Results for {city}")
    for rr in r_sorted[:3]:
        print(rr)
