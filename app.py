import sqlite3
from flask import Flask, jsonify, request, send_from_directory

DB_PATH = "mandi_compare.db"
# Assumed placeholder: flat transport rate in ₹ per quintal per km
TRANSPORT_RATE_PER_KM = 0.75

CROPS = [
    {"id": "cotton",  "mr": "कापूस",   "en": "Cotton"},
    {"id": "soybean", "mr": "सोयाबीन", "en": "Soybean"},
    {"id": "tur",     "mr": "तूर",      "en": "Tur (Arhar)"},
    {"id": "onion",   "mr": "कांदा",    "en": "Onion"},
    {"id": "wheat",   "mr": "गहू",      "en": "Wheat"},
]

MANDI_LABELS = {
    "Nagpur":   {"mr": "नागपूर",   "en": "Nagpur"},
    "Amravati": {"mr": "अमरावती", "en": "Amravati"},
    "Akola":    {"mr": "अकोला",   "en": "Akola"},
    "Pune":     {"mr": "पुणे",     "en": "Pune"},
    "Nashik":   {"mr": "नाशिक",   "en": "Nashik"},
}

app = Flask(__name__, static_folder=".", static_url_path="")


def db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@app.get("/")
def index():
    return send_from_directory(".", "index.html")


@app.get("/api/crops")
def api_crops():
    with db() as conn:
        available = {r["crop"] for r in conn.execute("SELECT DISTINCT crop FROM prices")}
    return jsonify([c for c in CROPS if c["id"] in available])


@app.get("/api/mandis")
def api_mandis():
    with db() as conn:
        rows = conn.execute(
            "SELECT name, distance_km_from_nagpur AS dist FROM mandis"
        ).fetchall()
    return jsonify([
        {
            "id": r["name"],
            "mr": MANDI_LABELS.get(r["name"], {}).get("mr", r["name"]),
            "en": MANDI_LABELS.get(r["name"], {}).get("en", r["name"]),
            "dist": r["dist"],
        }
        for r in rows
    ])


@app.get("/api/compare")
def api_compare():
    crop = request.args.get("crop", "").strip()
    home_mandi = request.args.get("home_mandi", "").strip()
    if not crop or not home_mandi:
        return jsonify({"error": "crop and home_mandi are required"}), 400

    with db() as conn:
        price_rows = conn.execute(
            "SELECT mandi, price_per_quintal, arrivals FROM prices WHERE crop = ?",
            (crop,),
        ).fetchall()
        mandi_rows = conn.execute(
            "SELECT name, distance_km_from_nagpur AS dist FROM mandis"
        ).fetchall()

    if not price_rows:
        return jsonify({"error": f"unknown crop: {crop}"}), 404
    dist_by_mandi = {r["name"]: r["dist"] for r in mandi_rows}
    if home_mandi not in dist_by_mandi:
        return jsonify({"error": f"unknown mandi: {home_mandi}"}), 404

    home_dist = dist_by_mandi[home_mandi]
    results = []
    for r in price_rows:
        name = r["mandi"]
        if name not in dist_by_mandi:
            continue
        dist_diff = abs(dist_by_mandi[name] - home_dist)
        transport = 0.0 if name == home_mandi else round(dist_diff * TRANSPORT_RATE_PER_KM, 2)
        net = round(r["price_per_quintal"] - transport, 2)
        results.append({
            "mandi": name,
            "mr": MANDI_LABELS.get(name, {}).get("mr", name),
            "en": MANDI_LABELS.get(name, {}).get("en", name),
            "raw_price": r["price_per_quintal"],
            "arrivals": r["arrivals"],
            "distance_from_home_km": dist_diff,
            "transport_cost": transport,
            "net_price": net,
        })

    results.sort(key=lambda x: x["net_price"], reverse=True)
    return jsonify({
        "crop": crop,
        "home_mandi": home_mandi,
        "transport_rate_per_km": TRANSPORT_RATE_PER_KM,
        "results": results,
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
