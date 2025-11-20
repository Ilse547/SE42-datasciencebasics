# %% [markdown]
# # Q1. Which bird species are the most commonly observed overall?

# %%
import pandas as pd
import matplotlib.pyplot as mpl
import numpy as np

# %%
df = pd.read_csv("<PATH>/0035785-251025141854904.csv",
sep="\t",
skiprows=1,
names=[
    "species","specieskey","year","month","countrycode","occurences"
])

# %%
df.isna().sum()

# %%
df.shape

# %%
df.head()

# %%
df.info()

# %%
species_cnt = (df.groupby('species',as_index=False)['occurences'].sum().sort_values('occurences', ascending=False))

# %%
n=10
species_cnt.head(n)

# %%
mpl.figure(figsize=(10,6))
top=species_cnt.head(n)
mpl.barh(top['species'][::-1],top['occurences'][::-1])
mpl.xlabel('occurences')
mpl.title('10 most observed bird species in fr and de')
mpl.tight_layout()

# %%



