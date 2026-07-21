"""Load layer: write transformed data into Postgres, idempotently.

The key property we're after is idempotency: running the same window twice
must not create duplicates or error. With Postgres + SQLAlchemy Core that
means INSERT ... ON CONFLICT (event_id) DO UPDATE (an upsert).

Responsibilities (pairing target):
  - Create tables if absent (metadata.create_all) or leave that to migrations.
  - Upsert dimensions, then the fact table (order matters for FKs).
  - Batch inserts so we're not doing one round-trip per row.
"""

from __future__ import annotations


def load_events():
    """Upsert transformed data into the warehouse. Signature TBD when we pair."""
    raise NotImplementedError("pair-programming target")
