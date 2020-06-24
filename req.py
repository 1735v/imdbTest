import requests

#API_KEY = &apikey=d1149b8f


def search_movie(name):
    url = 'http://www.omdbapi.com/'
    para ={'apikey': 'd1149b8f' ,'t': name}
    respons = requests.get(url, params=para)

    return (respons.json())


def search_movie_list(name):
    url = 'http://www.omdbapi.com/'
    para = {'apikey': 'd1149b8f', 's': name}
    respons = requests.get(url, params=para)

    return (respons.json())


#print(search_movie_list('Knives'))

def search_movie_pages(name,page=1):
    url = 'http://www.omdbapi.com/'
    para ={'apikey': 'd1149b8f' ,'s': name,'page':page}
    respons = requests.get(url, params=para)

    return (respons.json())


def search_movie_ratings(name):
    url = 'http://www.omdbapi.com/'
    para = {'apikey': 'd1149b8f' ,'t': name}
    respons = requests.get(url, params=para)
    ratings_amdb = float(respons.json()['Ratings'][0]['Value'].split('/')[0])
    return (ratings_amdb)




print(search_movie_ratings('Knives Out'))
