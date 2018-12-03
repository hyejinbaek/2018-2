#unit 31
import pandas as pd
import numpy

alco2009 = pd.read_csv("niaaa-report2009.csv", index_col="State")
print(alco2009)

print(alco2009["Wine"].head())
print(alco2009.Beer.tail())
alco2009["Total"]=0
print(alco2009.head())

#unit 32












inflation = pd.Series((2.2, 3.4, 2.8, 1.6, 2.3, 2.7, 3.4, 3.2, 2.8, 3.8, -0.4, 1.6, 3.2, 2.1, 1.5, 1.5))

print(inflation)
print(inflation.values)
print(inflation.index)

inflation.values[-1] = 1.6

inflation.index = pd.Index(range(1999, 2015))
inflation[2015] = numpy.nan

#프레임
import pandas as pd
alco2009 = pd.read_csv("niaaa-report2009.csv", index_col="State")
alco2009

alco2009.ix["Nebraska"]

"Samoa" in alco2009.index

alco2009.columns.values
alco2009.index.values

# unit 32 인덱싱
s_states = [state for state in alco2009.index if state[0] == 'S'] + ["Samoa"]

#unit 33 
alco2009 = pd.read_csv("niaaa-report2009.csv", index_col="State")
s_states = [state for state in alco2009.index if state[0] == 'S'] + ["Samoa"]
drinks = list(alco2009.columns) + ["Water"]
nan_alco = alco2009.reindex(s_state, columns=drinks)
nan_alco

nan_alco.dropna(how="all")

nan_alco.dropna(how="all", axis=1)

nan_alco.dropna()