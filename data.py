import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

baglanti = sqlite3.connect("okul.db")

cursor = baglanti.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS ogrenciler (
    id INTEGER PRIMARY KEY,
    ad TEXT,
    yas INTEGER,
    bolum TEXT
)
""")

ogrenciler = [
    ("Ayşe", 21, "Elektronik"),
    ("Mehmet", 19, "Bilgisayar"),
    ("Zeynep", 22, "Yazılım")
]
cursor.executemany("""
INSERT INTO ogrenciler (ad, yas, bolum)
VALUES (?, ?, ?)
""", ogrenciler)
baglanti.commit()
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