import requests
from datetime import datetime

from planes.models import Day, Hour

URL = 'WEATHER_API_URL'


def fetch():
    for data in requests.get(URL).json()['list']:
        date = datetime.strptime(data['dt_txt'], '%Y-%m-%d %H:%M:%S')
        if date.hour < 6:  # only hours: 6, 9, 12, 15, 18, 21
            continue
        if not Day.objects.first() or date.date() != Day.objects.last().date:
            new_day = Day(date=date.date())
            new_day.save()
        hour = Hour(time=date.time(), wind_degree=data['wind']['deg'])
        Day.objects.last().hours.add(hour, bulk=False)
