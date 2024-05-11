LONGEST_KEY = 1

def lookup(steno):
  if len(steno) != 1:
    raise KeyError

  stroke = steno[0]
  if stroke == "KR50*E7B":
    return "{plover:solo_dict:+korean_enter.py,+dicts/easy_korean_steno/easy_Korean_steno_chorded.py,+dicts/emily-symbols/emily-symbols.py,+dicts/emily-modifiers/emily-modifiers.py,+dicts/aerick/commands.json,+dicts/aerick/lapwing-numbers.json,+dicts/plover-left-hand-modifiers/abby-left-hand-modifiers.py,+dicts/raoeus-commands.json}"
  elif stroke == "KR50*E7BD":
    return "{plover:end_solo_dict}"
  raise KeyError
