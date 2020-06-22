import requests
import pandas as pd
from datetime import datetime

URL = 'http://traffic-tracker.herokuapp.com/planes/day/all'
end_date = datetime(2020, 3, 4)
json_dict = []


def fetch(info=False):
    for day in requests.get(URL).json():
        if day["wind_speed"] > 50:
            continue
        date = datetime.strptime(day["date"], '%Y-%m-%d')
        if date.date() == end_date.date():
            continue
        planes = day["hours_plane"][6:-1]
        winds = day["hours_wind"][6:-1]
        for i in range(len(planes)):
            json_dict.append({"planes": planes[i], "wind_degree": winds[i]})
    df = pd.DataFrame(json_dict)
    df.to_csv("planes.csv", index=False)
    if info:
        print(df.info())
        print(df.head())
    return df


if __name__ == "__main__":
    fetch(True)
