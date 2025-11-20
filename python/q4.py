# %% [markdown]
# # how does the number of sightings of Phylloscopus collybita vary per month and country?

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
spe_name='Phylloscopus collybita'
df_spe=df[df['species']==spe_name]

# %%
piv=df_spe.pivot_table(
    index='month',
    columns='countrycode',
    values='occurences',
    aggfunc='sum',
    fill_value=0
)

# %%
print(piv)

# %%
pivot_reset=piv.reset_index().melt(id_vars='month',var_name='country',value_name='occurences')
mpl.figure(figsize=(12,5))
for country in piv.columns:
    mpl.bar(piv.index+(0.2 if country==piv.columns[0] else -0.2),
            piv[country],width=0.4,label=country)
mpl.xlabel('month')
mpl.ylabel('sightings')
mpl.title('sightings of bird species by month and country')
mpl.legend(title='country')
mpl.tight_layout()

# %%



