import sqlite3
import os

# Dir must already be created
db_dir = 'db'
topCoinsDB = sqlite3.connect( os.path.abspath( os.path.join( db_dir, "topCoins.db") ) )

# Example of connecting to db in a subfolder
# btcDB = sqlite3.connect( os.path.abspath( os.path.join( db_dir, "btc.db") ) )
