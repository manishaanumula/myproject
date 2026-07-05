import snowflake.connector


def validate_data():

    conn = snowflake.connector.connect(
        user='HARINI',
        password='YOUR_PASSWORD',
        account='ACHKARW-TR90715',
        warehouse='ETL_WH',
        database='ETL_DB',
        schema='ETL_SCHEMA'
    )

    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM SUPERSTORE_DATA")

    count = cur.fetchone()[0]

    print(f"Rows available in Snowflake : {count}")

    cur.close()
    conn.close()


if __name__ == "__main__":
    validate_data()
