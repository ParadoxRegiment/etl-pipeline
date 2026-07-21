# Earthquake ETL Pipeline

A production-shaped ETL pipeline that ingests earthquake events from the
[USGS FDSN event API](https://earthquake.usgs.gov/fdsnws/event/1/), cleans and
models them, and loads them into PostgreSQL — orchestrated with Apache Airflow.

> Status: in active development. This README is a skeleton; sections marked
> _TODO_ get filled in as the pipeline comes together.

## Why this matters

_TODO — the real-world framing: reliable, idempotent, scheduled ingestion of a
live public data source into a queryable warehouse; the patterns here
(retry/backoff, raw caching, star-schema modeling, idempotent upserts) are the
day-to-day of data engineering._

## Architecture

```
Extract            Transform             Load              Orchestrate
USGS API  ──▶  clean / dedupe /  ──▶  idempotent    ──▶  Airflow DAG
(GeoJSON)      type-coerce            upsert              (scheduled)
   │           (pandas)               (SQLAlchemy Core
   └─ raw cached to disk               → Postgres)
```

_TODO — replace with a proper diagram once the pieces are built._

## Stack

- **Extract:** `requests` + `tenacity` (retry/backoff), raw responses cached to disk
- **Transform:** `pandas`
- **Load:** `SQLAlchemy` Core (not the ORM) → PostgreSQL, idempotent upserts
- **Orchestration:** Apache Airflow 3 (Docker)
- **Tooling:** `uv`, `ruff`, `pytest`, GitHub Actions CI, Docker Compose

## Project layout

```
src/etl/        extract / transform / load / models / config
dags/           Airflow DAG (added in the orchestration step)
tests/          pytest suite (transform first — it's pure)
data/raw/       cached raw API responses (gitignored)
```

## Local setup

```bash
# 1. Python deps (uv manages the venv + lockfile)
uv sync --dev

# 2. Environment
cp .env.example .env      # then edit as needed

# 3. Warehouse database
docker compose up -d warehouse

# 4. Run tests
uv run pytest
```

## Sample query

_TODO — a query against the loaded data that shows it's actually useful
(e.g. daily count of M4.5+ events by region)._
