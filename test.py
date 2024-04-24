from pandas import *
import matplotlib.pyplot as plt
data = read_csv("rym_top_5000_all_time.csv")['Average Rating'].tolist()
plt.hist(data,density=True, bins=80)
plt.show()