# xmltocsv
Scrapes XML/HTML to CSV

## Requires Python 2.6 or higher

### Required modules:

- lxml

- requests

- requests-testadapter

## Install Python VirtualEnv (this is optional)

- `pip install virtualenv`

## Run prepare.sh

- `chmod +x prepare.sh`

- `./prepare.sh`

prepare.sh runs the following:

1) `python -m virtualenv .venv`
2) `source .venv/bin/activate`
3) `pip install -r requirements.txt`

- Edit xmltocsv.py to change fields to collect
- Run
 `./xmltocsv.py`