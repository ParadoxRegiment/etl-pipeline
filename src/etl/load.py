"""Load layer: save the cleaned earthquakes into a local SQLite database.

Plain-English version of what's going on here:

  * A *database* is just an organized place to store rows of data that you can
    later ask questions of ("give me every quake above magnitude 6").
  * A *table* is one grid of that data -- think of a single spreadsheet tab:
    each row is one earthquake, each column is one field (mag, place, time...).
  * *SQLite* is the simplest kind of database: the ENTIRE database is a single
    file on disk (data/earthquakes.db). There's no server to install or start.
    Python talks to that file directly through the built-in `sqlite3` module,
    which is why it's perfect for learning.

We are deliberately keeping ONE flat table -- one row per earthquake, every
field as its own column. Splitting the data across multiple linked tables is
the "data warehousing" we cut out to keep this approachable.

The actual write is one pandas call: a DataFrame knows how to dump itself into
a SQL table via `df.to_sql(...)`, and it creates the columns for you from the
DataFrame's columns. You'll learn SQL on the *reading* side -- by writing
SELECT queries against the table once the data is in there.
"""

from __future__ import annotations

import sqlite3

import pandas as pd

from etl.config import DB_PATH


def load_events(df: pd.DataFrame, *, table_name: str = "earthquakes") -> None:
    """Write the cleaned earthquakes DataFrame into the SQLite table.

    Steps for you to fill in:
      1. Open a connection:  sqlite3.connect(DB_PATH) -- this CREATES the file
         if it doesn't exist yet, so there's no setup. Wrap it in `with` so it
         closes itself even if something errors.
      2. Write the data:  df.to_sql(table_name, conn, ...)
           - if_exists="replace"  -> wipe and rewrite the table each run.
             Simplest thing that works; we'll make re-runs smarter later.
           - index=False          -> don't write pandas' row-number index as a
             surprise extra column.
    """
    # TODO (you): open the connection and call df.to_sql(...)
    raise NotImplementedError("load target -- you'll write this")
