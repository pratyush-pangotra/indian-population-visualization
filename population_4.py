import pandas as pd
import matplotlib.pyplot as plt
data= pd.read_csv(" The CSV file path ")

# Create figure with 2 subplots side-by-side
fig, axs = plt.subplots(1, 2, figsize=(16, 6), sharex=True)

# Subplot 1: Life Expectancy and Death Rate
axs[0].plot(data['Year'], data['Life Expectancy'], color='green', label='Life Expectancy', linewidth=3)
axs[0].plot(data['Year'], data['Death Rate'], color='blue', label='Death Rate', linewidth=3)
axs[0].set_title('Life Expectancy & Death Rate')
axs[0].set_xlabel('Year')
axs[0].set_ylabel('Value')
axs[0].legend()
axs[0].grid(True)

# Subplot 2: Birth Rate and Infant Mortality Rate
axs[1].plot(data['Year'], data['Birth Rate'], color='orange', label='Birth Rate', linewidth=3)
axs[1].plot(data['Year'], data['Infant Mortality Rate'], color='red', label='Infant Mortality Rate', linewidth=3)
axs[1].set_title('Birth Rate & Infant Mortality Rate')
axs[1].set_xlabel('Year')
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()
