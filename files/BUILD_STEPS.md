# Mandi Compare — Step-by-Step Build Plan

Follow these steps in exact order. Do not start a later step before the
current one is verified working. See `RULES.md` for constraints that
apply to every step.

## Step 1 — Create the sample data file
File: `data/prices.csv`
Columns: `crop, mandi, price_per_quintal, arrivals`
25 rows total = 5 crops × 5 mandis.

Crops: cotton, soybean, tur, onion, wheat
Mandis: Nagpur, Amravati, Akola, Pune, Nashik

Use plausible ₹/quintal ranges:
- cotton: 6500–7500
- soybean: 4500–5200
- tur: 7000–8500
- onion: 1200–2500
- wheat: 2200–2600

Arrivals: any plausible integer (e.g. 50–500 quintals/day), doesn't need
to be precise, just present in each row.

**Verify:** open the CSV, confirm 25 rows + header, no missing cells.

## Step 2 — Create the mandi reference data
Add distances (used later for transport cost), rough real road distances
from Nagpur:
- Nagpur: 0
- Amravati: 155
- Akola: 250
- Pune: 710
- Nashik: 680

This can live as a small Python dict in `setup_db.py`, or as a second
CSV `data/mandis.csv` with columns `name, distance_km_from_nagpur`.

## Step 3 — Write and run `setup_db.py`
This script should:
1. Read `data/prices.csv` with pandas
2. Load it into `mandi_compare.db` (SQLite) as table `prices`
3. Load mandi distance data into table `mandis`
4. Run once, then stop (not called again while the app runs)

**Verify:** query `SELECT * FROM prices LIMIT 5` and `SELECT * FROM mandis`
and confirm both return real rows, not empty tables.

## Step 4 — Write the comparison logic (no UI yet)
In `app.py`, write a function `compare(crop, home_mandi)`:
1. Query all mandi prices for the given crop from `prices`
2. For each mandi, compute transport cost = distance difference from
   home mandi × a flat rate (pick something in the ₹0.5–1 per
   quintal per km range, hardcoded as a constant)
3. Net price = price_per_quintal − transport cost (0 transport cost for
   the home mandi itself)
4. Return a dataframe sorted by net price, descending

**Verify:** call `compare("cotton", "Nagpur")` directly (e.g. via a quick
print or a Python shell) and confirm the output looks sane — home mandi's
net price should equal its raw price, other mandis should be adjusted.

## Step 5 — Build the Streamlit UI
Still in `app.py`, add:
1. A title and a one-line disclaimer: "Demo with sample price data, not
   a live Agmarknet feed"
2. Two `st.selectbox` widgets: crop, home mandi
3. Call `compare()` with the selected values
4. Show the result with `st.dataframe`
5. Show `st.success()` highlighting the best mandi and the ₹ gain vs
   selling at the home mandi
6. Show `st.bar_chart` of net prices across mandis

## Step 6 — Test end-to-end
Run `streamlit run app.py`. Manually click through all 5 crops with at
least 2 different home mandis each. Confirm no errors, numbers update
correctly, chart renders.

## Step 7 — Stop
Do not add features beyond this point. If time remains, spend it
rehearsing the pitch, not touching code.

## Definition of done
- App runs with `streamlit run app.py`, no errors
- All 5 crops × any home mandi produce a ranked comparison and a chart
- No network calls required to run the demo
- Sample-data disclaimer is visible in the UI
