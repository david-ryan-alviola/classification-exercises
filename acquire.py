import sys
import pandas as pd
import os

from env import user, password, host, util_repo, data_path
sys.path.append(util_repo)
from utilities import generate_db_url



def get_titanic_data():
    file_name = "titanic.csv"
    query = """
    SELECT *
        FROM passengers;
    """
    
    if os.path.isfile(file_name):
        
        return pd.read_csv(file_name)
    else:
        df = pd.read_sql(query, generate_db_url(user, password, host, "titanic_db"))
        df.to_csv(file_name)
        
        return df

def get_iris_data():
    file_name = "iris.csv"
    query = """
    SELECT *
        FROM measurements
            JOIN species USING(species_id);
    """
    
    if os.path.isfile(file_name):
        
        return pd.read_csv(file_name)
    else:
        df = pd.read_sql(query, generate_db_url(user, password, host, "iris_db"))
        df.to_csv(file_name)
        
        return df
    
    