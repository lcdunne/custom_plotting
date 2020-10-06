import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# Customisation:
from plot_settings import sci_rc, bar_kw, scatter_kw, palettes

sns.set_style("darkgrid")
sns.set_palette(palettes['bluegrey'])
# sns.set_palette("Set1")
plt.rcParams.update(sci_rc)

df = sns.load_dataset("fmri")


fig, ax = plt.subplots()
sns.lineplot(data=df,
             x='timepoint',
             y='signal',
             hue='region',
             style='region')
plt.show()

bar_kw['facecolor'] = (1, 1, 1, 0)

fig, ax = plt.subplots()
sns.barplot(data=df,
            x="region",
            y="signal",
            hue="event",
            **bar_kw,
            ax=ax)
plt.show()


ROC = pd.read_csv('roc.csv')#, sep='\t')


fig, ax = plt.subplots()
ax.plot([0,1], [0,1], linestyle='dashed', c='k')
ax.scatter(data=ROC,x='FPR', y='TPR', **scatter_kw)
ax.set(xlim=(0,1), ylim=(0,1))
plt.show()