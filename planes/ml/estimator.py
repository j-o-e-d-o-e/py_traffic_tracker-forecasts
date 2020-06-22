import joblib
from planes.models import Day


def predict():
    clf = joblib.load("planes/ml/model/random_forest_classifier.pkl")
    for day in Day.objects.all():
        for hour in day.hours.all():
            hour.probability = round(clf.predict_proba([[hour.wind_degree]])[0][1] * 100, 2)
            hour.save()
        day.probability = round(sum(hour.probability for hour in day.hours.all()) / len(day.hours.all()), 2)
        day.save()
        print(day)
    return Day.objects.all()
