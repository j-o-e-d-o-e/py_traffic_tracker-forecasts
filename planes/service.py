from planes.ml import estimator, client_weather
from planes.models import Day


def predict_and_get_forecasts():
    Day.objects.all().delete()
    client_weather.fetch()
    estimator.predict()
    return Day.objects.all()


def get_forecasts():
    return Day.objects.all()
