## imports Package
import matplotlib.pyplot as plt
import pandas as pd

## read file and add in variable
data = pd.read_table("/home/nsa/Documentos/Fametro/datascience/assets/fruit_data_with_colors.txt")

data.groupby('fruit_name')['mass'].agg('max')

kind = data['fruit_name'].value_counts()

## apresenta gráfic com as frutas de maior ocorrẽncia
kind.plot(kind = 'bar')
plt.show()