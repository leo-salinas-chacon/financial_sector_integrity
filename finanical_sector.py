import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')
pd.options.display.max_rows = 200

with open ("c:/Git/financial_sector_integrity/Data/FRB_H8_2.csv") as fp3:
    df3 = pd.read_csv(fp3)
    print(df3.head())
    df3t = df3.transpose()
    print(df3t.head())
#looking at the charateristics of the data to see what i can remove
    print(df3t.shape)
    print(df3t.isnull().any()) 
    sns.heatmap(df3t.isnull(), yticklabels=False,)
    plt.show()
#lots of null values annoying
    print(df3t.columns())
    print(df3t.dtypes())
   