import proplot as plot
import pandas as pd

# read data from CSV file
df = pd.read_csv('data.csv')

# create a colorful line graph
fig, ax = plot.subplots()
ax.plot(df['x'], df['D1'], label='Line 1', color='blue')
ax.plot(df['x'], df['D2'], label='Line 2', color='green')
ax.plot(df['x'], df['D3'], label='Line 3', color='red')
ax.legend()
ax.format(xlabel='Strains', ylabel='Halo diameter', title='PGPRs assay')
plot.show()

