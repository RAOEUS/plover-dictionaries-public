LONGEST_KEY = 1

def lookup(steno):
  if len(steno) != 1:
    raise KeyError

  stroke = steno[0]
  if stroke == "T*PD":
    return "{plover:solo_dict:+toki-pona.json,+toki-pona-lawa.json}"
  raise KeyError
