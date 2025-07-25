Indian Population Visualization Project 🇮🇳📊
===================================================

This project focuses on visualizing key trends in India's population statistics using Python libraries such as Pandas, Matplotlib, and NumPy.

📁 Project Structure
-------------------

indian-population-visualization/
│
├── data/
│   └── indian_population.csv       
│
├── images/
│   ├── population_density.jpg
│   ├── population_life_stats.jpg
│   ├── population_raw.jpg
│   └── population_urban_vs_rural.jpg
│
├── notebooks/
│   ├── population_1.py             # Plotting total population over time
│   ├── population_2.py             # % increase in population density (bar chart)
│   ├── population_3.py             # Urban vs Rural population percentages
│   └── population_4.py             # Life, Birth, Death & Infant Mortality rates
│
├── README.md
└── .gitignore

📊 Visualizations Included
--------------------------

1. 📈 Population Growth — in crores, visualized by year.
2. 📉 % Increase in Population Density — formatted as percentage bars.
3. 🏙️ vs 🌾 Urban vs Rural Distribution — population split percentages.
4. 📊 Life Expectancy, Birth & Death Rates — dual subplot for comparison.

🧪 Requirements
---------------

Make sure you have the following libraries:

pip install pandas matplotlib numpy

▶️ How to Run
-------------

Each script inside the notebooks/ folder can be run independently after adjusting the dataset path. 

Fill the path of the downloaded dataset
    data= pd.read_csv(" The CSV file path ")

Then run the script using:
    python notebooks/population_1.py

💡 Purpose
----------

This is a self-driven exploratory data analysis and visualization project aimed at understanding population trends in India over time. It also serves as a portfolio project to demonstrate Python data skills.

🙋‍♂️ Author
-----------

Made by Pratyush Pangotra — feel free to use, fork, or contribute!
