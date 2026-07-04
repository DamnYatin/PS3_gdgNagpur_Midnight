# Rules for Claude Code — Read Before Building

These rules apply to every step in `BUILD_STEPS.md`. If a rule and a
build step ever seem to conflict, the rule wins — ask before proceeding
rather than guessing.

## Scope lock — do not expand
- Exactly 5 crops: cotton, soybean, tur, onion, wheat. No more, no fewer.
- Exactly 5 mandis: Nagpur, Amravati, Akola, Pune, Nashik. No more, no fewer.
- Exactly 3 files total: `data/prices.csv`, `setup_db.py`, `app.py`
  (plus optionally `data/mandis.csv` if not embedding distances in code).
  Do not scaffold additional folders, config files, or modules.

## No invented integrations
- Do NOT add calls to Agmarknet, e-NAM, or any external API. This
  project uses only the local CSV/SQLite data described in
  `BUILD_STEPS.md`.
- Do NOT add a FastAPI, Flask, or any separate backend server. Streamlit
  reads directly from SQLite.
- Do NOT add authentication, user accounts, or login screens.
- Do NOT add deployment configuration (Docker, cloud config, CI/CD).
- Do NOT add a forecasting or ML model (BiLSTM, ARIMA, scikit-learn,
  etc.). The comparison logic is plain arithmetic only.
- Do NOT add SMS, WhatsApp, voice, or multi-language features.

## No invented data
- All prices, distances, and arrivals in this project are SAMPLE data
  for a demo, not real live market data. Never present them as real
  Agmarknet figures in code comments, UI text, or documentation.
- If a number is needed that isn't specified in `BUILD_STEPS.md` (e.g. a
  specific transport rate), pick one within the given range, hardcode it
  clearly, and leave a comment noting it's an assumed placeholder value.
- Do not fabricate additional crops, mandis, or data columns beyond what
  `BUILD_STEPS.md` specifies, even if it would make the demo "more
  complete."

## If something seems broken or missing
- If a step in `BUILD_STEPS.md` references a file or table that doesn't
  exist yet, stop and flag it rather than silently creating a
  workaround that changes the design.
- If you're unsure whether something is in scope, treat it as OUT of
  scope by default and flag it for confirmation instead of building it.

## Time discipline
- This is a 1-hour build. If a step is taking much longer than expected,
  cut scope (fewer crops/mandis, simpler UI) rather than add new
  approaches or libraries to "fix" it.
- Do not refactor or "clean up" working code once it passes the
  verification check in a step — move to the next step instead.
