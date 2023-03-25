with open("c:/Git/financial_sector_integrity/Data/FRB_H8.csv") as fp:

    df = pd.read_csv(fp)
    print(df.head())
    df_transposed = df.transpose()
    print(df_transposed.head())

    print(df_transposed.head(40))
    
with open ("c:/Git/financial_sector_integrity/Data/FRB_H8_2.csv") as fp2:
    df2 = pd.read_csv(fp2)
    print(df2.head())
    df2_transposed = df2.transpose()
    print(df2_transposed.head())
