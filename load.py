import snowflake.connector
from extract import extract_data
from transform import transform_data
from snowflake.connector.pandas_tools import write_pandas


def load_data():

    # Extract Data
    df = extract_data()

    # Transform Data
    df = transform_data(df)

    # Snowflake Connection
    conn = snowflake.connector.connect(
        user='HARINI',
        password='YOUR_PASSWORD',
        account='ACHKARW-TR90715',
        warehouse='ETL_WH',
        database='ETL_DB',
        schema='ETL_SCHEMA'
    )

    # Load Data
    success, nchunks, nrows, _ = write_pandas(
        conn,
        df,
        'SUPERSTORE_DATA'
    )

    if success:
        print(f"{nrows} records loaded successfully.")
    else:
        print("Data Load Failed.")

    conn.close()


if __name__ == "__main__":
    load_data()
