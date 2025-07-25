import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data= pd.read_csv(" The CSV file path ")

data['Urban Population % of Total Population'] = data['Urban Population % of Total Population'].replace('Null', np.nan)
data['Rural Population % of Total Population'] = data['Rural Population % of Total Population'].replace('Null', np.nan)
data['Urban Population % of Total Population'] = data['Urban Population % of Total Population'].str.rstrip('%').astype(float)
data['Rural Population % of Total Population'] = data['Rural Population % of Total Population'].str.rstrip('%').astype(float)

data.dropna(subset=['Urban Population % of Total Population', 'Rural Population % of Total Population'], inplace=True)

x = np.arange(len(data['Year']))
width = 0.4

plt.figure(figsize=(12, 6))
plt.bar(x - width/2, data['Rural Population % of Total Population'], width=width, color='orange', label='Rural')
plt.bar(x + width/2, data['Urban Population % of Total Population'], width=width, color='green', label='Urban')
plt.title('Urban vs Rural Population Percentage Over Years')
plt.xlabel('Year')
plt.ylabel('Population %')

# Custom Ticks
tick_locations = list(range(0, len(data['Year']), 5))
tick_labels = [data['Year'].iloc[i] for i in tick_locations]
plt.xticks(tick_locations, tick_labels, rotation=45)
plt.yticks(np.arange(0, 101, 5))

plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

