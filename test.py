#!/usr/bin/python

#import enable
#from enable.api import Component, ComponentEditor

import mysql.connector as sql
import urllib as ulib
import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

base_url = "http://ichart.finance.yahoo.com/table.csv?s="
output_path = '.'


cnx = mysql.connector.connect(user='root', password='sakshi', host='localhost', database='test')
print "Opened MySQL connection"
cursor = cnx.cursor()
cursor.execute("SELECT * FROM stockprices")
print "Associated cursor"
data = cursor.fetchone();
while data is not None:
  print data
  data = cursor.fetchone();

  
  
print "Closing MySQL connection"
cnx.close()


def make_url(ticker_symbol):
    return base_url + ticker_symbol

def make_filename(ticker_symbol, directory="data"):
    return output_path + "/" + directory + "/" + ticker_symbol + ".csv"

def pull_historical_data(ticker_symbol, directory="SP"):
    try:
        urllib.urlretrieve(make_url(ticker_symbol), make_filename(ticker_symbol, directory))
    except urllib.ContentTooShortError as e:
        outfile = open(make_filename(ticker_symbol, directory), "w")
        outfile.write(e.content)
        outfile.close()


def compute_RSI30(ticker_symbol)
    stock_url = make_url(ticker_symbol)
    file_handle = urllib.urlopen(stock_url)
    
    
