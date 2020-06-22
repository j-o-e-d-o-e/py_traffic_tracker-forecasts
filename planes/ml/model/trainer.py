import joblib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def create_model(info=True):
    df = pd.read_csv("../csv/planes.csv")
    if info:
        df.plot(kind="scatter", x="wind_degree", y="planes")
        plt.grid(True)
        plt.show()
    y = (df.pop('planes') > 0) * 1
    x_train, x_test, y_train, y_test = train_test_split(df, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(random_state=0)
    clf.fit(x_train, y_train)
    joblib.dump(clf, "random_forest_classifier.pkl", compress=0)


if __name__ == "__main__":
    create_model(info=False)
