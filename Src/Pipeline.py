from Extract import extract_data
from Transform import transform_data
from Load import load_data

from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv()
databaseURL = os.getenv("Database_URL")
engine = create_engine(databaseURL)

tickers = ["MSFT", "JPM", "UNH", "XOM", "PG", "CAT", "AMZN", "PLD", "SPY"]

ohlc_data, company_data = extract_data(engine, tickers)
ohlc_data = transform_data(ohlc_data)
load_data(engine, ohlc_data, company_data)