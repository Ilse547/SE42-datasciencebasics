# %% [markdown]
# # Q2. How do bird sightings vary over the year?
# 

# %%
import pandas as pd
import matplotlib.pyplot as mpl
import numpy as np

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
month_cnt=(df.groupby('month',as_index=False)['occurences'].sum().sort_values('month'))

# %%
mpl.figure(figsize=(12,5))
mpl.plot(month_cnt['month'],month_cnt['occurences'],marker="x")
mpl.xlabel('months')
mpl.ylabel('sightings')
mpl.xticks(range(1,13))
mpl.grid(True,alpha=0.3)
mpl.tight_layout()
mpl.show()


