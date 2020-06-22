import pandas as pd
import matplotlib.pyplot as plt


def clean_up():
    df = pd.read_csv("planes.csv")
    df.plot(kind="scatter", x="wind_degree", y="planes")
    print("data points:", len(df))
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    clean_up()
