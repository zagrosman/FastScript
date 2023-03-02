import proplot as plot
import pandas as pd

# Load the CSV data into a pandas dataframe
df = pd.read_csv('data.csv')

# Create a figure and set the axis labels
fig, ax = plot.subplots()
ax.format(xlabel='Strains', ylabel='Halo diameter')

# Create the stacked plot using the dataframe
ax.stackplot(df['x'], df.drop('x', axis=1).T, labels=df.drop('x', axis=1).columns)

# Add a legend and show the plot
ax.legend(loc='best')
plot.show()

