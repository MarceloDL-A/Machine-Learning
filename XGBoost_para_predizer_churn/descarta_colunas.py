def descarta_colunas_com_um_unico_valor(df):
    for i, feature in enumerate(df.columns):
        print(str(i) + ": ", feature, "\nValores únicos: " + str(len(df[feature].unique())))
        if len(df[feature].unique()) == 1:
            print(f"A coluna {feature} possui um único valor e não contribui para o modelo. Por isso essa coluna será excluída.")

            df.drop([feature],
                    axis=1, # escolha axis = 0 para remover linhas, axis = 1 para remover colunas (features)
                    inplace=True # para substituir o resultado do drop no próprio dataframe df
            )
        print("_"*150)
    return df