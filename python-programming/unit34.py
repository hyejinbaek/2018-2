import pandas as pd
import numpy as np

alco2009 = pd.read_csv("niaaa-report2009.csv", index_col="State")
population = pd.read_csv("population.csv", index_col="State")
df = pd.merge(alco2009.reset_index(), population.reset_index()).set_index("State")
print(df.head())
print(population.head())


