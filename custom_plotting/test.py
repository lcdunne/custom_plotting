import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# Customisation:
from plot_settings import sci_rc, bar_kw, palettes

# sns.set_style("darkgrid")
sns.set_palette(palettes['bluegrey'])
# sns.set_palette("Set1")
plt.rcParams.update(sci_rc)

df = sns.load_dataset("fmri")
print(df.head())

fig, ax = plt.subplots()
sns.lineplot(data=df,
             x='timepoint',
             y='signal',
             hue='region',
             style='region')
plt.show()


fig, ax = plt.subplots()
sns.barplot(data=df,
            x="region",
            y="signal",
            hue="event",
            **bar_kw,
            ax=ax)
plt.show()
