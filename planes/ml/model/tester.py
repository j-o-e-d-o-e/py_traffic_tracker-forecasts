import joblib
import matplotlib.pyplot as plt


def check(info=True):
    clf = joblib.load("decision_tree_proba.pkl")
    res = []
    for i in range(360):
        proba = clf.predict_proba([[i]])[0][1]
        res.append(proba)
    if info:
        plt.scatter(range(360), res)
        plt.xlabel("wind_degree")
        plt.ylabel("planes")
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    check()
