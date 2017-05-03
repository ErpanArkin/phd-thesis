import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from io import StringIO



df = pd.read_table('graphene_publications.txt',index_col=0)

fig = plt.figure() # Create matplotlib figure

ax = fig.add_subplot(111) # Create matplotlib axes
ax2 = ax.twinx() # Create another axes that shares the same x-axis as ax.

width = 0.4

df.publications.plot(kind='bar', color='red', ax=ax, width=width, position=1)
df.patents.plot(kind='bar', color='blue', ax=ax2, width=width, position=0)

ax.set_ylabel('publications')
ax2.set_ylabel('patents')
plt.xlabel('Year')
fig.autofmt_xdate()
lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc=0)

plt.savefig('graphene_papers.eps',bbox_inches='tight')

plt.show()