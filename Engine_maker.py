import json
from pathlib import Path

DATA_PATH = Path(__file__).with_name("Format.json")

def load_json():
    with DATA_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)

data = load_json()
formats = data["formats"]  # dict: canonical -> list of aliases


def build_format_alias_map(formats_dict: dict) -> dict:
    """
    Returns a dict mapping *any accepted user input* -> canonical format.
    Example: "i" -> "inline", "inline" -> "inline", "r" -> "rotary"
    """
    alias_map = {}

    for canonical, aliases in formats_dict.items():
        # allow typing the canonical key itself
        alias_map[canonical.strip().lower()] = canonical

        # allow typing any alias listed in JSON
        for a in aliases:
            alias_map[str(a).strip().lower()] = canonical

    return alias_map


FORMAT_ALIASES = build_format_alias_map(formats)


def normalize_format(user_value: str) -> str:
    key = user_value.strip().lower()
    canonical = FORMAT_ALIASES.get(key)
    if not canonical:
        allowed = sorted(formats.keys())
        raise ValueError(f"Unknown format '{user_value}'. Allowed formats: {allowed}")
    return canonical


def parse_positive_int(user_value: str, field_name: str) -> int:
    try:
        n = int(user_value)
    except ValueError as e:
        raise ValueError(f"{field_name} must be an integer.") from e
    if n <= 0:
        raise ValueError(f"{field_name} must be > 0.")
    return n


def basic_engine_maker():
    engine_format = normalize_format(
        input("format (inline/i, v, vr, w, rotary/r): ")
    )

    # interpret "size" as cylinder count (since you didn’t specify units)
    cylinders = parse_positive_int(input("size (cylinders): ").strip(), "size")

    # Here’s a simple “result object” you can expand later
    engine = {
        "format": engine_format,     # canonical: inline/v/vr/w/rotary
        "cylinders": cylinders,
    }

    # Branching point for future logic
    if engine_format == "inline":
        # e.g., allow 3/4/5/6 etc.
        pass
    elif engine_format == "v":
        pass
    elif engine_format == "vr":
        pass
    elif engine_format == "w":
        pass
    elif engine_format == "rotary":
        pass

    return engine


def advanced_engine_maker():
    pass
