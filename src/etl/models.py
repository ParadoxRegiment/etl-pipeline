"""Warehouse schema, defined with SQLAlchemy Core (Table/MetaData, not the ORM).

We'll design a star schema here together: a fact table for earthquake
events plus dimension tables (time, location/region, ...). Core rather than
ORM is a deliberate choice — it keeps the SQL close to the surface, which is
the point of this project.
"""

from __future__ import annotations

from sqlalchemy import MetaData

metadata = MetaData()

# TODO (pair): define fact + dimension Tables against `metadata`.
#   fact_earthquake: event grain — one row per USGS event id
#   dim_time, dim_location, ...  (decide the grain and keys together)
