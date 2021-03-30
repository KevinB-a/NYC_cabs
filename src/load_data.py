import pandas as pd
import numpy as np

df = pd.read_csv("/home/apprenant/PycharmProjects/NYC_cabs/data/train.csv")
#print(df)
#print(df.columns.values)

################################################################
"""Selection des colonnes """

#print(df.head())
#print(df.columns)

df = df[['id','vendor_id', 'pickup_datetime', 'dropoff_datetime', 'pickup_longitude', 'pickup_latitude','dropoff_longitude', 'dropoff_latitude','trip_duration']]

# deux colonnes ne serviront pas dans notre etude  : passenger_count et store_and_fwd_flag

################################################################
"""Valeurs manquantes """

print(df.isnull().sum()) 
print(df.shape)

# pas de valeurs manquantes sur le dataframe 
################################################################
"""Traitement des dates """

################################################################
"""sauvegarde du dataframe nettoyé """

df.to_csv("/home/apprenant/PycharmProjects/NYC_cabs/data/clean.csv", index = False , sep = ',' , encoding = 'utf-8', line_terminator = '\n' )

################################################################