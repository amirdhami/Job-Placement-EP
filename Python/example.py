import causaldata

data_class = causaldata.nsw_mixtape

df = data_class.load_pandas().data

print(df.head(5))

print(data_class.NOTE)
print(data_class.DESCRLONG)
