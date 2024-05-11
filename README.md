# RAOEUS Plover Dictionaries (Lapwing Theory Based)

Clone the contents of the repo directly into the plover configuration folder with `git clone https://github.com/RAOEUS/plover-dictionaries.git` and init submodules with `git submodule update --init --recursive`

The base theory for Lapwing comes from `aerick/commands.json` and `aerick/lapwing-base.json`

Credit to [@jenchanws](https://gist.github.com/jenchanws/5c8dedb826c775fc2a1521c9b9104ea9) for the raw steno python dictionaries

## Required Plover plugins:

- `plover-dict-commands` for raw mode
- `plover-python-dictionary` for Emily's Modifiers, Emily's Symbols, Jeff's Phrasing, Abby's Left-Hand Modifiers, lapwing-prefixed-proper-nouns.py, and raw.py
- `plover-retro-stringop` for retro string alterations in retro.json
- `plover-stitching` for raw mode

## Optional Plover plugins:

- plover-clippy (For the `clippy-monitor.ps1` PowerShell script)
- plover-tapey-tape (For the `tapey-tape-monitor.ps1` PowerShell script)

## modes.json
- Starter chord is SPH- for "**S**witch **M**ode"


| Mode Name   | Chord        | Notes                                                 |
|-------------|--------------|-------------------------------------------------------|
| Reset       | SPH-R        | Resets all modes                                      |
| camelCase   | SPH-PBLG     | KPA first word to get PascalCase instead              |
| CAPS        | SPH-PBG      |                                                       |
| kebap-case  | SPH-FP       |                                                       |
| lower       | SPH-L        |                                                       |
| nospaces    | SPH-FP       | Very useful for URLs.                                 |
| snake_case  | SPH-T        | You can still use KPA to capitalize                   |
| Title Case  | SPH-T        | You can still use HRO*ER to lowercase                 |


## retro.json
This dictionary is used with the `plover-retro-stringop` plugin.
- `KWR` is the arbitrary starter chord; it is always pressed.
- `STPH` represent binary numbers. For example, to retroactively change 6 words to camelCase, `TKPWR-B`. `KWR-B` is camelCase, adding `TP` for 6 words.
  - S = 8, T = 4, P = 2, H = 1
- `-R` is snake_case, `-B` is camelCase, `-G` is PascalCase, `-RB` is UPPER_SNAKE_CASE, `-BG` is kebap-case
- As an alternative to using STPH for binary numbers, you can also just repeat it once per word.
  - For example, to change three words to snake_case, `KWR-R/KWR-R/KWR-R` instead of `KPWHR-R`
 
## lapwing-prefixed-proper-nouns.py
The original lapwing-prefixed-proper-nouns.json from Lapwing is used when your machine does not have an option to re-map the top `-S` key to `#`. However, the starting `#` is, by default, mapped to `=repeat_last_translation`. I like the default stroke for repeating translations, so I created this Python dictionary to change the starting chord for proper nouns to `SKWR` instead of `#`.

You do not need to load the original lapwing-prefixed-proper-nouns.json in Plover in addition to this python dictionary.

> What's the point of this? Well, this way I can pull Aerick's commits in my submodule without having to manually find and replace the starter.

## Ordering and Enabled/Disabled

The dictionaries should be in a particular order and some should be kept disabled. This is the current order of my dictionaries, and it will be unchecked if it should be left disabled.

This information should already be stored in the plover.cfg (you can simply move this over to your main Plover config directory and then modify it), but if you don't want to use that, this may help you out.

- [x] plover-dictionaries/raw_enter.py [For creating raw steno output]
- [x] plover-dictionaries/raoeus-lapwing.json
- [x] plover-dictionaries/raoeus-commands.json
- [x] plover-dictionaries/raoeus-text-expansion.json
- [x] plover-dictionaries/modes.json
- [x] plover-dictionaries/plover-left-hand-modifiers/abby-left-hand-modifiers.py
- [x] plover-dictionaries/jeff-phrasing/jeff-phrasing.py
- [x] plover-dictionaries/emily-symbols/emily-symbols.py
- [x] plover-dictionaries/emily-modifiers/emily-modifiers.py
- [x] plover-dictionaries/lapwing-prefixed-proper-nouns.py
- [x] plover-dictionaries/lapwing-numbers.py
- [x] plover-dictionaries/aerick/lapwing-commands.json
- [x] plover-dictionaries/aerick/commands.json
- [x] plover/dictionaries/aerick/lapwing-base.json
- [ ] plover-dictionaries/raw.py [Will be the only enabled dict when raw steno mode is turned on via raw-enter.py]
