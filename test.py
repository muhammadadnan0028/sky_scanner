import json

file = open('x.json', 'r')
data = json.loads(file.read())
file.close()

Price_Grid = data.get('PriceGrids', {})
r = []

for oneMonthGrid in Price_Grid.get('Grid'):
    for d in range(len(oneMonthGrid)):
        day = d + 1
        if oneMonthGrid[d].get('Direct'):
            price = oneMonthGrid[d].get('Direct').get('Price')
            pairs = oneMonthGrid[d].get('Direct').get('TraceRefs')
            
            # Extract and convert the dates from the 'Traces' values
            dates = [data['Traces'][pair].split('*')[-3] for pair in pairs]
            
            # Convert dates from 'YYYYMMDD' format to 'YYYY-MM-DD' format
            formatted_dates = [date[:4] + '-' + date[4:6] + '-' + date[6:] for date in dates]
            
            r.append({'price': price, 'dates': formatted_dates})

# Sort the list 'r' based on the 'price' field in ascending order
r_sorted = sorted(r, key=lambda x: x['price'])

for rr in r_sorted[:3]:
    print(rr)
