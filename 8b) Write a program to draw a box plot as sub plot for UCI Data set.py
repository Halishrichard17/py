import matplotlib.pyplot as plt
import pandas as pd
import random
import sys
fig, axes = plt.subplots(2,2) # create figure and axes

df = pd.DataFrame(data={'A': random.sample(range(60, 100), 10),
                    'B': random.sample(range(20, 40), 10),
                    'C': random.sample(range(2000, 3010), 10),
                    'type': list(3*'K')+list(3*'L')+list(4*'M')})

for i,el in enumerate(list(df.columns.values)[:-1]):
    a = df.boxplot(el, by="type", ax=axes.flatten()[i])

fig.delaxes(axes[1,1]) # remove empty subplot
plt.tight_layout() 

plt.show()