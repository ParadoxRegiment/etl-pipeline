"""Runtime configuration, sourced from environment variables.

Design intent: everything the pipeline needs to talk to the outside world
(DB connection, API base URL, cache location) lives here, read from the
environment, so nothing downstream hard-codes a secret or a host.

We'll fill this in together. Open questions to decide when we do:
  - Plain dataclass + os.environ, or pydantic-settings for validation?
  - Do we build a single SQLAlchemy URL here, or assemble it in load.py?
"""

from __future__ import annotations

# TODO (pair): define a Settings object that reads:
#   - warehouse DB connection (user/password/host/port/name -> SQLAlchemy URL)
#   - USGS API base URL (default https://earthquake.usgs.gov/fdsnws/event/1/query)
#   - raw cache directory (default data/raw)
