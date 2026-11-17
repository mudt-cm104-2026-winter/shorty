import random, string, validators

_entries = []
_next_id = 1


def all_entries():
    """Return a copy of all entries, oldest first."""
    return list(_entries)


def create_short():
    short = "".join(random.choices(string.ascii_letters, k=5))
    for i in _entries:
        for entry in _entries:
            if entry["short"] == short:
                short = "".join(random.choices(string.ascii_letters, k=5))

    return short


def validate_url(url):
    url = url.strip()
    if not url.startswith(("https://", "http://")):
        url = "https://" + url

    return url if validators.url(url) else None


def add_entry(url, short):
    """Store a new entry and return it."""
    global _next_id
    entry = {"id": _next_id, "url": url, "short": short}
    _entries.append(entry)
    _next_id += 1
    return entry


def search_for_url(short_url):
    long_url = next(
        (item["url"] for item in _entries if item["short"] == short_url), None
    )
    return long_url
