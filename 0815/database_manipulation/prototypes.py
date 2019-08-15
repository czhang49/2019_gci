import pandas as pd

df = pd.read_csv("./world_development_indicator.csv")

print(df.sample(2))
print(df[df["Latest trade data"]>2016].sample(10))
new_df = df.groupby("Short Name")
