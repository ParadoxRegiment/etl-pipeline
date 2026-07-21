"""Transform layer: turn the raw GeoJSON into a clean, FLAT table of events.

Input:  the GeoJSON dict from extract (a "FeatureCollection").
Output: a pandas DataFrame with ONE ROW PER EARTHQUAKE and one column per
        field we care about -- exactly the shape that drops straight into a
        single SQLite table in load.py.

Each feature looks like:
    {
      "id": "us7000abcd",
      "properties": {"mag": 4.2, "place": "...", "time": 1690000000000,
                     "magType": "mb", "type": "earthquake", ...},
      "geometry": {"type": "Point", "coordinates": [lon, lat, depth_km]}
    }

The real work (pairing target):
  - Pull each feature's `id`, its `properties`, and its `geometry.coordinates`
    into flat columns.
  - Split coordinates -> longitude, latitude, depth  (remember: LON is first).
  - Convert `time` / `updated` from epoch-milliseconds to real timestamps.
  - Decide what to do with missing values (mag, felt, cdi, mmi are often null).
  - Drop duplicate ids if any slipped in.
"""

from __future__ import annotations

import pandas as pd


def transform_events(geojson: dict) -> pd.DataFrame:
    """Flatten a USGS GeoJSON FeatureCollection into a tidy DataFrame."""
    raise NotImplementedError("pair-programming target")
