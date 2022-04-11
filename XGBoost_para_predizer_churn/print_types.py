def p():
colunas = []
Type = []
unique_valor = []

for column in df.columns:
    colunas += [column]
    Type += [df[column].dtype]
    unique_valor += [df[column].unique()]
dict_info.update({"Coluna": colunas, "Type": Type, "unique_valor": unique_valor})
df_info = pd.DataFrame(dict_info)

# Default value of display.max_rows is 10 so at max
# 10 rows will be printed. Set it None to display
# all rows in the dataframe
pd.set_option('display.max_rows', None)
df_info