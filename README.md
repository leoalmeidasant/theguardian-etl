# TheGuardianETL

Repository from project to get data from technology section on The Guardian API and store as csv files locally.

## Getting Started

### Requirements

Before start, you have to register your account to get the api-key here: https://bonobo.capi.gutools.co.uk/register/developer

You need python 3.6 and pip installed on your machine to run this application.

And, you have to set the configurations in `config.ini` file:

```ini
[DEFAULT]
SECTION=technology
API_KEY=<your-api-key>
URI=https://content.guardianapis.com/search
PAGE_SIZE=200
OUTPUT_DIR=
```

### Installing

```bash
pip install -r requirements.txt
```

### Running

To run the ETL process, you have to pass a start date and an end date, with arguments `--from-date` and `--to-date`

```bash
python run.py --from-date "2018-08-15" --to-date "2018-08-17"
```

### Running tests

To run all test cases you need to run the following command:

```bash
python -m unittest discover ./app/tests
```

## Built With

* [Python 3.6](https://www.python.org/downloads/release/python-360/) - Main language of project
* [PIP](https://pypi.org/project/pip/) - Dependency manager
* [Pandas](https://pandas.pydata.org/) - Used pandas for test case