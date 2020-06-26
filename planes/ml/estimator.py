import joblib


def predict(days):
    clf = joblib.load("planes/ml/model/random_forest_classifier.pkl")
    for day in days:
        for hour in day["hours"]:
            hour["probability"] = round(clf.predict_proba([[hour["wind_degree"]]])[0][1] * 100, 2)
        day["probability"] = round(sum(hour["probability"] for hour in day["hours"]) / len(day["hours"]), 2)
    return days

