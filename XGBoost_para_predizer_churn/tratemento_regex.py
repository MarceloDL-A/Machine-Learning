
from pandas import DataFrame


def modifica_dados_da_coluna(df: DataFrame, feature: str, string_procurada: str, string_modificada: str):
    df[feature].replace(string_procurada, string_modificada, regex = True, inplace = True)
    return df

def adiciona_underscore_nos_espacos_dos_nomes_das_colunas(df):
    df.columns = df.columns.str.replace(" ", " ")
    return df
