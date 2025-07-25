import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

data= pd.read_csv(" The CSV file path ")
# Remove the '%' sign and convert to float
data['% Increase in Population Density'] = data['% Increase in Population Density'].str.rstrip('%').astype(float)
plt.figure(figsize=(12, 6))
plt.bar(data['Year'], data['% Increase in Population Density'])

# Define custom y-axis ticks (in decimal form)
custom_yticks = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 2, 2.75]
plt.yticks(custom_yticks)

# Set x-axis ticks with a 5-year gap
plt.xticks(range(data['Year'].min(), data['Year'].max() + 1, 5))

# Format y-axis ticks as percentages
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:.2f}%'))

plt.show()
