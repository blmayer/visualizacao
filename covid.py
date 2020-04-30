import csv
import json

covid_data = []
with open("arquivo_geral.csv") as covid_file:
    reader = csv.DictReader(covid_file, delimiter=';')
    for line in reader:
        covid_data.append(line)

covid_infec = {}
covid_death = {}
for dat in covid_data:
    covid_infec[dat['estado']] = covid_infec.get(
        dat['estado'], 0) + int(dat['casosNovos'])
    covid_death[dat['estado']] = covid_death.get(
        dat['estado'], 0) + int(dat['obitosNovos'])

topo = json.load(open('covid.json'))
for state in topo['objects']['estados']['geometries']:
    state['properties']['cases'] = covid_infec[state['id']]
    state['properties']['deaths'] = covid_death[state['id']]

json.dump(topo, open('covid_brasil.json', 'w'), ensure_ascii=False)
