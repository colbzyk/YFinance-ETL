from Extract import extract_data
from Transform import transform_data
from Load import load_data
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

load_dotenv()
databaseURL = os.getenv("Database_URL")
engine = create_engine(databaseURL)

tickers = ["MSFT", "JPM", "UNH", "XOM", "PG", "CAT", "AMZN", "PLD", "SPY"]

logger.info(f"Starting pipeline with tickers: {tickers}")
try:
    ohlc_data, company_data = extract_data(engine, tickers)
    ohlc_data = transform_data(ohlc_data)
    load_data(engine, ohlc_data, company_data)
    logger.info("Pipeline finished")
except Exception:
    logger.exception("Pipeline Failed")
    raise