# %% [markdown]
# # Q5: How doe4s the diversity of different species changed over the years ?

# %%
import pandas as pd
import matplotlib.pyplot as mpl
import numpy as np
import seaborn as sb

# %%
df=pd.read_csv('<PATH>/0035785-251025141854904.csv',
               sep='\t',
               skiprows=1,
               names=['species','specieskey','year','month','countrycode','occurences'])

# %%
spe_div=df.groupby('year')['species'].nunique().reset_index()

# %%
mpl.figure(figsize=(12,5))
mpl.plot(spe_div['year'], spe_div['species'],marker='.')
mpl.xlabel("year")
mpl.ylabel('species oberserved')
mpl.title('bird species observed over the years')
mpl.grid(True)
mpl.tight_layout()


# %%


# %%



