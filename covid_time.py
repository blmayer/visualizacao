import csv
import json

covid_time = {}
with open('arquivo_geral.csv') as covid_file:
    reader = csv.DictReader(covid_file, delimiter=';')
    for line in reader:
        if line['estado'] in covid_time:
            continue
        else:
            if int(line['casosNovos']) > 0:
                covid_time[line['estado']] = line['data']

topo = json.load(open('covid_brasil.json'))
for state in topo['objects']['estados']['geometries']:
    state['properties']['start'] = covid_time[state['id']]

json.dump(topo, open('covid_brasil.json', 'w'), ensure_ascii=False)
