
from datetime import date, datetime, timedelta
import sqlite3
import time

from os.path import join, abspath

# Project Imports
from DataCollector import getTopCryptos, getHistoricalDataDaily

NUM_CRYTPOS = 35

# dir must already exist
DB_DIR = 'db'

top_cryptos = getTopCryptos(NUM_CRYTPOS)

def get_ts():
   raw = time.time()
   # Return nice format
   return datetime.fromtimestamp(raw).strftime('%Y-%m-%d_%H%M%S')

db_name = get_ts()
conn = sqlite3.connect( abspath( join( DB_DIR, db_name) ) )
c = conn.cursor()
aggr = {}  # To aggregate total value of all NUM_CRYPTOS for each date
today_price = {}

def pop_marketcap():
   # Create marketcap table
   c.execute('''CREATE TABLE marketcap
               (coin text, mkt_cap real, time_collected text)''')
   for crypto in top_cryptos:
      mkt_cap = today_price.get(crypto) / aggr.get(str(date.today()))
      ts = get_ts()
      string = "INSERT INTO marketcap VALUES ('" + str(crypto) + "', " + str(mkt_cap) + ", '" + str(ts) + "')"
      c.execute(string)

def pop_aggregate():
   # Create aggregate table for market data of all top cryptos
   c.execute('CREATE TABLE aggregate'
            '''(date text, close real, time_collected text)''')
   for ag in aggr: # ag will be a simple date string
      c.execute( "INSERT INTO aggregate VALUES ('" + str(ag) + "', " + str(aggr.get(ag)) + ", '" + str(get_ts()) + "')" )

def pop_cryptos():
   for crypto in top_cryptos:
      # Create table for each NUM_CRYTOS
      try:
         c.execute('CREATE TABLE ' + crypto +
                  '''(date text, close real, high real, low real, open real, time_collected text)''')
      except sqlite3.OperationalError:
         break # Just skip this one: Wierd symbol name like HOT*

      historData = getHistoricalDataDaily(crypto, all=True)

      days_ago = 0 # Keep track of days past for aggregate table
      for histDate in historData: 
         if days_ago == 0: # Update latest price (use for market cap)
            today_price.update( {crypto: histDate['open']})

         datestamp = str(date.today() - timedelta(days=days_ago)) # ISO-8601 date
         
         # update aggregate amount based on existing value an closing value of current crypto
         if len(aggr) > 0 and aggr.get(datestamp) is not None:
            # sum up with existing aggregated data
            aggr.update( {datestamp: (aggr.get(datestamp) + histDate['close']) } )
         else :  # first entry for this date
            aggr.update({datestamp: histDate['close']}) 
      
         estr = 'INSERT INTO ' + crypto + " VALUES ('" + datestamp + "', " + \
            str(histDate['close']) + ', ' + str(histDate['high']) + ', ' + \
            str(histDate['low']) + ', ' + str(histDate['open']) + ", '" + get_ts() +  "' )"
         
         c.execute( estr )
         days_ago += 1
def main():
   pop_cryptos()
   pop_aggregate()
   pop_marketcap()
   conn.commit()
   conn.close()

if __name__ == '__main__':
   main()