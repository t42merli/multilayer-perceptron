import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv', index_col="id")

gb = data.groupby('diagnosis')

for column in data.columns:
	fig = plt.figure()
	fig.suptitle(column)
	if(data[column].dtype == 'int' or data[column].dtype == 'float'):
		plt.hist(, bins=8, color=['red', 'blue'],label=[gb.groups], histtype='barstacked', alpha=0.5)
