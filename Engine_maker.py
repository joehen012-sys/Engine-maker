import json
from pathlib import Path

DATA_PATH = Path(__file__).with_name("Format.json")

def load_json():
    with DATA_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)

data = load_json()
formats = data["formats"]

def basic_engine_maker():
  format = Input("format (ex. inline, V, W, rotary): ")
  size = input("size: ")
  if format == str(inline):
    pass
  elif format == str(v):
    pass
  elif format == str(vr):
    pass
  elif format == str(w):
    pass
  elif format == str(rotary):
    pass
  else:
    pass
def advanced_engine_maker():
    pass
