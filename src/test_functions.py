import pandas as pd
from feature_engineering import feature_engineer
from pre_processing import process

df = pd.read_csv("data/raw/onlinefraud.csv/onlinefraud.csv")

sample = df.sample(n=10)

engineered = feature_engineer(sample)

print(engineered.columns)
print(engineered.head())

print("\nNaN Count Before Processing:\n")
print(engineered.isna().sum())

processed = process(engineered)

print(processed.head())

print("\nColumns:\n")
print(processed.columns)

print("\nNaN Count After Processing:\n")
print(processed.isna().sum())