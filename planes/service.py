from planes.ml import estimator, client_weather
from planes.models import Day, Hour
from django.utils import timezone
from datetime import timedelta


def predict_and_get_forecasts():
    Day.objects.filter(date__lt=timezone.now().date() - timedelta(days=30)).all().delete()
    weather_data = client_weather.fetch()
    for prediction in estimator.predict(weather_data):
        day = Day.objects.filter(date=prediction["date"]).first()
        if not day:
            day = Day.objects.create(date=prediction["date"], probability=prediction["probability"])
        else:
            day.probability = prediction["probability"]
            day.hours.all().delete()
        for prediction_hour in prediction["hours"]:
            hour = Hour(time=prediction_hour["time"], wind_degree=prediction_hour["wind_degree"],
                        probability=prediction_hour["probability"])
            day.hours.add(hour, bulk=False)
        day.save()
    return Day.objects.filter(date__gte=timezone.now().date()).all()


def get_forecasts():
    return Day.objects.all()

