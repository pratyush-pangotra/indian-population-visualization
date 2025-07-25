import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
data= pd.read_csv(" The CSV file path ")

#Removing "," from the values
data['Population'] = pd.to_numeric(data['Population'].astype(str).str.replace(',',''),errors='coerce')

#changing population to X crores
data['Population_Crore']=data['Population']/1e7

#plotting the population
plt.plot(data['Year'], data['Population_Crore'], color= 'red', )
plt.yticks(ticks=range(0, int(data['Population_Crore'].max()) + 5, 5))
plt.xlabel('Years')
plt.ylabel('Population in Crores')
plt.tight_layout()
plt.show()