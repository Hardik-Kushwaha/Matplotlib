import matplotlib.pyplot as plt
import pandas as pd
file = pd.read_excel('data.xlsx')
plt.pie(file['Value'],labels=file['Label'])
plt.show()
