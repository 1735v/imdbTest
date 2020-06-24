import requests
import datetime

#print(datetime.datetime.today().strftime("%Y-%m-%d"))
#print(type(datetime.datetime.today().strftime("%Y-%m-%d")))

#url = 'http://api.weatherbit.io/v2.0/history/daily'
#api_key = '41ecbf8db5264877be8ed6b1f8995135'

def check_weather(city,start_date='2020-06-24',
                  end_date='2020-06-25'):
    url = 'http://api.weatherbit.io/v2.0/history/daily'
    api_key = '41ecbf8db5264877be8ed6b1f8995135'
    para = {'key':api_key,'city':city,'start_date':start_date, 'end_date': end_date}
    respons = requests.get(url,para)
    if respons.status_code==200:
        return respons.json()
    else:
        return 'Incorect city name'
print(check_weather('Lviasdadsv'))