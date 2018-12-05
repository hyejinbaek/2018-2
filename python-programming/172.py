#모두의 데이터과학 172쪽 문제 1번 스라소니 밀렵
import pandas as pd

lynx=pd.read_csv("lynx.csv")
lynx["time"] = round(lynx.time / 10) * 10
sum_lynx = lynx.groupby("time").sum()
sort_lynx = sum_lynx.sort_values("value", ascending = False).head(10)
print(sort_lynx)



