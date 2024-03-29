import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mystat = pd.read_csv('Area & Production in Pakistan CSV.csv')
mystat
print(mystat)
mystat.duplicated()
mydataframe = pd.DataFrame(mystat)
mydataframe.loc[0]
mydataframe.head()
mydataframe.tail(5)

plt.title('Fruits Statistics')
plt.xlabel('Production Year')
plt.ylabel("Production Area (Hectres)")
plt.grid()
plt.show()