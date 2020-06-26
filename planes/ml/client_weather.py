import requests
from datetime import datetime

URL = 'WEATHER_API_URL'


def fetch():
    days = []
    for data in requests.get(URL).json()['list']:
        date = datetime.strptime(data['dt_txt'], '%Y-%m-%d %H:%M:%S')
        if date.hour < 6:  # only hours: 6, 9, 12, 15, 18, 21
            continue
        if not days or date.date() != days[-1]["date"]:
            days.append({"date": date.date(), "hours": []})
        days[-1]["hours"].append({"time": date.time(), "wind_degree": data['wind']['deg']})
    return days

