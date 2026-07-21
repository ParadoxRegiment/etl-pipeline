# Earthquake ETL Pipeline

A small, real-world ETL pipeline that pulls earthquake events from the
[USGS FDSN event API](https://earthquake.usgs.gov/fdsnws/event/1/), cleans them
into a tidy table, and loads them into a local SQLite database — orchestrated
with Apache Airflow.

> Status: in active development. This README is a skeleton; _TODO_ sections get
> filled in as the pipeline comes together.

## Why this matters

_TODO — reliable, scheduled ingestion of a live public data source into a
queryable store; the patterns here (HTTP with retries, caching raw responses,
cleaning messy real data, loading into SQL) are the core of data engineering._

## Architecture

```
Extract              Transform            Load            Orchestrate
USGS API   ──▶   clean / flatten   ──▶  one flat    ──▶  Airflow DAG
(GeoJSON)        (pandas)               SQLite table     (scheduled)
   │
   └─ raw cached to disk (data/raw/)
```

## Stack

- **Extract:** `requests` (retry/backoff via `tenacity`, added later); raw responses cached to `data/raw/`
- **Transform:** `pandas`
- **Load:** `sqlite3` (standard library) → a single flat table in `data/earthquakes.db`
- **Orchestration:** Apache Airflow (added last)
- **Tooling:** `uv`, `ruff`, `pytest`, GitHub Actions CI

## Project layout

```
src/etl/        config / extract / transform / load
tests/          pytest suite (transform first — it's pure)
data/raw/       cached raw API responses (gitignored)
data/earthquakes.db   the SQLite database (gitignored)
```

## Local setup

```bash
uv sync --dev                 # install deps into a managed venv
uv run python -m etl.extract  # smoke-test the extract step
uv run pytest                 # run tests
```

## Sample query

_TODO — once data is loaded, a SELECT that shows it's useful, e.g.:_

```sql
SELECT date(time) AS day, COUNT(*) AS quakes, MAX(mag) AS biggest
FROM earthquakes
WHERE mag >= 4.5
GROUP BY day
ORDER BY day;
```
