#시리즈
import pandas as pd
import numpy
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

#재인덱싱
s_states = [state for state in alco2009.index if state[0] == 'S'] + ["Samoa"]

#결측치 삭제
nan_alco.dropna(how="all")

#결측치 보정
nan_alco.isnull()

sp = nan_alco["Spirits"]
clean = sp.notnull()
sp[-clean] = sp[clean].mean()
nan_alco