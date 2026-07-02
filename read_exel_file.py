
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt
from utilities import plot_settings


data = pd.read_excel("data\\raw\\raw_data\\fsi-2020.xlsx", index_col=0)



for clm in data.columns[2:3]:
    data[clm].plot(figsize=(15, 2.5))
    plt.show()
    
path = "C:\\Users\\tanvi\\OneDrive\\Desktop\\Pathan Tahirkhan Aarifkhan\\low_level_data_visualization\\data\\raw\\raw_data"    
files = sorted(glob(path + "\\*.xlsx"))

data_combined = pd.concat(
    [pd.read_excel(f, index_col=0) for f in files]
    )

data_combined["Total"].plot()
plt.show()

data_combined.to_excel("data\\processed\\visualized_data.xlsx")
data_combined.to_csv("data\\processed\\visualized_data.csv")