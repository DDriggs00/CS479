import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Create your connection.
dbpath = "C:\\Users\\Jolteon\\Documents\\Homework\\CS-479 Data Science\\CS379\\db\\2019-04-27_162536"
cnx = sqlite3.connect(dbpath)

df = pd.read_sql_query("SELECT date, close FROM BTC", cnx)

df.plot()
plt.show()