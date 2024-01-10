import pandas as pd
import matplotlib.pyplot as plt


def plot_data_from_csv():
    x = 6
    y = 6

    csv_data = pd.read_csv('data.csv')
    plot_all_values(csv_data)

    plot_first_x_values(csv_data, x)

    plot_last_y_values(csv_data, y)


def plot_all_values(csv_data):
    csv_data.plot()
    plt.title('Grafic cu toate valorile')
    plt.show()


def plot_first_x_values(csv_data, x):
    csv_data.head(x).plot()
    plt.title(f'Grafic cu primele {x} valori')
    plt.show()


def plot_last_y_values(csv_data, y):
    csv_data[['Durata', 'Puls']].tail(y).plot()
    plt.title(f'Grafic cu ultimele {y} valori pentru Durata si Puls')
    plt.show()
