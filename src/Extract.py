import yfinance as yf
from sqlalchemy import text
from sqlalchemy.orm import Session
from datetime import timedelta
import pandas as pd
import logging
logger = logging.getLogger(__name__)

def extract_data(engine, tickers):
    session = Session(engine)
    maxDate = session.execute(text("SELECT max(date) from portfolio_ohlc_data")).scalar()
    session.close()

    if maxDate is None:
        date = "2022-01-01"
        ohlc_data = yf.download(tickers, start=date)
        company_data = []

        for t in tickers:
            ticker = yf.Ticker(t)
            info = ticker.info

            row = {
                "ticker" : t,
                "name" : info.get("displayName"),
                "sector" : info.get("sector"),
                "industry" : info.get("industry")
            }
            company_data.append(row)

        company_data = pd.DataFrame(company_data)

        logger.info(f"Extracted {len(ohlc_data)} ohlc rows and {len(company_data)} company data rows from date: {date}")
        return ohlc_data, company_data

    else:
        startDate = maxDate + timedelta(days=1)
        ohlc_data = yf.download(tickers, start= startDate)

        logger.info(f"Extracted {len(ohlc_data)} ohlc rows to append from date: {startDate}")
        return ohlc_data, None

