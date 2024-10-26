from pandas import read_excel
df = read_excel('tests.xlsx', index_col=0)
print(df.head()) # shows headers with top 5 rows

print("\n\n\n")
print(df)
