"""Transform layer: GeoJSON FeatureCollection -> tidy, typed DataFrame(s).

Each GeoJSON feature looks like:
    {
      "id": "us7000abcd",
      "properties": {"mag": 4.2, "place": "...", "time": 1690000000000,
                     "type": "earthquake", "magType": "mb", ...},
      "geometry": {"type": "Point", "coordinates": [lon, lat, depth_km]}
    }

Responsibilities (pairing target):
  - Flatten properties + geometry into columns.
  - Coerce types (epoch-millis -> UTC timestamp; numeric mag/depth).
  - Deduplicate on the event id.
  - Handle missing values sensibly (mag can be null, place can be null).
  - Shape the output to match the star schema we design in models.py.
"""

from __future__ import annotations


def transform_events():
    """Turn raw GeoJSON into the DataFrame(s) the load layer expects.

    Parameters/return shape left open until we've designed the schema.
    """
    raise NotImplementedError("pair-programming target")
