import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame):
    heavy_animals = animals[animals["weight"] > 100].sort_values(by='weight', ascending=False)
    return heavy_animals[['name']]