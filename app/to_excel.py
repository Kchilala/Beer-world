
path = '/Users/MB/PycharmProjects/h11-assignment-2-template/assets/beer_db_v4.csv'
from app.data_loader import read_dataset, path

import pandas as pd
df = pd.DataFrame(read_dataset(path))
df.to_excel("beer_data.xlsx", index=False)