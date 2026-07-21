"""Extract layer: pull raw earthquake events from the USGS FDSN event API.

Endpoint:  GET https://earthquake.usgs.gov/fdsnws/event/1/query
Params:    format=geojson, starttime, endtime (ISO-8601), plus optional
           minmagnitude, limit, offset, orderby, ...
Returns:   a GeoJSON FeatureCollection.

Responsibilities (what we'll build together):
  - Build the request from a time window (and any filters).
  - Handle transient failures with retry/backoff.
  - Handle pagination: USGS caps a single response at 20,000 events and
    returns HTTP 400 with a "count too large" message past that. Strategy
    options we'll discuss: offset/limit paging, or time-window splitting.
  - Cache the raw response to disk *before* any processing, so a bad
    transform never costs us a re-fetch.
"""

from __future__ import annotations
import requests


def fetch_events(starttime, endtime, *, min_magnitude=None, session:requests.Session | None=None):
    """Fetch a window of earthquake events from USGS and return raw GeoJSON.

    Signature intentionally left open — we'll decide the parameters
    (time window? filters? injected session?) when we pair on this.
    """
    # raise NotImplementedError("pair-programming target")
    
    url_template = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    url_params = {
        "format": "geojson",
        "starttime": starttime,
        "endtime": endtime,
    }
    if min_magnitude is not None:
        url_params["minmagnitude"] = min_magnitude
    
    client = session or requests
    resp = client.get(url_template, params=url_params, timeout=(5, 30))
    
    resp.raise_for_status()
    events_data = resp.json()
    
    print(events_data)
    return events_data

if __name__ == "__main__":
    fetch_events("2014-01-01", "2014-01-02")