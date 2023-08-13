import json
import csv

f1 = open('data1.json')
data1 = json.load(f1)

f2 = open('data2.json')
data2 = json.load(f2)

labels = ['id', 'name', 'brand', 'price', 'variety',
          'volume', 'quantity', 'alcohol', 'container', 'origin']

a = data1['results'][112]['raw']
print(a)

with open('beers.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(labels)
    for entry in data1['results']:
        i = entry['raw']
        c = i['ec_category_filter'][0].split('|')

        try:
            volume = i['lcbo_unit_volume'].split('x')[-1]
        except KeyError:
            volume = 'NA'

        row = [i['permanentid'], i['title'], i.get('ec_brand', 'NA'), i['ec_price'], c[2:], volume,
               i.get('lcbo_bottles_per_pack', 'NA'), i.get('lcbo_alcohol_percent', 'NA'),
               i.get('lcbo_selling_package_name', 'NA'), i.get('country_of_manufacture', 'NA')
               ]
        writer.writerow(row)

    for entry in data2['results']:
        i = entry['raw']
        c = i['ec_category_filter'][0].split('|')

        try:
            volume = i['lcbo_unit_volume'].split('x')[-1]
        except KeyError:
            volume = 'NA'

        row = [i['permanentid'], i['title'], i.get('ec_brand', 'NA'), i['ec_price'], c[2:], volume,
               i.get('lcbo_bottles_per_pack', 'NA'), i.get('lcbo_alcohol_percent', 'NA'),
               i.get('lcbo_selling_package_name', 'NA'), i.get('country_of_manufacture', 'NA')
               ]
        writer.writerow(row)


