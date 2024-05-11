LONGEST_KEY = 1

def lookup(steno):
  if len(steno) != 1:
    raise KeyError

  stroke = steno[0]
  if stroke == "RA*U":
    return "{plover:solo_dict:+raw.py}"
  elif stroke == "SRA*U":
    return "{plover:solo_dict:+raw.py}{`^}"
  raise KeyError