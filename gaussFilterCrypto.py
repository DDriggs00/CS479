import numpy
from os.path import abspath, join
from matplotlib import pyplot

from scipy.ndimage.filters import gaussian_filter1d

import sqlite3

DB_DIR = 'db'
db_name = '2019-04-27_162536'

crypto = 'BTC'

conn = sqlite3.connect( abspath( join( DB_DIR, db_name) ) )
c = conn.cursor()

prices = c.execute('SELECT high FROM '+ crypto).fetchall()
dates = c.execute('SELECT date FROM '+ crypto ).fetchall()

y = []
x = []

for price in prices:
   y.append(price[0])

for date in dates:
   x.append(date[0])

ysmoothed = gaussian_filter1d(y, sigma=2)

pyplot.plot(x, ysmoothed)
pyplot.show()