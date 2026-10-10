
def load_data(engine, data):
    data.to_sql(
        "portfolio_ohlc_data", 
        engine,
        if_exists="append",
        index=False
    )