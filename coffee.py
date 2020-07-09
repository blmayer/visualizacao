#!/usr/bin/env python3
import csv
import json

coffees = []
with open('brazil-coffee.csv') as csv_file:
    headers = csv_file.readline().split(',')
    reader = csv.DictReader(csv_file, fieldnames=headers)
    for line in reader:
        if line['Variety'] == "":
            line['Variety'] = 'Standard'
        coffees.append(dict(line))


keys = ['Aroma', 'Flavor', 'Aftertaste', 'Acidity', 'Body',
        'Balance', 'Uniformity', 'Moisture', 'Sweetness', 'Clean.Cup']
groups = {x: {k: [] for k in keys}
          for x in set([x['Variety'] for x in coffees])}

# Get values
for v in coffees:
    for k in keys:
        groups[v['Variety']][k].append(float(v[k]))

# Tranform into mean
for g, v in groups.items():

    groups[g] = {k: sum(v[k])/len(v[k]) for k in keys}

# print(groups)
val_range = {
    k: [
        max([g[k] for g in groups.values()])*1.01,
        min([g[k] for g in groups.values()])*.98
    ]
    for k in keys
}

# Write in format
json.dump(
    {
        'varieties': list(groups.keys()),
        'reviews': [
            [
                {
                    'axis': k,
                    'value': (g[k]-val_range[k][1])/(val_range[k][0]-val_range[k][1])
                }
                for k in keys
            ]
            for g in groups.values()
        ]
    },
    open('coffee.json', 'w')
)
