import sqlite3
import pandas as pd

DB_PATH = "mandi_compare.db"
PRICES_CSV = "data/prices.csv"

# Rough real road distances (km) from Nagpur
MANDI_DISTANCES = {
    "Nagpur": 0,
    "Amravati": 155,
    "Akola": 250,
    "Pune": 710,
    "Nashik": 680,
}


def main():
    prices = pd.read_csv(PRICES_CSV)
    mandis = pd.DataFrame(
        [{"name": name, "distance_km_from_nagpur": km}
         for name, km in MANDI_DISTANCES.items()]
    )

    with sqlite3.connect(DB_PATH) as conn:
        prices.to_sql("prices", conn, if_exists="replace", index=False)
        mandis.to_sql("mandis", conn, if_exists="replace", index=False)

        cur = conn.cursor()
        print("prices sample:")
        for row in cur.execute("SELECT * FROM prices LIMIT 5"):
            print(row)
        print("\nmandis:")
        for row in cur.execute("SELECT * FROM mandis"):
            print(row)


if __name__ == "__main__":
    main()
