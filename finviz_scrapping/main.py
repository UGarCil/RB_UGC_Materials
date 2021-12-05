'''
Created by Uriel Garcilazo Cruz on 12/5/2021
Send get request to finviz and parse the received content using bs4
'''

import os
import requests
from bs4 import BeautifulSoup

# Domain analysis
# link -> requests -> bs4 -> [str,str,str,...]
# --> link --> requests -> bs4 -> <pd.Dataframe> -> .xls File


# CONSTANTS
PATH = os.getcwd()
LINK = "https://finviz.com/screener.ashx?v=111&f=geo_usa&r=21"

#~~~~~~~~~~~~~~~~~~~~~~~~ Defining Functions ~~~~~~~~~~~~~~~~~~~~
# Function def. extractTk(sp)
# Signature: <class 'bs4.results'> -> l_o_tk
# purp.: extract tickers from results
def extractTk(l_o_r):
    l_o_tk = []
    for r in l_o_r:
        # expression that finds the ticker in tr
        pass
    return(l_o_tk)




# Function def. findTickers(sp)
# Signature: <class 'bs4.BeautifulSoup'> -> l_o_tk
# purp.: extract tickers from soup

def findTickers(sp):
    # _sp = soup.findAll('table')[0]
    _sp = soup.findAll("table")[0]
    _sp = soup.findAll("tr")
    return(extractTk(_sp))
#~~~~~~~~~~~~~~~~~~~~~~~~ Defining Data ~~~~~~~~~~~~~~~~~~~~
# Data def. ticker
# tk = str
# interp. value in the Ticker column of finviz
# Examples
tk0 = "A"
tk1 = "AA"
tk2 = "ABGI"
tk3 = "ABIO"

# Data def. list of ticker
# l_o_t = [tk, tk, tk,...]
# interp. list of tickers extracted from request to finviz
# Examples
l_o_tk0 = [tk1]
l_o_tk1 = [tk1, tk2]
l_o_tk2 = [tk1, tk2, tk3]


# Extract l_o_tk
response = requests.get(LINK)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)
l_o_tk3 = findTickers(soup)




