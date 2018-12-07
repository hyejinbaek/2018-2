import numpy.random as rnd 

rnd.seed(0)
print(rnd.uniform(low=0.0, high=1.0, size=None))

print(rnd.rand(2,3))


import pandas as pd
import numpy as np

alco=pd.read_csv("niaaa-report.csv", index_col=["State", "Year"])
beer_seriesNY = alco.ix["New York"]['Beer']
beer_seriesCA = alco.ix['California']['Beer']
print(beer_seriesNY.corr(beer_seriesCA))
print(beer_seriesCA.cov(beer_seriesNY))
print([x.skew() for x in (beer_seriesCA, beer_seriesNY)])