from config.locations import LOCATIONS


def extract_locations(text):

    locations = []

    lower = text.lower()

    for city in LOCATIONS:

        if city.lower() in lower:

            locations.append(city)

    return locations



"""
location_extractor.py

Extracts location-related information.
"""


def extract_candidate_location(candidate):

    return {
        "city": candidate['profile'].get("location"),
        "state": candidate['profile'].get("location"),
        "country": candidate['profile'].get("country"),
        "preferred_locations": candidate['redrob_signals'].get("preferred_locations", []),
        "willing_to_relocate": candidate['redrob_signals'].get("willing_to_relocate", False),
        "work_mode": candidate['redrob_signals'].get("preferred_work_mode")
    }