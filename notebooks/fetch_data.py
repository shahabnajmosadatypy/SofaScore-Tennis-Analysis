
import numpy as np, pandas as pd
from glob import glob



def fetch_data(first_day:int,last_day:int,table_name:str):

    day ,days_to_query , files_to_load, dataframes = first_day, [], [] ,[]

    while day <= last_day:
        
        days_to_query.append(str(day))

        if day % 100 == 31 and day != 20240331:
            day = 20240300
        day += 1



    for day in days_to_query:

        files_to_load.extend(glob(f'/home/nima/data_science/tennis_project/SofaScore-Tennis-Analysis/data/interim/{day}/{table_name}_[0-9]*.parquet'))



    for file in files_to_load:

        df = pd.read_parquet(file)
        if df.shape[0] == 1 and df.iloc[0].isna().all():
            continue
        dataframes.append(df)

    data = pd.concat(dataframes,ignore_index=True)

    return(data)
