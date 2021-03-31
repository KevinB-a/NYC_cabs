import pandas as pd
import numpy as np

desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 10)

df = pd.read_csv("/home/apprenant/PycharmProjects/NYC_cabs/data/train.csv")

print(df.head(10))

print(round(df.describe()))

print(df.shape)

print("Nombre de lignes dupliquées")
print(df.duplicated().value_counts())

print("\n" + "Nombre de valeurs manquantes")
print(df.isnull().sum())

print(df.columns)

df_clean = df[['id', 'vendor_id', 'pickup_datetime', 'dropoff_datetime', 'pickup_longitude', 'pickup_latitude',
               'dropoff_longitude', 'dropoff_latitude', 'trip_duration']]

df_clean.to_csv("/home/apprenant/PycharmProjects/NYC_cabs/data/clean.csv", index = False)
