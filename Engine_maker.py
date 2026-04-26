import json 

data_path = format.json

def load_json(): 
    global data_path
    path = data_path
    with open(path, 'r') as file: # 3. Open file
        data = json.load(file) # 4. Use json.load()
    return data
  
load_json()

def engine_make():
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
