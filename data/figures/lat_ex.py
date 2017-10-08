import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from io import StringIO



df0 = pd.read_csv('lat_ex.dat',delim_whitespace=True,index_col=0)
df= df0.transpose()
print(df)
fig = plt.figure() # Create matplotlib figure

ax = fig.add_subplot(111) # Create matplotlib axes
ax2 = ax.twinx() # Create another axes that shares the same x-axis as ax.

width = 0.4

df[['lattice constant']].plot(kind='bar', color='red', ax=ax, width=width, position=1)
df[['band gap']].plot(kind='bar', color='blue', ax=ax2, width=width, position=0)

ax.set_ylabel('MAE of lattice constants (pm)', color="red")
ax2.set_ylabel('MAE of band gaps (eV)', color="blue")
ax.tick_params(axis='y', colors='red')
ax2.tick_params(axis='y', colors='blue')
ax2.spines['left'].set_color('red')
ax2.spines['right'].set_color('blue')
plt.xlabel('Functionals')
fig.autofmt_xdate(rotation=0, ha='center')
lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc=0)

plt.savefig('lat_ex.eps',bbox_inches='tight')

plt.show()