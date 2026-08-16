import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
veriler= np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(veriler.std())

data = {
    "isim": ["Ali", "Ayşe", "Mehmet"],
    "yas": [20, 22, 21],
    "puan": [80, 95, 75]
}
df = pd.DataFrame(data)
print(df.describe())
print(df["puan"]>94)
plt.plot(df["yas"], df["puan"])
plt.show()
sns.histplot(df["puan"], bins=5, kde=True)