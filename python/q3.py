# %% [markdown]
# # Which species show the most significant changes in observation frequency over the years?

# %%
import pandas as pd
import matplotlib.pyplot as mpl
import numpy as np
import seaborn as sb

# %%
df = pd.read_csv("<PATH>0035785-251025141854904.csv",
sep="\t",
skiprows=1,
names=[
    "species","specieskey","year","month","countrycode","occurences"
])

# %%
df.isna().sum()

# %%
df.head()

# %%
sp_year=(df.groupby(['species','year'],as_index=False)['occurences'].sum())

# %%
pivot=sp_year.pivot(index='species',columns='year',values='occurences').fillna(0)

# %%
year_change=pivot.diff(axis=1).abs().sum(axis=1)

# %%
top_spe=year_change.sort_values(ascending=False).head(10).index

# %%
hm=pivot.loc[top_spe]


# %%
mpl.figure(figsize=(12,5))
sb.heatmap(hm,annot=True,fmt='.0f',cmap="YlOrRd")
mpl.title('Changing Bird sighting(Top 10)')
mpl.xlabel('year')
mpl.ylabel('species')
mpl.tight_layout()
mpl.show()

# %%



