#!/usr/bin/env python3
import requests


def geocode(address):
    base = 'https://nominatim.openstreetmap.org/search'
    parameters = {'q': address, 'format': 'json'}
    user_agent = 'Search2.py'
    headers = {'User-Agent': user_agent}
    response = requests.get(base, params=parameters, headers=headers)
    reply = response.json()

    print('Endereço buscado: ', address)
    i = 0
    for r in reply:
        aux = r['display_name'].split(',')  # lista
        lat = r['lat']
        lon = r['lon']
        print('\tResultado ', i + 1, ': ')
        print('\t\tCEP: ', aux[len(aux) - 2])
        print(f'\t\t(Latitude, Longitude): ({lat}, {lon})')
        i = i + 1


if __name__ == '__main__':
    geocode('Belarmino Vilela Junqueira, Ituiutaba, MG')
