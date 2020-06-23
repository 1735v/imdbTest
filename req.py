import requests

#API_KEY = 'd1149b8f'
#url = 'http://www.omdbapi.com/'
#params = {
#    't' : 'Knives Out',
#    'p' : 'full'
#}

def search_movie(name):
    url = 'http://www.omdbapi.com/'
    para ={'apikey': 'd1149b8f' ,'t': name}
    respons = requests.get(url, params=para)

    return (respons.json()['Title'])

print(search_movie('Knives Out'))



#respons = requests.get(url, params=params)
#r = respons.json()
#print(r)
