"""Tests for the transform layer.

Transform is pure (GeoJSON in, DataFrame out) with no I/O, which makes it the
natural place to start testing. We'll add real cases once transform exists:
  - a normal feature flattens to the expected row
  - null mag / null place are handled
  - duplicate ids collapse to one row
  - epoch-millis converts to the correct UTC timestamp
"""

import pytest


@pytest.mark.skip(reason="transform not implemented yet — pairing target")
def test_placeholder():
    pass
