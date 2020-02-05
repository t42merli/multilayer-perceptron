# import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv', index_col="id")

print (data.corr())

# gb = data.groupby('diagnosis')
# groups = [gb.get_group('M'), gb.get_group('B')]

# for column in data.columns:
# 	if((data[column].dtype == 'int' or data[column].dtype == 'float')):
# 		fig = plt.figure()
# 		fig.suptitle(column)
# 		plt.hist([groups[0][column], groups[1][column]], bins=8, color=[
#                  'red', 'blue'], label=['M', 'B'], histtype='barstacked', alpha=0.5)

# plt.legend()
# plt.show()

# "extVal fractal dimension, extval smothness, stde fratal dim, stde concativity, stdE smoothness, stde texture, mean fractal dimennsion"
