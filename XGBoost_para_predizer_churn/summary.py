def categorias_unicas(coluna_analisada):
    return len(coluna_analisada.unique())

def summary(df):
    metric_dict = {feature: ["max", "min", categorias_unicas] for feature in df.columns}
    return df.agg(metric_dict)
