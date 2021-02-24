import pandas as pd

def prep_iris(raw_iris_df):
    iris_df = raw_iris_df.copy()
    
    iris_df.drop(columns=['species_id', 'measurement_id'], inplace=True)
    iris_df.rename(columns={'species_name' : 'species'}, inplace=True)
    
    species_dummies_df = pd.get_dummies(iris_df[['species']], dummy_na=False, drop_first=True)
    
    return pd.concat([iris_df, species_dummies_df], axis=1)