"""Where the entries are kept.

For now: a Python list in memory. Simple, and it forgets everything when
the app restarts. That is fine for this stage.

The rest of the app only uses the functions below. Later in the semester
this file can be replaced by one that keeps the entries somewhere else.
As long as the function names stay the same, main.py does not change.
"""

_entries = []
_next_id = 1


def all_entries():
    """Return a copy of all entries, oldest first."""
    return list(_entries)


def add_entry(thing, person):
    """Store a new entry and return it."""
    global _next_id
    entry = {"id": _next_id, "thing": thing, "person": person}
    _entries.append(entry)
    _next_id += 1
    return entry
