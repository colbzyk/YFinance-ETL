from Extract import extract_data
from Transform import transform_data
from Load import load_data

from dotenv import load_dotenv
import os
import yfinance as yf
import pandas as pd
import psycopg2
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

load_dotenv()
databaseURL = os.getenv("Database_URL")
engine = create_engine(databaseURL)

tickers = ["MSFT", "JPM", "UNH", "XOM", "PG", "CAT", "AMZN", "PLD", "SPY"]

data = extract_data(engine, tickers)
data = transform_data(data)
load_data(engine, data)