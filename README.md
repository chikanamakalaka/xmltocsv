# xmltocsv
Scrapes XML/HTML to CSV

## Requires Python 2.6 or higher

### Required modules:

lxml

requests

requests-testadapter

## Install Python VirtualEnv (this is optional)

### `pip install virtualenv`

## Run prepare.sh

### `chmod +x prepare.sh`

### `./prepare.sh`

prepare.sh runs the following:

- `python -m virtualenv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`

## Edit xmltocsv.py to change fields to collect

## Run

### `./xmltocsv.py`