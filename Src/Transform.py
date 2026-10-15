import logging
logger = logging.getLogger(__name__)

def transform_data(data):
    df_flat = data.stack(level='Ticker', future_stack=True).reset_index()

    df_flat.columns = [
        "Date",
        "Ticker",
        "Close",
        "High",
        "Low",
        "Open",
        "Volume"
    ]

    df_flat.columns = df_flat.columns.str.lower()

    df_flat = df_flat[["date", "ticker", "open", "high", "low", "close", "volume"]]

    logger.info(f"Flattened data to {len(df_flat)} rows")
    return df_flat
