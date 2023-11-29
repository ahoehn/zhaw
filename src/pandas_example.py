import matplotlib.pyplot as plt
import pandas as pd
data_frame = pd.read_excel("hydrocarbons.xlsx")
plt.scatter(data_frame['nr_molecules'],
            data_frame['heat_release'])
plt.title("Scatter Plot X vs. Y")
plt.xlabel(data_frame.columns[1])
plt.ylabel(data_frame.columns[2])
plt.show()
