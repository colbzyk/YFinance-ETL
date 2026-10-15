import logging
logger = logging.getLogger(__name__)

def load_data(engine, ohlc_data, company_data):
    if company_data is not None:
        company_data.to_sql(
            "company_data", 
            engine,
            if_exists="append",
            index=False
        )
        logger.info("Loading company_data to db sucessful")

    ohlc_data.to_sql(
        "portfolio_ohlc_data", 
        engine,
        if_exists="append",
        index=False
    )
    logger.info("Loading ohlc_data to db sucessful")

    