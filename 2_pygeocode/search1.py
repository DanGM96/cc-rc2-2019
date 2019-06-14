from geopy.geocoders import Nominatim

if __name__ == '__main__':
    address = 'Ceará, Ituiutaba, MG'
    user_agent = 'Search1'
    location = Nominatim(user_agent=user_agent).geocode(address, exactly_one=False) # addressLine, locality (city), adminDistrict (state), countryRegion, or postalcode

    print('Endereço buscado: ', address)
    i = 0
    for l in location:
        aux = l[0].split(',') # lista
        print('\tResultado ', i + 1, ': ')
        print('\t\tCEP: ', aux[len(aux) - 2]) # pega a penúltima posição da lista
        print(f'\t\t(Latitude, Longitude): ({l.latitude}, {l.longitude})')
        i = i + 1
