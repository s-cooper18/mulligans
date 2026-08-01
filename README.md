# Mulligans

This repo is a simple mulligan simulator that handles the card "[Serum Powder](https://scryfall.com/card/ima/228/serum-powder)".
This has been made primarily for myself because I had not found an appropriate way to practise certain decklists smoothly via existing mulligan simulators.

This is a work in progress, made primarily for myself. Use at your own risk.

## Installation

- Ensure Python is installed (example, via [pyenv](https://github.com/pyenv/pyenv))
- Create virtual environment e.g. virtualenv, venv
- `pip install .` from root directory

## How to use
Copy decklist content into `tests/sample_data/decklist.txt`

Run
`python3 -m simulate_mulligans`

Share your poor mulligan choices with friends!

## Intended next steps
- Not hardcarding the input file location
- Actually adding tests
- Logging results / decisions in a format that can be saved and shared rather than just copying terminal output
- Determining a friendlier way to share this with non-programmers whether by GUI, executable, web page, link with Discord bot or something else
