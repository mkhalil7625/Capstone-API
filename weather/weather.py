import requests
import os
import datetime
from dateutil import parser
from pytz import timezone
def main():
    key = os.environ.get('WEATHER_KEY')
    city = input("Enter City Name: ").capitalize()
    country = input("Enter Country Code").capitalize()
    query = {'q':(city,country), 'units':'imperial', 'appid':key}
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    res= requests.get(url, params=query).json()
    print(res)
    if res.get('cod')=='200':
        res_list=res['list']
        print(f'                     ***Weather Forecast Report*** \n'
              f'                        ***of {city}***')

        print('             ***Three hour intervals over the next 5 days***')
        print('')
        for data in res_list:
            time=parser.parse(data['dt_txt'])#utc time
            time_utc=time.replace(tzinfo=timezone('UCT'))
            # convert to central
            time_central=time_utc.astimezone(tz=timezone('EST'))
            temp = data['main']['temp']
            weather_description=data['weather'][0]['description']
            wind_speed=data['wind']['speed']
            wind_degree=data['wind']['deg']

            print(f'* At {time_central}:\n the weather will be {weather_description}, \n'
                  f'  the temperature will be {temp:.2f}F,\n'
                  f'  and the expected wind speed is {wind_speed} mph, at {wind_degree} degrees')
    elif res.get('cod')=='404':
        print(f"Error: {res['message']}")

    # weather_description = data['weather'][0]['description']
    #
    # temp_f = data['main']['temp']
    # print(f'The weather is {weather_description}, the temperature is {temp_f:.2f}F.')
    #

if __name__ == '__main__':
    main()
