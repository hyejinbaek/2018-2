#모두의 데이터과학 225쪽 해보자 1번째

import pandas as pd
from scipy.stats import pearsonr

snp=pd.read_csv("^GSPC.csv", index_col=["Date"])
type(snp)
type(snp["Close"])
type(snp.ix["2001-01-02"])
snp.ix["2001-01-02"]
print(snp["Close"].mean())
print(snp["Close"].std())

print(pearsonr(snp["Close"], snp["Volume"]))


