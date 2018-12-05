#모두의 데이터과학 unit35
import pandas as pd
import numpy as np

alco2009 = pd.read_csv("niaaa-report2009.csv", index_col = "State")
population = pd.read_csv("population.csv", index_col = "State")
df=pd.merge(alco2009, population, left_index=True, right_index=True)
print(population.join(alco2009).tail(10))
print(pd.concat([alco2009, population], axis=1).tail())

dna="AGTCCGCGAATACAGGCTCGGT"
dna_as_series=pd.Series(list(dna), name = "genes")
print(dna_as_series)
print(dna_as_series.unique())
print(dna_as_series.value_counts().sort_index())
valid_nucs = list("ACGT")
print(dna_as_series.isin(valid_nucs).all())